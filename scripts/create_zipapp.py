import os
import shutil
from pathlib import Path

main_file = Path('scripts/__main__.py').resolve()
requirements_file = Path('requirements.txt').resolve()
app_name = Path('doc2html_app').resolve()

# delete app_name and its contents and recreate an empty app_name directory
shutil.rmtree(app_name, ignore_errors=True)
app_name.mkdir(exist_ok=True)

# copy main_file to the app_name/__main__.py
with open(app_name / '__main__.py', 'w', encoding='utf-8-sig') as f:
    with open(main_file, 'r', encoding='utf-8-sig') as f2:
        f.write(f2.read())

# install dependencies to the packaging folder
command = f'python -m pip install -r "{requirements_file}" --target "{app_name}"'
os.system(command)

# create the package
command = f'python -m zipapp -p "python" "{app_name}"'
os.system(command)

# delete packaging folder and its contents
shutil.rmtree(app_name, ignore_errors=True)
