
<img src="doc2html.png" alt="Alt DOC2HTML" width="300" >

## Contents

- [Description](#description)
- [Use Cases](#use-cases)
  - [Mail Merge](#mail-merge)
  - [Content Management Systems](#content-management-systems)
  - [Web Publishing](#web-publishing)
- [Installation](#installation)
  - [Command-Line Interface (CLI)](#command-line-interface-cli-1)
  - [Alteryx Macro](#alteryx-macro-1)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Alteryx Macro](#alteryx-macro)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

Doc2HTML converts Word documents and word templates to HTML format. The application can be run as a standalone zipapp, requiring only Python >= 3.8.5 or as an Alteryx Macro, using Alteryx's built-in Python interpreter.
Doc2HTML is a pure Python application that has no C dependencies, making it highly portable across different systems. It uses the `mammoth` library for the conversion and `jinja2` for HTML templating.

## Use Cases

Doc2HTML can be used in a variety of scenarios where conversion of Word documents to HTML is required. 
Maintain the original formatting and styles from the Word document in a format that can be easily viewed in a web browser.
In Alteryx, it can be used to convert Word documents to formatted reports, which can then be sent using the Email tool.

### Templates

Doc2HTML can be used to convert a single Word template to multiple HTML files, each with different data. This is useful for mail merge operations where you want to create multiple documents based on a single template but with different data for each document.

To achieve this, you need to create a CSV file and a Word template. 
The CSV file should contain the data for each document. The Word template should contain placeholders for the data in the CSV file. The placeholders should be in the format `{{column_name}}`, where `column_name` is the name of the column in the CSV file. The CSV file should have a header row with the column names. The column names should match the placeholders in the Word template.
See the csv and word template in the sample data for an example.
Read more about jinja2 templating [here](https://jinja.palletsprojects.com/en/3.0.x/templates/).

In Alteryx, no csv file is needed, the input data is passed to the macro as a data stream. 

## Installation

### Command-Line Interface (CLI)
For simple usage, ensure you have Python >= 3.8.5 installed and download the [`doc2html_app.pyz`](https://github.com/Au2mater/Doc2HTML/blob/main/doc2html_app.pyz) file from the repository.

### Alteryx Macro
Download the [`Alteryx_Doc2HTML.zip`](https://github.com/Au2mater/Doc2HTML/blob/main/Alteryx_Doc2HTML.zip) file from the repository. This contains the Alteryx macro and sample data.

## Usage

Word2HTML can be used in two ways: as aas a command-line application and an Alteryx macro.

### Command-Line Interface (CLI)
Run the application with the path to the Word document as an argument:
```sh
python doc2html_app.pyz --wordfile sample_data/sample_word_file.docx
```
This will create an HTML file in the same directory as the Word file, with the same name as the Word file but with a .html extension.

The application provides several command-line arguments to customize its behavior:

- `-h, --help`: Displays the help message and exits the program. Use this if you need a quick reminder of the command-line arguments.
- `--wordfile WORDFILE`: Specifies the path to the Word file that you want to convert to HTML. This is a required argument.
- `--htmlfile HTMLFILE`: (Optional) Specifies the path to the output HTML file. If this argument is not provided, the HTML file will be created in the same directory as the Word file, and it will have the same name as the Word file but with a .html extension.
- `--csvfile CSVFILE`: (Optional) Specifies the path to a CSV file that contains data for rendering the Word template. This is useful for mail merge operations where you want to create multiple documents based on a single template but with different data for each document.
- `--outputdir OUTPUTDIR`: (Optional) Specifies the path to the directory where the output HTML files from a template should be saved. If this argument is not provided, the output files will be saved in the same directory as the Word file in an `output` subdirectory. This is only applicable when using a Word template.

Here's an example of how to use these arguments:

```sh
python doc2html_app.pyz --wordfile path_to_your_word_file --htmlfile path_to_your_html_file --outputdir path_to_your_output_dir --csvfile path_to_your_csv_file
``` 
### Alteryx Macro
Unzip the `Alteryx_Doc2HTML.zip`.To use the macro, open the Alteryx workflow in the Alteryx Designer and drag the macro onto the canvas. Connect the macro to the rest of your workflow and configure the macro as follows:
![Alt text](screenshot.jpg)

## Development
For further development, clone the repository to your local machine:

```sh
git clone https://github.com/yourusername/doc2html.git
```
create a virtual environment and install the dependencies:
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r dev_requirements.txt
```
To recreate the zip app, run the create_zipapp.py script in the scripts directory.
```sh
python scripts/create_zipapp.py
```
This will overwrite the zipapp in the root directory of the project.

For testing, run the following command:
```sh
pytest tests
```
## Contributing
Contributions are welcome. Please make sure to update tests as appropriate.

## License
MIT

