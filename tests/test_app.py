import os
import pytest
import shutil
from pathlib import Path

output = Path("sample_data/output/").resolve()
output2 = Path("sample_data/output2/").resolve()
csvfile = Path("sample_data/names.csv").resolve()
html = Path("sample_data/output/letter_from_Doc.html").resolve()
html2 = Path("sample_data/output/letter_from_Doc_2.html").resolve()
main = Path("scripts/__main__.py").resolve()


def teardown():
    shutil.rmtree(output, ignore_errors=True)
    shutil.rmtree(output2, ignore_errors=True)


@pytest.fixture(scope="session", autouse=True)
def wordfile():
    wordfile = Path("sample_data").resolve() / "letter_from_Doc.docx"
    yield wordfile

    teardown()


def test_word_to_html_1(wordfile):
    command = f'python "{main}" --wordfile "{wordfile}"'
    os.system(command)
    # check if the output html file exists
    assert os.path.exists(html)


def test_word_to_html_2(wordfile):
    command = f'python "{main}" --wordfile "{wordfile}" --htmlfile "{html2}"'
    os.system(command)
    # check if the output html file exists
    assert os.path.exists(html2)


def test_wordtemplate_to_html_1(wordfile):
    command = f'python "{main}" --wordfile "{wordfile}" --csvfile "{csvfile}"'
    os.system(command)
    # check if word template was converted to html template
    assert os.path.exists(html)
    # check if the two html files exists in output/output
    rendered_htmlfiles = [
        f for f in output.iterdir() if f.is_file() and "htm" in f.suffix
    ]
    assert len(rendered_htmlfiles) - 1 == 2


def test_wordtemplate_custom_output(wordfile):
    command = f'python "{main}" --wordfile "{wordfile}" --csvfile "{csvfile}" --outputdir "{output2}"'
    os.system(command)
    # check if word template was converted to html template
    assert os.path.exists(html)
    # check if the two html files exists in output2
    rendered_htmlfiles = [
        f for f in output2.iterdir() if f.is_file() and "htm" in f.suffix
    ]
    assert len(rendered_htmlfiles) == 2


if __name__ == "__main__":
    wordfile = Path("sample_data").resolve() / "letter_from_Doc.docx"
    test_word_to_html_1(wordfile)
    test_word_to_html_2(wordfile)
    test_wordtemplate_to_html_1(wordfile)
    test_wordtemplate_custom_output(wordfile)
    teardown()
