# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.13.2

#https://stackoverflow.com/questions/41319407/how-do-i-add-a-layout-to-a-qtablewidget-in-pyqt
#https://stackoverflow.com/questions/7782015/how-can-i-select-by-rows-instead-of-individual-cells-in-qtableview-in-pyqt
#https://stackoverflow.com/questions/34258650/how-to-make-columns-and-rows-dynamically-in-pyqt

import sys
import json
import dictionary_building_module as db
import VSM_retrieval_module as vr
import corpus_access_module as ca
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

corpusPath = '../output/storage.json'

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(836, 651)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.scrollArea.setFont(font)
        self.scrollArea.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 814, 604))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 5)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 3, 3, 1, 1)
        self.checkBox_3.stateChanged.connect(self.onCheckBox_Toggled)


        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 3)

        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton_2.clicked.connect(self.onViewDetail_clicked)

        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)

        self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 2, 2, 1, 1)

        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 3, 1, 1)
        self.checkBox_2.stateChanged.connect(self.onCheckBox_Toggled)

        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.onCheckBox_Toggled)

        self.gridLayout.addWidget(self.checkBox, 1, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onSearch_clicked)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Simple Search Engine"))
        self.checkBox_3.setText(_translate("mainWindow", "Normalization"))
        self.label.setText(_translate("mainWindow", "Type of model"))
        self.label_2.setText(_translate("mainWindow", "Type of collection"))
        self.pushButton_2.setText(_translate("mainWindow", "View Detail"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Boolean Retrieval Model"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Vector Space Model"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "UofO catalog"))
        self.checkBox_2.setText(_translate("mainWindow", "Stemming"))
        self.checkBox.setText(_translate("mainWindow", "Stopword "))
        self.pushButton.setText(_translate("mainWindow", "Search"))
    
    def onCheckBox_Toggled(self):
        if self.checkBox.isChecked():
            db.stopWordFlag = True
        else :
            db.stopWordFlag = False

        if self.checkBox_2.isChecked():
            db.wordStemmingFlag = True
        else:
            db.wordStemmingFlag = False

        if self.checkBox_3.isChecked():
            db.normalizationFlag = True
        else:
            db.normalizationFlag = False
        #print("stopWordFlag is %s" %db.stopWordFlag)
        #print("wordStemmingFlag is %s" %db.wordStemmingFlag)
        #print("normalizationFlag is %s" %db.normalizationFlag)
    
    def onSearch_clicked(self):
        model = self.comboBox.currentText()
        collection = self.comboBox_2.currentText()
        query = self.lineEdit.text()
        print("onSearch_clicked, module: "+ model +" collection: "+ collection)

        if query == "":
            msg = QMessageBox()
            msg.setWindowTitle("warning!")
            msg.setText("Please fill out the search field!")
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            msg.setFont(font)
            
            x = msg.exec_()
        else:
            #self.tableWidget.addItem(query)
            if model == "Vector Space Model":
                self.tableWidget.removeRow(0)
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setHorizontalHeaderLabels(['docId', 'title', 'desc', 'score'])
                result = vr.comput_score(query)
                print(result)
                for i in result:
                    currentRowCount = self.tableWidget.rowCount()
                    doc = ca.getDocs([i[0]])
                    #print(doc)
                    self.tableWidget.insertRow(currentRowCount)
                    self.tableWidget.setItem(currentRowCount,0,QTableWidgetItem(str(doc[0]['link'])))
                    self.tableWidget.setItem(currentRowCount,1,QTableWidgetItem(doc[0]['title']))
                    self.tableWidget.setItem(currentRowCount,2,QTableWidgetItem(doc[0]['desc']))
                    self.tableWidget.setItem(currentRowCount,3,QTableWidgetItem(str(i[1])))
            elif model == "Boolean Retrieval Model":
                print("Boolean Retrieval Model")

    
    def onViewDetail_clicked(self):
        with open(corpusPath, 'r') as file:
            f = json.load(file)
            print("onViewDetail_clicked")
            id = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
            for i in f:
                #print(i)
                if i["docId"] == int(id):
                    title = i["title"]
                    desc = i["desc"]
                    info = QMessageBox()
                    info.setWindowTitle(title)
                    info.setText(desc)
                    font = QtGui.QFont()
                    font.setFamily("Times New Roman")
                    font.setPointSize(10)
                    info.setFont(font)
            
                    y = info.exec_()


    
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(w)
    #print("corpus preprocessing...")
    #db.pre_dictionary_building()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
