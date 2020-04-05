# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.13.2

#https://stackoverflow.com/questions/41319407/how-do-i-add-a-layout-to-a-qtablewidget-in-pyqt
#https://stackoverflow.com/questions/7782015/how-can-i-select-by-rows-instead-of-individual-cells-in-qtableview-in-pyqt
#https://stackoverflow.com/questions/34258650/how-to-make-columns-and-rows-dynamically-in-pyqt
#https://stackoverflow.com/questions/36772927/pyqt-how-to-pass-information-between-windows
#https://stackoverflow.com/questions/58735786/pyqt5-qtableview-how-to-find-out-if-row-is-selected-and-which-one
#https://stackoverflow.com/questions/37222081/pyqt-qtableview-set-horizontal-vertical-header-labels
#https://stackoverflow.com/questions/40995778/resize-column-width-to-fit-into-the-qtablewidget-pyqt
#https://stackoverflow.com/questions/34374660/how-can-i-get-the-selected-rows-value-of-a-qtablewidget-in-pyqt

import sys
import json
import os
import dictionary_building_module as db
import inverted_index_construction_module as iic
import VSM_retrieval_module as vr
import corpus_access_module as ca
import spelling_correction_module as sc
import boolean_retrieval_model_module as br
import query_expansion_module as qe
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

reBuildFlag = False
stopWordFlag = True
wordStemmingFlag = True
normalizationFlag = True

