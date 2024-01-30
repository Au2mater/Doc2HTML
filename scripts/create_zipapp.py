import os
import shutil

main_file = "scripts/__main__.py"
requirements_file = "requirements.txt"
app_name = "doc2html_app"

# delete app_name and it's contents and recreate an empty app_name directory
shutil.rmtree(app_name, ignore_errors=True)
os.makedirs(app_name, exist_ok=True)

# copy main_file to the app_name/__main__.py
with open(os.path.join(app_name, "__main__.py"), "w") as f:
    with open(main_file, "r") as f2:
        f.write(f2.read())

# install dependencies to the packaging folder
command = f"python -m pip install -r {requirements_file} --target {app_name}"
os.system(command)

# create the package
command = f'python -m zipapp -p "python" {app_name}'
os.system(command)

# delete packaging folder and it's contents
shutil.rmtree(app_name, ignore_errors=True)