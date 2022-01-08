import pathlib
import os
a= pathlib.Path(os.getcwd())
for i, a in enumerate(a.glob('*.docx')):
    new_name = str(i) + '.docx'
    a.rename(new_name)
   