corpusPath = '../output/storage.json'
indexPath = '../output/index.json'
weightedIndexPath = '../output/weightedindex.json'


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
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 3)

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

        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLocale(QtCore.QLocale(QtCore.QLocale.Armenian, QtCore.QLocale.Armenia))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.onExpansion_clicked)
        self.gridLayout.addWidget(self.pushButton_3, 0, 4, 1, 1)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
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
        self.comboBox_2.setItemText(1, _translate("mainWindow", "Reuters21578"))
        self.checkBox_2.setText(_translate("mainWindow", "Stemming"))
        self.checkBox.setText(_translate("mainWindow", "Stopword "))
        self.pushButton.setText(_translate("mainWindow", "Search"))
        self.pushButton_3.setText(_translate("mainWindow", "Query Expansion"))
        
    #change the rebuild flag when setting is toggled
    def onCheckBox_Toggled(self):
        global reBuildFlag
        global stopWordFlag
        global wordStemmingFlag
        global normalizationFlag
        reBuildFlag = True
        if self.checkBox.isChecked():
            stopWordFlag = True
        else :
            stopWordFlag = False

        if self.checkBox_2.isChecked():
            wordStemmingFlag = True
        else:
            wordStemmingFlag = False

        if self.checkBox_3.isChecked():
            normalizationFlag = True
        else:
            normalizationFlag = False
        print("reBuildFlag is %s" %reBuildFlag)
    
    def onSearch_clicked(self):
        
        model = self.comboBox.currentText()
        collection = self.comboBox_2.currentText()
        query = self.lineEdit.text()
        print("onSearch_clicked, module: "+ model +" collection: "+ collection)
        self.tableWidget.setRowCount(0)

        #reBuild index if the setting is changed
        if reBuildFlag == True:
            rebuild()
        
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
            if model == "Vector Space Model":
                print("Vector Space Model")
                terms = vr.extractQueryTerms(query)
                #check weather the imput query is in the index.
                w = sc.check(terms,collection)
                
                if w != []:
                    #ask user to pick a different query 
                    correction = sc.getCorrection(w,collection)
                    for i in correction.items():
                        c = get_correction(i)
                        if c != None:
                            if c[1] != None:
                                terms = [w.replace(c[0],c[1]) for w in terms]
                            else:
                                for i in terms:
                                    if i == c[0]:
                                        terms.remove(i)
                        #print(terms)
                #set up table
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setHorizontalHeaderLabels(['docId', 'title', 'desc', 'score'])
                terms = db.wordStemming(terms)# word stemming after spelling correction
                result = vr.comput_score(terms,collection)
                if result != None:
                    for i in result:
                        currentRowCount = self.tableWidget.rowCount()
                        doc = ca.getDocs([i[0]])
                        #print(doc)
                        if 'link' in doc[0] and 'title' in doc[0] and 'desc' in doc[0]:
                            self.tableWidget.insertRow(currentRowCount)
                            self.tableWidget.setItem(currentRowCount,0,QTableWidgetItem(str(doc[0]['link'])))
                            self.tableWidget.setItem(currentRowCount,1,QTableWidgetItem(doc[0]['title']))
                            self.tableWidget.setItem(currentRowCount,2,QTableWidgetItem(doc[0]['desc']))
                            self.tableWidget.setItem(currentRowCount,3,QTableWidgetItem(str(i[1])))
                        else:
                            print(doc[0])
                else:
                    self.tableWidget.setRowCount(0)
                    print("can not find the term " +query+" from the collection")
            elif model == "Boolean Retrieval Model":
                print("Boolean Retrieval Model")
                result = br.demo_processWithIndex(query, [], json.load(open(br.iic.indexPath, 'r')))
                if result != []:
                    #set up table
                    print(result)
                    self.tableWidget.setRowCount(0)
                    self.tableWidget.setColumnCount(3)
                    self.tableWidget.setHorizontalHeaderLabels(['docId', 'title', 'desc'])
                    doc = ca.getDocs(result)
                    for i in doc:
                        currentRowCount = self.tableWidget.rowCount()
                        #print(doc)
                        if 'link' in i and 'title' in i and 'desc' in i:
                            self.tableWidget.insertRow(currentRowCount)
                            self.tableWidget.setItem(currentRowCount,0,QTableWidgetItem(str(i['link'])))
                            self.tableWidget.setItem(currentRowCount,1,QTableWidgetItem(i['title']))
                            self.tableWidget.setItem(currentRowCount,2,QTableWidgetItem(i['desc']))
                        else:
                            print(i)
                else:
                    self.tableWidget.setRowCount(0)
                    print("can not find the term " +query+" from the collection")

    
    def onViewDetail_clicked(self):
        
        if self.tableWidget.rowCount() == 0:
            print("table is empty")
        elif not self.tableWidget.selectionModel().selectedRows():
            print("not selected")
        else:
            with open(corpusPath, 'r') as file:
                f = json.load(file)
                print("onViewDetail_clicked")
                
                id = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
                if id is  None:
                    print("empty table")
                
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


    def onExpansion_clicked(self):
        query = self.lineEdit.text()
        model = self.comboBox.currentText()
        collection = self.comboBox_2.currentText()
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
            exp = qe.expansion(query, model, collection)
            print(exp)
            if exp != {}:
                explist = []
                for i in exp:
                    q = exp[i]
                    qe_msg = expMessageBox([i,q])
                    currentClick = qe_msg.exec_()
                    word = None
                    if currentClick == 0 :
                        print ('Accepted')
                        if qe_msg.tableWidget3.rowCount() == 0:
                            print("Expansion table is empty")
                            word = [i,None]
                        elif not qe_msg.tableWidget3.selectionModel().selectedRows():
                            print("Expansion not selected")
                            word = [i,None]
                        else:
                            templist = []
                            rows=[idx.row() for idx in qe_msg.tableWidget3.selectionModel().selectedRows()]
                            for r in rows:
                                templist.append(qe_msg.tableWidget3.item(r,0).text())
                            word = [i,templist]
                    else:
                        word = [i,None]
                    explist.append(word)
                print(explist)
                newquery = ''
                if model == "Vector Space Model":
                    tempquery = query.split()
                    for e in explist:
                        if e[1] != None:
                            s= ' '.join(str(s) for s in e[1])+" "+str(e[0])
                            tempquery[:] = [s if x==e[0] else x for x in tempquery]
                        else:
                            print("no expansion for "+e[0])
                    newquery = ' '.join(str(s) for s in tempquery)
                else:
                    tempquery = query.split()
                    for e in explist:
                        if e[1] != None:
                            s = '( '+' OR '.join(str(s) for s in e[1])+" OR "+str(e[0])+' )'
                            tempquery[:] = [s if x==e[0] else x for x in tempquery]
                            print(s)
                            print(tempquery)
                        else:
                            print("no expansion for "+e[0])
                    newquery = ' '.join(str(s) for s in tempquery)
                self.lineEdit.setText(newquery)

            else:
                print("can not find expansion")

