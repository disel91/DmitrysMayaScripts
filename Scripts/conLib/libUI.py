import pprint

from maya import cmds

import controllerLib
reload (controllerLib)

from PySide2 import QtWidgets, QtCore, QtGui

class ControllerLibraryUI(QtWidgets.QDialog):

    """
    The Controller Library UI allows us to import and save controllers
    """

    def __init__(self):
        super(ControllerLibraryUI, self).__init__()

        self.setWindowTitle('Controller Library UI')


        #Library variable points to an instance of our controller library
        self.library = controllerLib.ControllerLibrary()


        #Every new instance automatically build and populates the UI
        self.buildUI()
        self.populate()

    def buildUI(self):

        #Master Layout
        layout = QtWidgets.QVBoxLayout(self)

        #Child horizontal widget
        saveWidget = QtWidgets.QWidget()
        saveLayout = QtWidgets.QHBoxLayout(saveWidget)
        layout.addWidget(saveWidget)

        self.saveNameField = QtWidgets.QLineEdit()
        saveLayout.addWidget(self.saveNameField)

        saveBtn = QtWidgets.QPushButton('Save')
        saveBtn.clicked.connect(self.save)
        saveLayout.addWidget(saveBtn)


        #These are the thumbnail param
        size = 80
        buffer = 12

        #This creates the grid for thumbnails
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setViewMode(QtWidgets.QListWidget.IconMode)
        self.listWidget.setIconSize(QtCore.QSize(size,size))
        self.listWidget.setResizeMode(QtWidgets.QListWidget.Adjust)
        self.listWidget.setGridSize(QtCore.QSize(size+buffer, size+buffer))
        layout.addWidget(self.listWidget)

        #This holds the buttons
        btnWidget = QtWidgets.QWidget()
        btnLayout = QtWidgets.QHBoxLayout(btnWidget)
        layout.addWidget(btnWidget)

        importBtn = QtWidgets.QPushButton('Import')
        importBtn.clicked.connect(self.load)
        btnLayout.addWidget(importBtn)

        refreshBtn = QtWidgets.QPushButton('Refresh')
        refreshBtn.clicked.connect(self.populate)
        btnLayout.addWidget(refreshBtn)

        closeBtn = QtWidgets.QPushButton('Close')
        closeBtn.clicked.connect(self.close)
        btnLayout.addWidget(closeBtn)



    def populate(self):

        #Clears and populates the library
        self.listWidget.clear()
        self.library.find()

        for name, info in self.library.items():
            item = QtWidgets.QListWidgetItem(name)
            self.listWidget.addItem(item)

            screenshot = info.get('screenshot')
            if screenshot:
                icon = QtGui.QIcon(screenshot)
                item.setIcon(icon)

            item.setToolTip(pprint.pformat(info))

    def load(self, *args):

        #Loads the object
        currentItem = self.listWidget.currentItem()

        if not currentItem:
            return

        name = currentItem.text()
        self.library.load(name)

    def save(self):

        #Saves the new object and name
        name = self.saveNameField.text()
        if not name.strip():
            cmds.warning("You must name the object!")
            return

        self.library.save(name)
        self.populate()
        self.saveNameField.setText('')

def showUI():
    ui = ControllerLibraryUI()
    ui.show()
    return ui
