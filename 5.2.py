import pathlib
import os
a = pathlib.Path(os.getcwd())
for i in a.glob('*.docx'):
    i.unlink()
