"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Main_Interface.py']
DATA_FILES = []
OPTIONS = {'iconfile': 'icon.icns',
           'plist': {
                        'CFBundleName': 'momofish',  # 应用名
                        'CFBundleDisplayName': 'momofish',  # 应用显示名
                        'CFBundleVersion': '1.0.0',  # 应用版本号
                    }
           }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
