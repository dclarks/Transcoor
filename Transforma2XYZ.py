

# Form implementation generated from reading ui file 'Transforma2XYZ.ui'
#
# Created: Sun May 24 13:45:10 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys
import math
import numpy as np
coordenadas_para_tabela = []
numero_col = 0
numero_lin = 0
latitude_dec = []
longitude_dec = []
altitude =[]
coordenadas_tridimensionais = []

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1163, 527)
        self.gridFrame = QtGui.QFrame(Form)
        self.gridFrame.setGeometry(QtCore.QRect(30, 20, 681, 371))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtGui.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtGui.QTableWidget(self.gridFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.botaoAbrir = QtGui.QPushButton(Form)
        self.botaoAbrir.setGeometry(QtCore.QRect(110, 420, 94, 23))
        self.botaoAbrir.setObjectName("botaoAbrir")
        self.tableWidget_2 = QtGui.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(730, 20, 381, 371))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.botaoCalcular = QtGui.QPushButton(Form)
        self.botaoCalcular.setGeometry(QtCore.QRect(230, 420, 94, 23))
        self.botaoCalcular.setObjectName("botaoCalcular")
        # adicionado
        self.botaoNovo = QtGui.QPushButton(Form)
        self.botaoNovo.setGeometry(QtCore.QRect(110, 445, 94, 23))
        self.botaoNovo.setObjectName("botaoNovo")
        # adicionado
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(530, 440, 151, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 470, 151, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(410, 440, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(410, 470, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 410, 241, 16))
        self.label_3.setObjectName("label_3")
        self.botaoSalvar = QtGui.QPushButton(Form)
        self.botaoSalvar.setGeometry(QtCore.QRect(960, 430, 94, 23))
        self.botaoSalvar.setObjectName("botaoSalvar")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 500, 371, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.botaoAbrir, QtCore.SIGNAL("clicked()"), self.abrir_arquivo)
        QtCore.QObject.connect(self.botaoCalcular, QtCore.SIGNAL("clicked()"), self.calcular)
        QtCore.QObject.connect(self.botaoSalvar, QtCore.SIGNAL("clicked()"), self.saveFile)
        QtCore.QObject.connect(self.botaoNovo, QtCore.SIGNAL("clicked()"), self.Novo)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.botaoAbrir, self.botaoCalcular)
        Form.setTabOrder(self.botaoCalcular, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.tableWidget)
        Form.setTabOrder(self.tableWidget, self.tableWidget_2)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Programa para transformar LAT LON ALT em X Y Z", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Latitude", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Longitude", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Altitude Elip.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Form", "sigma Lat", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Form", "sigma Lon", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Form", "sigma Alt", None, QtGui.QApplication.UnicodeUTF8))
        self.botaoAbrir.setText(QtGui.QApplication.translate("Form", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.botaoCalcular.setText(QtGui.QApplication.translate("Form", "Calcular", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Form", "6378137.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("Form", "298.257222101 ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Semieixo maior:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Achatamento: 1/", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "PADRAO SIRGAS2000,4", None, QtGui.QApplication.UnicodeUTF8))
        self.botaoSalvar.setText(QtGui.QApplication.translate("Form", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        # adicionado
        self.botaoNovo.setText(QtGui.QApplication.translate("Form", "Novo", None, QtGui.QApplication.UnicodeUTF8))
        # adicionado
        self.label_4.setText(QtGui.QApplication.translate("Form", "Programa desenvolvido por Thiago Igarashi", None, QtGui.QApplication.UnicodeUTF8))

    def abrir_arquivo(self):
            
            # Nao tem parent=None, QFileDialog nao e instancia de Ui_Form
            filename = QtGui.QFileDialog.getOpenFileName(None, 'Open File','Abrir Arquivo GG.MMSSSSSS','Text File *.txt (*.txt)')
            # print filename
            filename = filename[0]
            # print "valor da tupla"
            # print filename
            global coordenadas_para_tabela
            global numero_lin
            global numero_col

            #nome = "(u'/home/thiago/scripts/python/teste.txt', u'Text File *.txt (*.txt)')"
            #separado = nome.split('u')
            #print separado
            #print nome
            
            # texto = open('/home/thiago/UFPR.02/Mestrado/Geodesia Geral/Programa/coordenadas_SAD69-96.txt').read()
            # coordenadas_para_tabela = texto
            #print "coordenadas para a tabela print open"
            with open(filename,'r') as input:
                for line in input:
                    coordenadas_para_tabela.append(line.strip().split(' '))
          
            print coordenadas_para_tabela
            # Conta as linhas dos dados de entrda
            # Conta as colunas na linha
            self.tableWidget.setRowCount(len(coordenadas_para_tabela))
            self.tableWidget.setColumnCount(len(coordenadas_para_tabela[0]))
            numero_lin = len(coordenadas_para_tabela)
            numero_col = len(coordenadas_para_tabela[0])

            for i, row in enumerate(coordenadas_para_tabela):
                for j, col in enumerate(row):
                    item = QtGui.QTableWidgetItem(col)
                    self.tableWidget.setItem(i, j, item)

    def Novo(self):
        global coordenadas_para_tabela
        # colunas = self.tableWidget.clear()
        # print colunas


        # Seta o tamanho da tabela
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        # Cria as colunas
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        # Adiciona os nomes
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Latitude", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Longitude", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Altitude Elip.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Form", "sigma Lat", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Form", "sigma Lon", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Form", "sigma Alt", None, QtGui.QApplication.UnicodeUTF8))

        coordenadas_para_tabela = []


    def calcular(self):
        global coordenadas_para_tabela
        global latitude_dec
        global longitude_dec
        global altitude
        global coordenadas_tridimensionais
        # N = []
        # M = []
        # X = []
        # Y = []
        # Z = []
        # N = np.array(N)
        # M = np.array(M)
        # X = np.array(X)
        # Y = np.array(Y)
        # Z = np.array(Z)


        matriz = [[11,22,322],[43,52,61],[71,81,91]]
        # a matriz dos dados passara a se chamar m
        m = np.array(coordenadas_para_tabela)
        # Passa m para float, estava dando erro nas altitude, estava com '787.78','746.12'.....
        m = m.astype(np.float)
        latitude_sex = m[:,0]   # copia todas as latitudes
        longitude_sex = m[:,1]  # copia todas as longitudes
        altitude = m[:,2]       # copia todas as altitudes

        print type(latitude_sex)
        print type(longitude_sex)
        print type(altitude)

        # RECEBE OS VALORES DOS EDIT_TEXT DO PYSIDE
        # semieixo_maior = float(str(self.lineEdit.displayText()))   
        # achatamento = float(str(self.lineEdit_2.displayText()))
        print self.lineEdit.text()
        print self.lineEdit_2.text()
        achatamento_origem = 1/float((self.lineEdit_2.text()))
        semieixo_maior_origem = float(self.lineEdit.text())
        # primeira excentricidade ao quadrado
        e = (2*achatamento_origem) - math.pow(achatamento_origem,2)
        #% segunda excentricidade ao quadrado
        e2 = (e/(1-e))
        print "excentricidade = " , e
        print "excentricidade ao quadrado = " , e2

        tam = len(latitude_sex)
        n = []
        m = []
        x1 = []
        y1 = []
        z1 = []

        i = 0
        for i in range(tam):
            
            #Passa para decimal
            decimallatitude = self.sex2dec(latitude_sex[i])
            decimallongitude = self.sex2dec(longitude_sex[i])
            # Tem que usar append porque latitude_dec[0] nao existe
            latitude_dec.append(decimallatitude) 
            longitude_dec.append(decimallongitude)
            latitude_radiano = latitude_dec[i] * math.pi / 180
            longitude_radiano = longitude_dec[i] * math.pi / 180
            # Calcula N M
            n.append( semieixo_maior_origem / math.sqrt((1 - e * math.pow(math.sin(latitude_radiano),2) )))
            m.append( n[i] / (1 + e *  math.pow( math.cos(latitude_radiano),2)  ) )
            # print n
            # print type(altitude)
            # print type(n)
            # print type(latitude_radiano)
            # print type(longitude_radiano)
            # print (altitude)
            # print (n)
            # print (latitude_radiano)
            # print (longitude_radiano)

            x1.append( (n[i] + altitude[i]) * math.cos(latitude_radiano) * math.cos(longitude_radiano) ) 
            y1.append( (n[i] + altitude[i]) * math.cos(latitude_radiano) * math.sin(longitude_radiano) )   
            z1.append( (n[i] * (1-e) + altitude[i]) * math.sin(latitude_radiano))

        # print x1
        # print y1
        # print z1
        # print type(x1)
        # print type(y1)
        # print type(z1)
        coordenadas_para_tabela2 = []
        # x1 = zip(x1)
        # y1 = zip(y1)
        # z1 = zip(z1)
        ''' Tem que dar um reshape nesta bosta, porque quando der x1.shape --> (10,) nao entende o numero del inhas e colunas
        dando um reshape -->> printando x1.shape:  (1, 10) da certo'''
        x1 = np.array(x1)
        t = len(x1)
        x1 = x1.reshape(1,t)
        y1 = np.array(y1)
        y1 = y1.reshape(1,t)
        z1 = np.array(z1)
        z1 = z1.reshape(1,t)
        #print "printando x1: ", x1
        #print "printando x1.shape: ", x1.shape
        #x1 = x1[:,None]
        #y1 = y1[:,None]
        #z1 = z1[:,None]

        coordenadas_tridimensionais = np.concatenate((x1,y1,z1))
        #coordenadas_tridimensionais = coordenadas_tridimensionais.transpose()
        #print "tamanho agora eh de: ",coordenadas_tridimensionais.shape

        #coordenadas_tridimensionais = np.concatenate((x1,y1,z1))
        coordenadas_tridimensionais = coordenadas_tridimensionais.transpose()
        #print "tamanho da matriz: " , coordenadas_tridimensionais.shape
        coordenadas_tridimensionais = coordenadas_tridimensionais.tolist()
        #print coordenadas_tridimensionais
        # coordenadas_para_tabela2 = x1 + y1 + z1
        coordenadas_para_tabela2 = coordenadas_tridimensionais
        #print coordenadas_para_tabela2
        # coordenadas_para_tabela2.tolist()
        #coordenadas_para_tabela2.shape
        lin = len(coordenadas_para_tabela2)
        #print lin
        col = len(coordenadas_para_tabela2[0])
        #print col

        self.tableWidget_2.setRowCount(lin)
        self.tableWidget_2.setColumnCount(col)

        for i, row in enumerate(coordenadas_tridimensionais):
            for j, col in enumerate(row):
                item = QtGui.QTableWidgetItem(str(col))
                self.tableWidget_2.setItem(i, j, item) 
 


    def saveFile(self):
        global coordenadas_tridimensionais   
        print coordenadas_tridimensionais

        filename = QtGui.QFileDialog.getSaveFileName(None, 'Save File', '.xyz')
        # filename e/ tupla, tem que pegar a primeira parte que contem o caminho do arquivo.
        print filename[0]
        filename = filename[0]

        #separado = nome.split('u')
        k = open(filename,'w')
        arquivo = (coordenadas_tridimensionais)
        print arquivo
        arquivo = np.array(arquivo)
        arquivo.shape
        np.savetxt(k, arquivo)        
        # print type(coordenadas_tridimensionais)
        # for item in arquivo:
            
        #     s = ",".join(item).replace(","," ")
        #     k.write(s)
        #     # k.write('\n')


    def sex2dec(self,angulo):
            angulo = float(angulo)
            resto, inteiro = math.modf(angulo)
            grau = inteiro
            minuto_g = resto * 100
            resto, inteiro = math.modf(minuto_g)
            minuto = inteiro / 60
            segundos_g = resto * 100
            segundos = segundos_g / 3600

            grau_decimal = grau + minuto + segundos
            return grau_decimal


    def mostra_por_linhas_conteudo(matriz):
        # Indexaca pelo conteudo.
        for linha in matriz:
            for coluna in linha:
                print coluna

    def mostra_por_linhas_posicao(matriz):
        #Indexacao pela posicao.
        for pos_linha in range(len(matriz)):
            for pos_coluna in range(len(matriz[0])):
                print matriz[pos_linha][pos_coluna]


    # TEM QUE ADICIONAR AS LINHAS ABAIXO AT O IF PARA QUE A JANELA SEJA EXECUTADA
    # SE NAO ADICIONAR, VAI EXECUTAR E NAO VAI ACONTECER NADA, A JANELA NAO SERA MOSTRADA
class ControlMainWindow(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        metodo = Ui_Form()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
        
