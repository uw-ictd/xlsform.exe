If possible use the online [XLSForm converter](http://opendatakit.org/use/xlsform/).
XLSForm.exe won't work on all Windows systems, it doesn't run the output xml through ODK Validate, and it won't be updated as frequently as the online version.

Using XLSForm.exe:
------------------
1. Download the zip [here](http://opendatakit.org/downloads/download-info/xlsform-for-windows/).
2. Extract it somewhere.
3. Drag an XLSForm onto xlsform.exe. A corresponding xform will appear in the output directory.

___________________________________


Problems:
---------

Some systems might be missing the Microsoft Visual C runtime DLL [and it is not bundled with the exe](http://www.py2exe.org/index.cgi/Tutorial#A5.ProvidingtheMicrosoftVisualCruntimeDLL).

If you are familiar with Python one work around would be to run [the XLSForm code](https://github.com/UW-ICTD/pyxform) directly.

Setting up Python on Windows:
-----------------------------

http://www.python.org/download/releases/2.6.6/
(Python version is very important. Ealier versions have unicode kwarg bug, later versions don't work with py2exe)

[Install setup-tools](http://pypi.python.org/pypi/setuptools)

```Shell
set PYTHONPATH=%PYTHONPATH%;C:\Python26\
set PATH=%PATH%;C:\Python26\
set PATH=%PATH%;C:\Python26\Scripts
```

```
easy_install pip
pip install xlrd
```

lxml might also be needed. Use the windows installer for that here:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml

Install [py2exe](http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/)

Building the exe:
-----------------

1. Download the pyxform source and add the nested pyxform folder to this project's root.

2. In this projects root directory `python setup.py py2exe`

3. Create an `output` directory within the `dist` directory.

4. Rename the `dist` directory to `xlsform`.

5. Right-click on `xlsform`, choose Send To / Compressed (zipped) folder.  

The resulting zip file is equivalent to the zip available on the opendatakit.org downloads page
