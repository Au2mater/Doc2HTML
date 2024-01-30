import os
import pytest
import shutil


output = "sample_data/output/"
output2 = "sample_data/output2/"
csvfile = "sample_data/names.csv"
html = "sample_data/output/letter_from_Doc.html"
html2 = "sample_data/output/letter_from_Doc_2.html"


def teardown():
    shutil.rmtree(output, ignore_errors=True)
    shutil.rmtree(output2, ignore_errors=True)


@pytest.fixture(scope="session", autouse=True)
def wordfile():
    wordfile = "sample_data/letter_from_Doc.docx"

    yield wordfile

    teardown()


def test_word_to_html_1(wordfile):
    command = f"python scripts\\__main__.py --wordfile {wordfile}"
    os.system(command)
    # check if the output html file exists
    assert os.path.exists(html)


def test_word_to_html_2(wordfile):
    command = f"python scripts\\__main__.py --wordfile {wordfile} --htmlfile {html2}"
    os.system(command)
    # check if the output html file exists
    assert os.path.exists(html2)


def test_wordtemplate_to_html_1(wordfile):
    command = f"python scripts\\__main__.py --wordfile {wordfile} --csvfile {csvfile}"
    os.system(command)
    # check if word template was converted to html template
    assert os.path.exists(html)
    # check if the two html files exists in output/output
    rendered_htmlfiles = [
        os.path.join(output, "output", f)
        for f in os.listdir(os.path.join(output, "output"))
        if "htm" in f
    ]
    assert len(rendered_htmlfiles) == 2


def test_wordtemplate_custom_output(wordfile):
    output2 = "sample_data/output2"
    command = f"python scripts\\__main__.py --wordfile {wordfile} --csvfile {csvfile} --outputdir {output2}"
    os.system(command)
    # check if word template was converted to html template
    assert os.path.exists(html)
    # check if the two html files exists in output2
    rendered_htmlfiles = [
        os.path.join(output2, f) for f in os.listdir(output2) if "htm" in f
    ]
    assert len(rendered_htmlfiles) == 2


if __name__ == "__main__":
    wordfile = "sample_data/letter_from_Doc.docx"
    # test_word_to_html_1(wordfile)
    # test_word_to_html_2(wordfile)
    test_wordtemplate_to_html_1(wordfile)
    # test_wordtemplate_custom_output(wordfile)
    teardown()
