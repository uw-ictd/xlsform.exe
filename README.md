If possible use the online XLSForm converter or formhub.
XLSForm.exe won't work on all Windows systems, it doesn't run the output xml through ODK Validate,
and it won't be updated as frequently.

Running:
--------
Download the zip [here](http://www.google.com).
Extract it.
To convert XLSForms drag them onto XLSForm.exe, an xform with the same name will appear.


Problems:
---------

There might be some missing libraries that I didn't package with the exe.

If you can I suggest just using the python script directory.

Building:
---------

python setup.py py2exe


Setting up Python on Windows:
-----------------------------

http://www.python.org/download/releases/2.6.6/
(Python version is very important. Ealier versions have unicode kwarg bug, later versions don't work with py2exe)

http://pypi.python.org/pypi/setuptools

set PYTHONPATH=%PYTHONPATH%;C:\Python26\
set PATH=%PATH%;C:\Python26\
set PATH=%PATH%;C:\Python26\Scripts

easy_install pip
pip install xlrd


lxml might also be needed. I had to use the windows installer for that here:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
