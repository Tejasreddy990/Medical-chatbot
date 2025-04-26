import os
from pathlib import Path
import logging


logging.basicConfig(
    level=logging.INFO,          
    format='[%(asctime)s]: %(message)s:' 
)

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")
    
   
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")
