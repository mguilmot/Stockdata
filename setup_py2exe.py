from distutils.core import setup
from setup_py2exe_scriptdetails import *
import py2exe
import glob

DATA=[('imageformats',['C:\\Python/Python34/Lib/site-packages/PyQt5/plugins/imageformats/qjpeg.dll',
    'C:\\Python/Python34/Lib/site-packages/PyQt5/plugins/imageformats/qgif.dll',
    'C:\\Python/Python34/Lib/site-packages/PyQt5/plugins/imageformats/qico.dll',
    'C:\\Python/Python34/Lib/site-packages/PyQt5/plugins/imageformats/qmng.dll',
    'C:\\Python/Python34/Lib/site-packages/PyQt5/plugins/imageformats/qsvg.dll',
    'C:\\Python/Python34/Lib/site-packages/PyQt5/plugins/imageformats/qtiff.dll'
    ]),('platforms',['C:\\Python/Python34/Lib/site-packages/PyQt5/plugins/platforms/qwindows.dll']),('.',[scripticon,'README.txt']),scriptextraincludes]

includes = ["sip",
            "PyQt5",
            "PyQt5.QtCore",
            "PyQt5.QtGui"]

setup(
    name=scriptname,
    version=scriptver,
    url='',
    license=scriptcopyright,
    windows=[
        {
            "script": scriptpath,
            "icon_resources": [(1, scripticon)]
        }
    ],
    scripts=[scriptpath],
    data_files = DATA,
    options={
        "py2exe":{
            "includes": includes,
            "bundle_files": 1,
            "optimize": 2,
            "packages":scriptpackages,
        }
    },
)


try:
    import setup_py2exe_extra
except:
    # does not exist
    pass