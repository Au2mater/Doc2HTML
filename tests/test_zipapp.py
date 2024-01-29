import os
from tests.test_app import teardown, wordfile

# test the package
app_dir = "doc2html_app"


def test_word_to_html_1(wordfile):
    command = f"python {app_dir}.pyz --wordfile {wordfile}"
    os.system(command)
    # check if the output html file exists
    assert os.path.exists("sample_data/output/letter_from_Doc.html")
