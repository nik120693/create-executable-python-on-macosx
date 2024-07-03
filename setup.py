from setuptools import setup

APP = ['simple_tkinter_app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'frameworks': ['/System/Library/Frameworks/Tk.framework'],
}


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
