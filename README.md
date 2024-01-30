
<img src="doc2html.png" alt="Alt DOC2HTML" width="300" >

## Contents

- [Description](#description)
- [Use Cases](#use-cases)
  - [Mail Merge](#mail-merge)
  - [Content Management Systems](#content-management-systems)
  - [Web Publishing](#web-publishing)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Alteryx Macro](#alteryx-macro)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

Doc2HTML converts Word documents and templates to HTML format. It uses the `mammoth` library for the conversion and `jinja2` for HTML templating. The application can be run as a standalone zipapp, requiring only Python >= 3.8.5. It is a pure Python application that has no C dependencies, making it highly portable across different systems.

## Use Cases

Doc2HTML can be used in a variety of scenarios where conversion of Word documents to HTML is required. Here are a few examples:

### Mail Merge

If you have a Word document template for a mail merge, you can use Doc2HTML to convert this template to HTML. You can then programmatically insert the relevant data into the HTML template for each recipient of the mail merge. This allows you to create personalized emails in bulk.

### Content Management Systems

If you're working with a content management system (CMS) that accepts HTML input, you can use Doc2HTML to convert Word documents to HTML. This can be useful if your content creators prefer to work in Word, but your CMS requires HTML.

### Web Publishing

If you want to publish Word documents on the web, you can use Doc2HTML to convert them to HTML. This allows you to maintain the original formatting and styles from the Word document in a format that can be easily viewed in a web browser.

## Installation

For simple usage, ensure you have Python >= 3.8.5 installed and download the `doc2html_app.pyz` file from the repository.

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
- `--outputdir OUTPUTDIR`: (Optional) Specifies the path to the directory where the output HTML file should be saved. If this argument is not provided, the output will be saved in the same directory as the Word file.
- `--csvfile CSVFILE`: (Optional) Specifies the path to a CSV file that contains data for rendering the Word template. This is useful for mail merge operations where you want to create multiple documents based on a single template but with different data for each document.

Here's an example of how to use these arguments:

```sh
python doc2html_app.pyz --wordfile path_to_your_word_file --htmlfile path_to_your_html_file --outputdir path_to_your_output_dir --csvfile path_to_your_csv_file
``` 
### Alteryx Macro
Download the Alteryx_Doc2HTML.zip file from the repository. This contains the Alteryx macro and sample data. To use the macro, open the Alteryx workflow in the Alteryx Designer and drag the macro onto the canvas. Connect the macro to the rest of your workflow and configure the macro as follows:
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

