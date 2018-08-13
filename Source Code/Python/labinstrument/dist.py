#!/usr/bin/python
# coding:utf-8
__Author__ = 'Adair.l'
import os
import shutil
os.system('python3 setup.py sdist bdist_wheel')
try:
    shutil.rmtree("dist_compiled")
    os.remove('dist_compiled')
    os.mkdir('dist_compiled')
except:
    pass
shutil.move("dist",'dist_compiled')
shutil.move("build",'dist_compiled')
shutil.move("labinstrument.egg-info",'dist_compiled')