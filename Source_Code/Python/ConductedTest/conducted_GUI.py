import json
import sys
import os
from .untitled import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets

class MainUI(Ui_Dialog,QtWidgets.QWidget):

    def __init__(self,*args,**kwargs):
        super(MainUI,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.manual_connect()
        self.load_cases()

    def manual_connect(self):
        self.button_browse.clicked.connect(self.on_browse)
        self.list_case.mouseDoubleClickEvent=self.on_select
        self.list_to_run.mouseDoubleClickEvent=self.on_clear
        self.pushButton.clicked.connect(self.on_select)
        self.button_run.clicked.connect(self.on_run)
        self.button_save.clicked.connect(self.on_save)


    def load_cases(self):
        print('load_cases')
        for x in json.load(open(os.path.join(os.path.dirname(__file__),'config.txt'))):
            self.list_case.addItem(QtWidgets.QListWidgetItem(x))



    def on_select(self,event=None):
        print('on select')
        if event:
            print(event)

    def on_save(self):
        print('on save')

    def on_run(self):
        print('on run')

    def on_clear(self,event=None):
        print('on clear')

    def on_delete(self):
        print('on delete')

    def on_browse(self):
        print('on browse')
        content=QtWidgets.QFileDialog().getExistingDirectory(None,"Select the path",os.path.dirname(__file__))
        if type(content) is str:
            self.line_path.setText(content)

def exec():
    app = QtWidgets.QApplication(sys.argv)
    main = MainUI()
    main.show()
    app.exec()