import mammoth
from jinja2 import Environment, FileSystemLoader
import sys
from pathlib import Path
import argparse
import csv


def validate_word_file(filepath: str):
    """check if filepath exists and is a valid word document"""
    fileext = Path(filepath).suffix
    if not (Path(filepath).is_file() and fileext in [".doc", ".docx"]):
        raise Exception("File is not an existing word document")
    return True


def validate_csv_file(filepath: str):
    """check if filepath exists and is a valid csv document"""
    fileext = Path(filepath).suffix
    if not (Path(filepath).is_file() and fileext == ".csv"):
        raise Exception("File is not an existing csv document")
    return True


def validate_html_file(filepath: str):
    """check if filepath exists and is a valid html document"""
    fileext = Path(filepath).suffix
    if fileext not in [".html", ".htm"]:
        raise Exception("File is not an existing html document")
    return True


# %%


def doc2html(input: str, output: str = None):
    """
    convert a word document to html
    params:
    input: path to word document
    output: (optional) path to output html file. Default to same directory as input
    """
    with open(input, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
    if output is not None:
        # ensure that output directory exists
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w", encoding="utf-8") as html_file:
            html_file.write(result.value)
            print(f"written to {output}")
    else:
        output = str(Path(input).parent / "output" / Path(input).stem) + ".html"
        # ensure that output directory exists
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w", encoding="utf-8") as html_file:
            html_file.write(result.value)
            print(f"converted html written to {output}")
    return output


def render_template(template_file: str, csvfile: str, output: str = None):
    """
    render an html file with jinja2 template
    params:
    template_file: path to html template file
    csvfile: path to csv file
    output: (optional) path to output directory. Default to same directory as template
    """
    if not (validate_html_file(template_file) and validate_csv_file(csvfile)):
        # catch exception
        return

    with open(csvfile, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = []
        for rownum, row in enumerate(reader):
            # if rownum is a valid column name, use it as rownum
            if "rownum" in row.keys():
                row["rownum"] = row["rownum"]
            else:
                row["rownum"] = rownum + 1
            rows.append(row)
    print(rows)
    # create output directory if it does not exist
    if output is None:
        output = str(Path(template_file).parent)
    Path(output).mkdir(parents=True, exist_ok=True)
    print("output directory created")

    # read the html file
    with open(template_file, "r", encoding="utf-8") as f:
        template = f.read()

    # render the html file with jinja2
    env = Environment(loader=FileSystemLoader("."))
    template = env.from_string(template)
    for context in rows:
        output_content = template.render(context)
        output_filename = f"{Path(template_file).stem}_{context['rownum']}.html"
        output_path = Path(output) / output_filename
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_content)
        print(f"wrote {output_filename} to {output}")

    return output


# %%

# predefined arguments
# Create the parser
parser = argparse.ArgumentParser(
    description="Convert word documents and templates to html."
)

# Add the arguments
parser.add_argument("--wordfile", type=str, help="Path to word file")
parser.add_argument(
    "--htmlfile",
    type=str,
    help="(Optional) Path to output html file. Default to same directory as wordfile",
    default=None,
)
parser.add_argument(
    "--outputdir",
    type=str,
    help="(Optional) Path to output directory. Default to same directory as wordfile",
    default=None,
)
parser.add_argument(
    "--csvfile",
    type=str,
    help="(Optional) Path to csv file for word template rendering",
    default=None,
)

if len(sys.argv) > 1:
    args = parser.parse_args()

    wordfile = args.wordfile
    output = args.outputdir
    csvfile = args.csvfile
    htmlfile = args.htmlfile

    if not validate_word_file(wordfile):
        print("not a path to a valid word document")
        exit()


# cli manual input arguments
else:
    wordfile = None
    htmlfile = None
    csvfile = None
    output = None
    while wordfile is None:
        print("path to wordfile")
        wordfile = input()
        if not validate_word_file(wordfile):
            print("not a path to a valid word document")

        print("[optional] select html output file name")
        htmlfile = input()
        if htmlfile == "":
            htmlfile = None

        print("[optional] select csv file name")
        csvfile = input()
        if csvfile == "":
            csvfile = None

# execute conversion
if wordfile is not None:
    if csvfile is not None:
        template_file = doc2html(input=wordfile, output=htmlfile)
        outputdir = render_template(
            template_file=template_file, csvfile=csvfile, output=output
        )
    else:
        doc2html(wordfile, htmlfile)
