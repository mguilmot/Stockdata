@echo off
SET pythonpath=C:\python\Python34\

rd /s /q dist

%pythonpath%python.exe setup_py2exe.py install
%pythonpath%python.exe setup_py2exe.py py2exe

TIMEOUT /T 2
rd /s /q build
rd /s /q __pycache__