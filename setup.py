from os import name
from ssl import Options
from cx_Freeze import executable, setup, Executable


setup(
    name='Heitor Stalker',
    version='0.1',
    description="Aplicativo para Stalkear o Heitor",
    options={
        'build_exe': {
            'includes': ['tkinter', 'feedparser', 'sgmllib']
        }},
    executables=[
        Executable('heitorstalker01.py', base=None)
    ],

)
