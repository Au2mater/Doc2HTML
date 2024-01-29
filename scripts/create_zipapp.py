import os
import shutil

app_dir = "doc2html_app"

# delete app_dir and it's contents and recreate an empty app_dir
shutil.rmtree(app_dir, ignore_errors=True)

os.makedirs(app_dir, exist_ok=True)

# copy scripts/__main__.py to the app_dir/__main__.py
with open(os.path.join(app_dir, "__main__.py"), "w") as f:
    with open("scripts/__main__.py", "r") as f2:
        f.write(f2.read())

# install dependencies to the packaging folder
command = f"python -m pip install -r requirements.txt --target {app_dir}"
os.system(command)

# create the package
command = f'python -m zipapp -p "python" {app_dir}'
os.system(command)

# delete app_dir and it's contents
shutil.rmtree(app_dir, ignore_errors=True)