class expMessageBox(QtWidgets.QMessageBox):
    def __init__(self,lis):
        QtWidgets.QMessageBox.__init__(self)
        self.setSizeGripEnabled (True)
        self.setWindowTitle('Query Expansion')
        self.setText("Please select words below to expansion: "+lis[0]+
                     "\n Or press cancel. holding ctrl to select multiple items")
        self.addButton (
            QtWidgets.QPushButton('Accept'), 
            QtWidgets.QMessageBox.YesRole
        )
        self.addButton(
            QtWidgets.QPushButton('Cancel'), 
            QtWidgets.QMessageBox.RejectRole
        )
        self.addTableWidget (self,lis)
    def addTableWidget (self, parentItem,lis) :
        self.l =  QtWidgets.QVBoxLayout()
        self.tableWidget3 = QtWidgets.QTableWidget(parentItem)
        self.tableWidget3.setObjectName ('expansion_tableWidget')

        self.tableWidget3.move(100,130)
        self.tableWidget3.resize(200, 200)
        self.l.addWidget(self.tableWidget3)
        self.setLayout(self.l)
        self.tableWidget3.setColumnCount(1)
        self.tableWidget3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget3.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        for c in lis[1]:
            RowCount = self.tableWidget3.rowCount()
            self.tableWidget3.insertRow(RowCount)
            self.tableWidget3.setItem(RowCount,0,QTableWidgetItem(c))

        
    def event(self, e):
        result = QtWidgets.QMessageBox.event(self, e)
        self.setMinimumWidth(0)
        self.setMaximumWidth(16777215)
        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Expanding
        )
        self.resize(400, 400)

        return result


#message popup box with spelling correction table
class MyMessageBox(QtWidgets.QMessageBox):
    #get_word = QtCore.pyqtSignal(dict)
    def __init__(self,lis):
        QtWidgets.QMessageBox.__init__(self)
        
        self.setSizeGripEnabled (True)
        self.setWindowTitle('Spelling Correction')
        self.setText("Please select one of the word below to replace: "+lis[0]+
                     " Or press cancel to remove "+lis[0]+" from search query")
        
        self.addButton (
            QtWidgets.QPushButton('Accept'), 
            QtWidgets.QMessageBox.YesRole
        )
        self.addButton(
            QtWidgets.QPushButton('Cancel'), 
            QtWidgets.QMessageBox.RejectRole
        )

        self.addTableWidget (self,lis)
    def addTableWidget (self, parentItem,lis) :
        self.l =  QtWidgets.QVBoxLayout()
        self.tableWidget2 = QtWidgets.QTableWidget(parentItem)
        self.tableWidget2.setObjectName ('spelling_tableWidget')

        self.tableWidget2.move(100,130)
        self.tableWidget2.resize(200, 200)
        self.l.addWidget(self.tableWidget2)
        self.setLayout(self.l)
        self.tableWidget2.setColumnCount(1)
        self.tableWidget2.horizontalHeader().setStretchLastSection(True)
        for c in lis[1]:
            RowCount = self.tableWidget2.rowCount()
            self.tableWidget2.insertRow(RowCount)
            self.tableWidget2.setItem(RowCount,0,QTableWidgetItem(c[0]))

        
    def event(self, e):
        result = QtWidgets.QMessageBox.event(self, e)
        self.setMinimumWidth(0)
        self.setMaximumWidth(16777215)
        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Expanding
        )
        self.resize(400, 400)

        return result   

def get_correction(correction):
    #create a popup messagebox with option for user to pick desired query
    sc_msg = MyMessageBox(correction)
    currentClick = sc_msg.exec_()
    word = None
    if currentClick == 0 :
        print ('Accepted')
        if sc_msg.tableWidget2.rowCount() == 0:
            print("M table is empty")
            word = [correction[0],None]
        elif not sc_msg.tableWidget2.selectionModel().selectedRows():
            print("M not selected")
            word = [correction[0],None]
        else:
            word = [correction[0],sc_msg.tableWidget2.item(sc_msg.tableWidget2.currentRow(),0).text()]
    else:
        word = [correction[0],None]
    return word

#rebuild the index and reset the Flag
def rebuild():
    global reBuildFlag
    print("building index this may take a few seconds....")
    
    if stopWordFlag != db.stopWordFlag or wordStemmingFlag != db.wordStemmingFlag or normalizationFlag != db.normalizationFlag:
        db.toggleStopWordFlag(stopWordFlag)
        db.toggleWordStemmingFlag(wordStemmingFlag)
        db.toggleNormalizationFlag(normalizationFlag)
        vr.wc.getinvertedindex()
        vr.gettf_idf()
    
    reBuildFlag = False
    print("done....")

## setting of the stopword removal, stemming, normalization is on by defult
def main():
    #setup corpus, index, terms, and weighted index when open up search engine
    #print("corpus preprocessing....")
    #db.pre_dictionary_building()
    #print("creating inverted index....")
    #vr.wc.getinvertedindex()
    #print("creating weighted index....")
    #vr.gettf_idf()
    # if not os.path.exists(corpusPath):
    #     db.pre_dictionary_building()
    # if not os.path.exists(indexPath):
    #     iic.getinvertedindex()
    # if not os.path.exists(weightedIndexPath):
    #     vr.gettf_idf()
        
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
