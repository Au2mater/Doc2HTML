from pathlib import Path
import os


def test_word_to_html_1(wordfile):
    app_dir = Path("doc2html_app").resolve()
    command = f'python "{app_dir}.pyz" --wordfile "{wordfile}"'
    os.system(command)
    # check if the output html file exists
    output_file = Path("sample_data/output/letter_from_Doc.html").resolve()
    assert output_file.exists()
