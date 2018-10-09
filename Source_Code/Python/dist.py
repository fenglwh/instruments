#!/usr/bin/python
# coding:utf-8
__Author__ = 'Adair.l'
import os
import shutil
version='0.0.1'
for line in open('setup.py'):
    if 'version' in line:
        version='.'.join(line.split('=')[1].strip().split('.')[:-1]+[str(int(line.split('=')[1].strip().strip(',').strip("'").split('.')[-1])+1)])
        version=version[1:]
content=[(line if not 'version' in line else line.split('=')[0]+' = \''+ version+"',\n")  for line in open('setup.py').readlines()]
open('setup.py','w').writelines(content)

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
# os.system('pip3 uninstall labinstrument')
os.system('pip3 install dist_compiled/labinstrument-{}-py3-none-any.whl'.format(version))


