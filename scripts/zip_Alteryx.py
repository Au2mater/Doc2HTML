""" zip Alteryx folder and sample_data folder """
import os
import zipfile
from pathlib import Path

folders = [Path(f).resolve() for f in ['Alteryx', 'sample_data']]
archive_name = Path('Alteryx_Doc2HTML.zip').resolve()

# archive both folders to zip file, result in the following structure:
# Alteryx_Doc2HTML.zip
# ├── Alteryx
# ├── sample_data

with zipfile.ZipFile(archive_name, 'w') as zipf:
    for folder in folders:
        for root, _, files in os.walk(folder):
            for file in files:
                if Path(file).suffix == '.bak':
                    continue
                zipf.write(os.path.join(root, file), arcname=os.path.join(folder.name, file))

