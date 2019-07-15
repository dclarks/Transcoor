#--coding: utf-8 --
try:
    from PySide import QtGui, QtCore
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    from PySide2 import QtGui, QtCore, QtWidgets
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *



#from osgeo import osr
#from time import gmtime, strftime
#import calendar
#import datetime



''' 
    strftime("%Y-%m-%d %H:%M:%S", gmtime()) 
    '2009-01-05 22:14:39'
'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

'''  UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 21: ordinal not in range(128) 
    Para resolver isso deve-se usar o reload(sys) e sys.setdefaultencoding('utf8') 
'''




''' PYTHON USA __init__.py PARA DIZER QUE UM DIRETORIO É DE MODULO
AQUI USEI PARA A PASTA MODULOS
CASO NAO TENHA O ARQUIVO __init__.py COLCOAR: sys.path.insert(0, './modulos')
import interfaceGrafica


'''
import os
from modulos import interfaceGrafica
#from modulos import topografia
from modulos import ferramentas
from modulos import my_functions
from modulos import dxf
import math
import time
import ezdxf
import serial.tools.list_ports



'''
Mudar vim /etc/matplotlibrc
backend.qt4 : PySide
Para funcionar o matplotlib no Pyside
'''


import matplotlib
matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt



epsg_to_name = 0  # armazena codigo e nome do combobox
epsg_from_name = 0  # armazena codigo e nome do combobox
epsg_to = 0  # armazena apenas o numero
epsg_from = 0  # armazena apenas o numero
nomedoarquivo = None

global enderecocad
global endereco2dxfpontos

class JanelaPrincipal(QDialog, interfaceGrafica.Ui_Form):
    def __init__(self, parent=None):
        super(JanelaPrincipal, self).__init__(parent)
        self.setupUi(self)  # puxa do interfaceGrafica esse metodo setupUi

        #self.pushButtonPontotoDXFReordenar.clicked.connect(self.reordenarTabela)

        self.pushButton.clicked.connect(self.removeEPSGname)
        self.calculaButton.clicked.connect(self.calculaGdal)
        self.invertButton.clicked.connect(self.invertPosition)
        #self.connect(self.pushButton_openstation, SIGNAL("clicked()"), self.abrir_arquivoEstacao)
        self.pushButton_openstation.clicked.connect(self.abrir_arquivoEstacao)
        #self.connect(self.pushButton_Recalcula, SIGNAL("clicked()"), self.recalcular)
        self.pushButton_Recalcula.clicked.connect(self.recalcular)
        self.pushButton_RecalculaPor2pontos.clicked.connect(self.recalcularPoligonalporDoisPontos)

        self.tableWidget_dadosBrutos.cellClicked.connect(self.cell_was_clicked)
        #self.connect(self.pushButton_salvarCoordenadas, SIGNAL("clicked()"),self.salva_coordenadas)
        self.pushButton_salvarCoordenadas.clicked.connect(self.salva_coordenadas)
        #self.connect(self.pushButton_plota_pontos, SIGNAL("clicked()"),self.plota_pontos2D)
        self.pushButton_plota_pontos.clicked.connect(self.plota_pontos2D)
        #self.connect(self.pushButton_exportar_dxf, SIGNAL("clicked()"),self.exporta_dxf)
        self.pushButton_exportar_dxf.clicked.connect(self.exporta_dxf)

        self.pushButton_Virgual_Ponto_Change.clicked.connect(self.botaoTrocaVirgulaPonto)


        self.lineEdit_bits_por_segundo.setText("9600")
        self.lineEdit_tamanho_do_dado.setText("8")
        self.lineEdit_paridade.setText("Nenhum")
        self.lineEdit_bits_de_parada.setText("1")
        #self.connect(self.pushButton_localizaPorta, SIGNAL("clicked()"),self.procuraPorta)
        self.pushButton_localizaPorta.clicked.connect(self.procuraPorta)
        #self.connect(self.pushButton_3, SIGNAL("clicked()"),self.botaoTeste)
        self.radioButton2D.setChecked(True)
        self.radioButtonTopografica.setChecked(True)
        #self.pushButton_3.clicked.connect(self.botaoTeste)
        self.pushButton_pontos2dxf.clicked.connect(self.botaoAbrirpontoscsv)
        self.radioButtonpontotodxf2d.setChecked(True)
        self.pushButton_salvaPontos2dxf.clicked.connect(self.gravapontosdxfcsv)
        self.pushButtonPontotoDXFReordenar.clicked.connect(self.reordenarTabela)

    def removeEPSGname(self):
        global epsg_to_name, epsg_from_name, epsg_to, epsg_from
        epsgfrom = self.comboEPSG_from.currentText()
        epsgto = self.comboEPSG_to.currentText()

        epsg_from_name = str(epsgfrom).split()  # split cria lista
        epsg_from = int(float(epsg_from_name[0]))
        epsg_to_name = str(epsgto).split()  # split cria lista
        epsg_to = int(float(epsg_to_name[0]))

        #print epsg_from, epsg_to

    def showMessage(self):
        print self.comboEPSG_from.currentText()
        src = osr.SpatialReference()
        tgt = osr.SpatialReference()
        src.ImportFromEPSG(31983)
        tgt.ImportFromEPSG(4674)

        transform = osr.CoordinateTransformation(src, tgt)
        coords = transform.TransformPoint(580210.101, 7787362.590)
        x, y = coords[0:2]
        print x, y

    def calculaGdal(self):
        global epsg_to, epsg_from
        self.removeEPSGname()
        src = osr.SpatialReference()
        tgt = osr.SpatialReference()
        src.ImportFromEPSG(epsg_from)
        tgt.ImportFromEPSG(epsg_to)
        transform = osr.CoordinateTransformation(src, tgt)
        X = float((self.lineX.text()))
        Y = float((self.lineY.text()))

        coords = transform.TransformPoint(X,Y)
        x, y = coords[0:2]
        a = [str(x),str(y)]
        ", ".join(a)
        self.lineResult.setText(", ".join((a)))
        #print x, y

    def invertPosition(self):

        a = self.lineResult.text()
        a = a.replace(",", "")
        #"".join(a)
        aux = a.split()

        b = (aux[0])
        c = (aux[1])
        d = [c,b]

        self.lineResult.setText("")
        self.lineResult.setText(", ".join(d))

    def PositionLast (self, x,s): #Encontra posicao da ultima ocorrencia de um char
        count = len(s)
        for i in s[::-1]:
            count -= 1
            if i == x:
                return count
        return None

    def abrir_arquivoEstacao(self): # Topografia
        aux = QFileDialog.getOpenFileName(None, 'Open File', 'Abrir Arquivo Bruto', 'Topcon 200 *.M21 ;; Leica *.tcl ;; Todos os Arquivos *.* ')
        global nomedoarquivo
        global enderecocad
        # aux retorna uma lista em unicode
        #print aux
        filename = aux[0]

        self.tableWidget_dadosBrutos.setRowCount(0)
        self.tableWidget_dadosBrutos.setColumnCount(0)


        print filename

        x = "/"
        posicaodaultimaocorrencia = self.PositionLast(x,filename)

        # endereco para salvar o arquivo de cad
        endereco = filename[0:posicaodaultimaocorrencia+1]

        #print endereco



        posicaodaultimaocorrencia = posicaodaultimaocorrencia + 1

        nomedoarquivo = filename[posicaodaultimaocorrencia::]

        ponto = nomedoarquivo.find(".")

        posicaodoultimoponto = self.PositionLast(".",nomedoarquivo)

        nomedoarquivo = nomedoarquivo[0:posicaodoultimoponto]

        nomedoarquivo = nomedoarquivo

        enderecocad = endereco + nomedoarquivo
        #print enderecocad

        self.label_Caminho_Arquivo_M21.setText(filename)


        extensao = aux[1]
        dados_brutos = []
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        # __file__ is the pathname of the file from which the module was loaded, if it was loaded from a file.

        #filename = '/home/thiago/dos/PROGRAMACAO/TRANSCOR/teste/teste.m21';
        #filename = os.path.join(fileDir, 'teste/Q591.M21')
        matriz=[[],[],[],[],[],[],[]]
        est = 0
        irr = 0
        #contagem de linhas
        with open(filename, 'r') as input:
            for line in input:
                if line.strip():
                    if len(line) < 20:
                        est += 1
                    else:
                        irr += 1
        print est, irr
        total_linhas = est + irr

        self.tableWidget_dadosBrutos.setRowCount(total_linhas)
        self.tableWidget_dadosBrutos.setColumnCount(7)
        i = 0
        with open(filename, 'r') as input:
            for line in input:
                if line.strip(): # EXCLUI LINHAS COM APENAS ESPAÇOS

                    #coordenadas_para_tabela.append(line.strip().split(' '))


                    line = my_functions.filtraLinhasM21(line)
                    line = my_functions.filtraLinhasM21Estacao(line)
                    numero_de_arrobas = my_functions.contaArrobas(line)
                    print line

                    #print "140 " ,line

                    if numero_de_arrobas < 4:


                        line = line.split('@')
                        print "ESTACAO ENCONTRADA: " ,line
                        id = line[0]
                        cod = line[1]
                        hi = line[2]

                        # cria um item de tabela para cada string
                        item_pto = QTableWidgetItem(id)
                        self.tableWidget_dadosBrutos.setItem(i, 0, item_pto)
                        item_pto = QTableWidgetItem(cod)
                        self.tableWidget_dadosBrutos.setItem(i, 1, item_pto)
                        item_pto = QTableWidgetItem(hi)
                        self.tableWidget_dadosBrutos.setItem(i, 2, item_pto)

                        i += 1

                    elif not line.strip():
                        i = i - 1
                        print "LINHA DA TABELA VAZIA. NADA A FAZER"
                        #pass

                    else:
                        #print "LINHA DA TABELA: " + str(line) +  "TAMANHO: " + str(len(line))
                        #print "LINHA DA TABELA: ", line.strip()

                        aux = line.split('@')
                        #di

                        di = aux[1]
                        dh = aux[4]
                        hz = aux[3]
                        vt = aux[2]
                        pto = aux[0]
                        tipo = aux[8]

                        di = di[:5] + '.' + di[5:]
                        dh = dh[:5] + '.' + dh[5:]
                        hz = hz[:3] + '.' + hz[3:5] + "'" + hz[5:7] + '"'
                        vt = vt[:3] + '.' + vt[3:5] + "'" + vt[5:7] + '"'
                        hs = aux[9].strip() # remove espacos e newlines

                        matriz[0].append(pto)
                        matriz[1].append(tipo)
                        matriz[2].append(hz)
                        matriz[3].append(vt)
                        matriz[4].append(di)
                        matriz[5].append(dh)
                        matriz[6].append(hs)

                        item_pto = QTableWidgetItem(pto)
                        self.tableWidget_dadosBrutos.setItem(i, 0, item_pto)
                        item_tipo = QTableWidgetItem(tipo)
                        self.tableWidget_dadosBrutos.setItem(i, 1, item_tipo)
                        item_hz = QTableWidgetItem(hz)
                        self.tableWidget_dadosBrutos.setItem(i, 2, item_hz)
                        item_vt = QTableWidgetItem(vt)
                        self.tableWidget_dadosBrutos.setItem(i, 3, item_vt)
                        item_di = QTableWidgetItem(di)
                        self.tableWidget_dadosBrutos.setItem(i, 4, item_di)
                        item_dh = QTableWidgetItem(dh)
                        self.tableWidget_dadosBrutos.setItem(i, 5, item_dh)
                        item_hs = QTableWidgetItem(hs)
                        self.tableWidget_dadosBrutos.setItem(i, 6, item_hs)


                        i += 1

                        #print "Pto %s : %s, di %s, dh %s, hz %s, vt %s, hs %s " % (aux[0],aux[7],di, dh, hz, vt, hs)

    def recalcular(self):
        proximaestacaox = 0
        proximaestacaoy = 0
        proximaestacaoz = 0
        proximaestacaonome = 0
        atualestacaox = 0
        atualestacaoy = 0
        atualestacaoz = 0
        xinicial = 0
        yinicial = 0
        zinicial = 0
        # estacao começa com 1 porque se for 1 e azimute for o hz
        # seu calculo vai ser só somar outros angulos hz para az
        # se azimute for so somar, dai a variavel azimutesosomar passa a ser 1
        # dai verificar com if se estacao =1 e azimutesosomar = 1
        # nos proximos tem que colocar estacao 2 e assim por diante
        estacao = 0
        azimuteinicial = 180
        alturadoinstrumento = 0



        azimute = None

        ''' 
            Procurar se tem PI
            Se tiver procura novamente pelo mesmo ponto e já faz o cálculo PD PI
            Pega indice da linha PI pra apagar ela
            E coloca na tabela o hz me PD
            Pegar xo yo zo da tabela.
            Procurar estacoes
            se achar proxima estacao 
        '''

        # conta as linhas e colunas na tabela de dados brutos para os laços for
        linhas = self.tableWidget_dadosBrutos.rowCount()
        colunas = self.tableWidget_dadosBrutos.columnCount()

        N_estacao = self.lineEditEstacao_N.text()
        E_estacao = self.lineEditEstacao_E.text()
        Z_estacao = self.lineEditEstacao_H.text()

        N_re = self.lineEdit_6.text()
        E_re = self.lineEditRe_E.text()
        Z_re = self.lineEditRe_H.text()


        if not N_re and not E_re and not Z_re:
            #print "dentro"
            #time.sleep(2)
            di_re = self.tableWidget_dadosBrutos.item(1, 4).text();di_re = float(di_re)
            hs_re = self.tableWidget_dadosBrutos.item(1, 6).text() ; hs_re=float(hs_re)
            alturadoinstrumento = self.tableWidget_dadosBrutos.item(0, 2).text().strip() ;             alturadoinstrumento = float(alturadoinstrumento)
            vt_re = self.tableWidget_dadosBrutos.item(1, 3).text()
            vt_re = self.formata_angulo_tabela(vt_re)
            dh_calculado = ((di_re * math.sin(vt_re * math.pi / 180))) ; dh_calculado = float(dh_calculado)

            #print('di_re: ', di_re)
            #print('hs_re: ', hs_re)
            #print('vt_re: ', vt_re)
            #print('dh calculado ', dh_calculado)

            E_re = float(E_estacao)
            N_re = float(N_estacao) + dh_calculado
            Z_re = float(Z_estacao) + ((di_re * math.cos(vt_re * math.pi / 180)) + alturadoinstrumento - hs_re)


            E_re = round(E_re,3); E_re = str(E_re)
            N_re = round(N_re,3); N_re = str(N_re)
            Z_re = round(Z_re,3); Z_re = str(Z_re)

            print('COORDENADAS DE ESTACAO: ', E_re, N_re, Z_re)
            print(" ")

            self.lineEdit_6.setText(N_re)
            self.lineEditRe_E.setText(E_re)
            self.lineEditRe_H.setText(Z_re)

            #print(self.lineEdit_6.text())



        if N_estacao:
            # se string nao vazia:
            yinicial = N_estacao
            print yinicial, 'y'

        if E_estacao:
            # se string nao vazia:
            xinicial = E_estacao
            print xinicial , 'x'

        if Z_estacao:
            # se string nao vazia:
            zinicial = Z_estacao
            print zinicial , 'z'

        # Azimute Inicial
        if not N_re and not E_re and not Z_re:
            azimuteinicial = 180
            self.lineEditAzimute.setText(str(azimuteinicial))
        else:
            azimuteinicial = f.azimuteAB(E_re,N_re,E_estacao,N_estacao)
            self.lineEditAzimute.setText(str(azimuteinicial))
            #print('Azimute Calculado de: E_re',E_re, 'N_re: ',N_re, 'E_estacao: ', E_estacao, 'N_estacao: ', N_estacao)
            #print('tipo: E_re',type(E_re), 'N_re: ',type(N_re), 'E_estacao: ', type(E_estacao), 'N_estacao: ', type(N_estacao))
            print('Azimute Inicial: ',azimuteinicial)
            print(" ")

        # Aqui vai as coordenadas das estacoes
        estacoes = []
        angulo_hz = []
        # pegamos o nome da estacao inicial e re inicial
        # id é o nome
        id_re = self.tableWidget_dadosBrutos.item(1, 0).text()
        id_est= self.tableWidget_dadosBrutos.item(0, 0).text()

        #colocamos na lista
        estacoes.append(id_re)
        estacoes.append(E_re)
        estacoes.append(N_re)
        estacoes.append(Z_re)
        estacoes.append(id_est)
        estacoes.append(E_estacao)
        estacoes.append(N_estacao)
        estacoes.append(Z_estacao)





        # se estiver vazio as coordenadas da estacao de re
        # tem que procurar o primeiro Hz, esse vai ser o azimute



        print "Coordenadas Iniciais:"
        print "X: " , xinicial
        print "Y: " , yinicial
        print "Z: " , zinicial
        print " "


        print "A tabela está com ", linhas , "linhas e " , colunas , " colunas."
        print " "

        self.tableWidget_coordenadasFinais.setRowCount(linhas)
        self.tableWidget_coordenadasFinais.setColumnCount(5)

        linhav = []
        m = 0;

        ############################################################################################3
        # CONTADOR DE ESTACOES E DE RÉS
        ############################################################################################3

        linhadaest = []
        linhadere = []

        for x in range(linhas):

            #print x

            id = self.tableWidget_dadosBrutos.item(x, 0)
            cod = self.tableWidget_dadosBrutos.item(x, 1)
            hz = self.tableWidget_dadosBrutos.item(x, 2)
            vt = self.tableWidget_dadosBrutos.item(x, 3)
            di = self.tableWidget_dadosBrutos.item(x, 4)
            dh = self.tableWidget_dadosBrutos.item(x, 5)
            hs = self.tableWidget_dadosBrutos.item(x, 6)


            if id and cod:
                id = id.text()
                cod = cod.text()

            if cod == "E" or cod == "est" or cod == "EST" or cod == "ESTACAO":

                linhadaest.append(x)


            if cod == "R" or cod == "Ré" or cod == "Re" or cod == "r":
                linhadere.append(x)


        #print 'linha de estacao ', linhadaest
        #print 'linha de re ', linhadere

        #quit()
        ############################################################################################3

        if len(linhadaest) != len(linhadere):
            #print 'NÚMERO DE RÉ DIFERE DO NÚMERO DE ESTAÇÕES'
            #time.sleep(2)
            pass

        estacaoanterior = None
        for i in range(linhas):

            id = self.tableWidget_dadosBrutos.item(i,0)
            cod = self.tableWidget_dadosBrutos.item(i,1)
            hz = self.tableWidget_dadosBrutos.item(i,2)
            vt = self.tableWidget_dadosBrutos.item(i, 3)
            di = self.tableWidget_dadosBrutos.item(i,4)
            dh = self.tableWidget_dadosBrutos.item(i,5)
            hs = self.tableWidget_dadosBrutos.item(i,6)
            if cod and id:
                id = id.text()
                cod = cod.text()

            if cod == "E" or cod == "est" or cod == "ESTACAO" or cod == "EST" and not hs and not dh and not di:

                alturadoinstrumento = self.tableWidget_dadosBrutos.item(i,2).text()
                alturadoinstrumento = float(alturadoinstrumento)
                estacaoatual = id
                print "ESTACAO ATUAL: ", estacaoatual







                #time.sleep(5)
                # codigo antigo
                if estacaoanterior == None:
                    estacaoanterior = estacaoatual

                elif estacaoanterior == estacaoatual:
                    pass

                else:

                    xinicial = xmudanca
                    yinicial = ymudanca
                    zinicial = zmudanca
                    azimuteinicial = azimutedemudanca
                    estacaoanterior = estacaoatual




            elif id and cod and hz and vt and di and dh and hs and cod == "R" or cod == "RE" or cod == "Re" or cod == "re":
                hz_re = hz.text()
                hz_re = self.formata_angulo_tabela(hz_re)
                #print "363: hz_re é: ", hz_re


                vt = vt.text()
                vt = self.formata_angulo_tabela(vt)
                dh = dh.text()
                hs = hs.text()
                di = di.text()

                hs = hs.split('`')

                if len(hs)>1:
                    hs = hs[-1]
                else:
                    hs = hs[0]


                # Codigo antigo
                print('tipo azimuteinicial: ',azimuteinicial,type(azimuteinicial))
                print('tipo hz_re', type(hz_re))
                azimute = float(azimuteinicial) + float(hz_re) - 180
                # codigo antigo


                #print "RE ATUAL: ", id




                if azimute < 0:
                    azimute = azimute + 360
                if azimute > 360:
                    azimute = azimute - 360


                x = float(xinicial) + float(dh) * math.sin((azimute * math.pi) / 180)
                y = float(yinicial) + float(dh) * math.cos((azimute * math.pi) / 180)
                z = float(zinicial) + (( float(di) * math.cos(float(vt) * math.pi / 180)) + float(hs) - float(hs))

                x = round(x, 3)
                y = round(y, 3)
                z = round(z, 3)



                self.adiciona_na_tabela(m, 0, id)
                self.adiciona_na_tabela(m, 1, cod)
                self.adiciona_na_tabela(m, 2, y)
                self.adiciona_na_tabela(m, 3, x)
                self.adiciona_na_tabela(m, 4, z)



            else:

                # SE HZ E VT ESTIVEREM VAZIOS E SE USARMOS .TEXT() ELE VAI DAR ERRO
                hz_va = self.tableWidget_dadosBrutos.item(i, 2)
                vt_va = self.tableWidget_dadosBrutos.item(i, 3)
                dh = self.tableWidget_dadosBrutos.item(i, 5)
                hs = self.tableWidget_dadosBrutos.item(i, 6)
                di = self.tableWidget_dadosBrutos.item(i, 4)
                if hz_va:
                    hz_va = self.formata_angulo_tabela(hz_va.text())
                if vt_va:
                    vt_va = self.formata_angulo_tabela(vt_va.text())
                if dh:
                    #print dh
                    dh = float(dh.text())
                    #print "381: dh é: ", dh
                if di:
                    di = float(di.text())
                if hs:
                    hs = hs.text()
                    hs = hs.split('`')

                    if len(hs) > 1:
                        hs = hs[-1]
                    else:
                        hs = hs[0]
                    hs = float(hs)

                #print "389: hz_re é: ", hz_re , "e hz_va é: ", hz_va
                if hz_va:
                    hz = hz_va - hz_re
                    if hz < 0:
                        hz = hz + 360
                    if hz > 360:
                        hz = hz - 360
                #    print "392: hz calculado é: ", hz
                #print "angulohorizontal ", angulohorizontal
                #print "dh", dh
                
                azimute = float(azimuteinicial) + float(hz) - 180

                if azimute < 0:
                    azimute = azimute + 360
                if azimute > 360:
                    azimute = azimute - 360
                #print "402: azimute inicial é: ", azimuteinicial
                #print "403: azimute calculado é: " , azimute
                #print "id: ", id

                x = float(xinicial) + dh * math.sin((azimute * math.pi) / 180)
                y = float(yinicial) + dh * math.cos((azimute * math.pi) / 180)
                z = float(zinicial) + ((di * math.cos(vt_va * math.pi / 180)) + alturadoinstrumento - hs)

                x = round(x,3)
                y = round(y,3)
                z = round(z,3)

                #print "X: ", x
                #print "Y: ", y
                #print "Z: ", z

                cod = cod.split('`')

                if len(cod) > 1:
                    cod = cod[-1]
                else:
                    cod = cod[0]


                self.adiciona_na_tabela(m, 0, id)
                self.adiciona_na_tabela(m, 1, cod)
                self.adiciona_na_tabela(m, 2, y)
                self.adiciona_na_tabela(m, 3, x)
                self.adiciona_na_tabela(m, 4, z)

                if cod == "V" or cod == "van" or cod == "VANTE":
                    xmudanca = x
                    ymudanca = y
                    zmudanca = z
                    azimutedemudanca = azimute;
                    angulo_sexagesimal = f.dec2sex(hz)
                    angulo_hz.append(id) ; angulo_hz.append(angulo_sexagesimal)
                    #angulo_hz.append()
                    #print "COORDENADAS DO VANTE: ", id, x, y, z
                    #print "AZIMUTE DE MUDANCA:   ", azimutedemudanca, 'EST V: ', id
                    estacoes.append(id)
                    estacoes.append(x)
                    estacoes.append(y)
                    estacoes.append(z)



            m = m + 1

            if cod == "E" or cod == "EST" or cod == "ESTACAO" or cod == "estacao":
                m = m - 1

        print("")
        print("COORDENADAS DAS ESTAÇÕES: ")
        for lista in range(0,len(estacoes),4):
            print(estacoes[lista],estacoes[lista+1],estacoes[lista+2],estacoes[lista+3])
        print("")

        somatorio_angulos_internos = 0
        for lista in range(0, len(angulo_hz), 2):
            print(angulo_hz[lista], angulo_hz[lista + 1])
            somatorio_angulos_internos = somatorio_angulos_internos + angulo_hz[lista + 1]
        print("Soma dos angulos internos: ", somatorio_angulos_internos)


        print("Executado pelo metodo def recalcular(self):")
            #else:










    # Pega lin,col da tabela onde foi clicada
    def cell_was_clicked(self, row, column):

        item = self.tableWidget_dadosBrutos.item(row, column)
        if item:
            ID = item.text()

        # verifica se a celula nao esta vazia
        # se nao estiver, transforma para texto
        if ID:

            print "celula clicada: ", row, ", ", column, " ", ID
        else:
            print "celula clicada: ", row, ", ", column

    def formata_angulo_tabela(self,angulo):

        angulo = angulo.replace('"', '')
        angulo = angulo.replace("'", "")
        angulo = float(angulo)
        angulo = f.sex2dec(angulo)
        return angulo


    def adiciona_na_tabela(self,linha,coluna,variavel):

        item_pto = QTableWidgetItem(str(variavel))
        self.tableWidget_coordenadasFinais.setItem(linha, coluna, item_pto)




    def salva_coordenadas(self):

        global enderecocad

        linhas = self.tableWidget_coordenadasFinais.rowCount()
        print linhas , " linhas"
        #fileDir = os.path.dirname(os.path.realpath('__file__'))

        print enderecocad

        # Verifica se o 2D está ligado
        if self.radioButton2D.isChecked():
            #print '2D'
            filename = enderecocad + ' Coordenadas ' + '2D' + '.txt'


        if self.radioButton3D.isChecked():
            #print '3D'
            filename = enderecocad +  ' Coordenadas ' + '3D' + '.txt'

        with open(filename, 'w') as input:
            for i in range(linhas):
                x = self.tableWidget_coordenadasFinais.item(i,3)
                y = self.tableWidget_coordenadasFinais.item(i,2)
                z = self.tableWidget_coordenadasFinais.item(i,4)

                idp = self.tableWidget_coordenadasFinais.item(i,0)
                cod = self.tableWidget_coordenadasFinais.item(i,1)

                #if x:
                #    print x , "x"
                #if y:
                #    print y, "y"
                #if z:
                #    print z, "z"


                if x and y and z:
                    #print 'xyz'
                    x = x.text()
                    y = y.text()
                    z = z.text()
                    if idp:
                        idp = idp.text()
                    if not idp:
                        idp = ""
                    if cod:
                        cod = cod.text()
                    if not cod:
                        cod = ""

                    if self.radioButton2D.isChecked():
                        # print '2D'
                        z = "0"

                    print idp, cod, y, x, z

                    input.write("%s \t %s \t %s \t %s \t %s\n" % (idp,cod,y,x,z) )

    def plota_pontos2D(self):
        #janela = plt.figure()
        linhas = self.tableWidget_coordenadasFinais.rowCount()
        #print "eStou no plot"
        x = []
        y = []
        for i in range(linhas):
            vax = self.tableWidget_coordenadasFinais.item(i,3)
            vay = self.tableWidget_coordenadasFinais.item(i,2)

            if vax and vay:
                vax = vax.text()
                vay = vay.text()
                x.append(float(vax))
                y.append(float(vay))

        #plt.scatter(x, y, alpha=0.5) - alpha é para transparencia
        plt.axis('equal')
        plt.scatter(x,y)
        plt.title("Exemplo")
        plt.xlabel("Coordenadas X")
        plt.ylabel("Coordenadas Y")
        plt.show()





    # ESSE EH O DA ESTACAO TOPOGRAFIA
    def exporta_dxf(self):

        global enderecocad
        linhas = self.tableWidget_coordenadasFinais.rowCount()

        partefinaldonome = ''

        if self.radioButton2D.isChecked():
            partefinaldonome = " 2D.dxf"
        if self.radioButton3D.isChecked():
            partefinaldonome = " 3D.dxf"

        # print(endereco2dxfpontos); ''' /home/dclarks/TRANSCOR/teste/Q10262.txt '''
        nome_completo_do_arquivo_dxf = dxf.enderecoFinalParaSalvarDxf(enderecocad, partefinaldonome)
        # print(nome_completo_do_arquivo_dxf)

        vax = [];
        vay = [];
        vaz = [];
        descricao = [];
        indice = [];
        descricao_layer = []


        for i in range(linhas):
            valor_de_x = self.tableWidget_coordenadasFinais.item(i, 3)
            valor_de_y = self.tableWidget_coordenadasFinais.item(i, 2)
            valor_de_z = self.tableWidget_coordenadasFinais.item(i, 4)
            indice_individual = self.tableWidget_coordenadasFinais.item(i, 0)
            descricao_individual = self.tableWidget_coordenadasFinais.item(i, 1)

            if valor_de_x and valor_de_y and indice_individual and descricao_individual:
                vax.append(valor_de_x.text())
                vay.append(valor_de_y.text())

                if self.radioButton2D.isChecked():
                    valor_de_z = "0.0"
                    vaz.append(valor_de_z)
                else:
                    vaz.append(valor_de_z.text())
                indice.append(indice_individual.text())
                descricao.append(descricao_individual.text())
                descricao_layer.append("_" + descricao_individual.text())  # coloca underline na camada layer

        N_estacao = self.lineEditEstacao_N.text()
        E_estacao = self.lineEditEstacao_E.text()
        Z_estacao = self.lineEditEstacao_H.text()

        # pega nome da estacao inicial
        indice_estacao = self.tableWidget_dadosBrutos.item(0, 0).text()
        descricao_estacao = self.tableWidget_dadosBrutos.item(0, 1).text()

        print(indice_estacao, descricao_estacao)

        dxf.gravaPontosEstacaoEmDxf(vax, vay, vaz, indice, descricao, descricao_layer, nome_completo_do_arquivo_dxf,N_estacao,E_estacao,Z_estacao,indice_estacao,descricao_estacao)




    def procuraPorta(self):
        list = serial.tools.list_ports.comports()
        connected = []
        for element in list:
            connected.append(element.device)
            porta = str(connected)

            porta = porta.replace("'","")
            porta = porta.replace("[","")
            porta = porta.replace("]","")

            self.lineEdit_portaEncontrada.setText(porta)
        print("Connected COM ports: " + str(connected))



    def botaoTeste(self):

        dwg = ezdxf.new('ac1024')
        flag = dwg.blocks.new(name='FLAG')
        flag.add_polyline2d([(0, 0), (0, 5), (4, 3), (0, 3)])  # the flag as 2D polyline
        flag.add_circle((0, 0), .4, dxfattribs={'color': 2})  # mark the base point with a circle

        modelspace = dwg.modelspace()

        # define os atributos de flag
        flag.add_attdef('NAME', (0.5, -0.5), {'height': 0.5, 'color': 3})
        flag.add_attdef('XPOS', (0.5, -1.0), {'height': 0.25, 'color': 4})
        flag.add_attdef('YPOS', (0.5, -1.5), {'height': 0.25, 'color': 4})

        flag.add_attrib("NAME", "example text").set_pos((100, 100), align='MIDDLE_CENTER')

        modelspace.add_blockref('FLAG', (100, 100),
                                dxfattribs={'xscale': 1, 'yscale': 1, 'rotation': -15, 'layer': "Thiago",
                                            'name': 'MURO'})

        dwg.saveas("TESTESTE.dxf")
        print "Feito"



    def botaoAbrirpontoscsv(self):

        global endereco2dxfpontos

        linhas = self.tableWidget_dadosBrutos_2.rowCount()
        colunas = self.tableWidget_dadosBrutos_2.columnCount()
        aux = QFileDialog.getOpenFileName(None, 'Open File', 'Abrir Arquivo Bruto',
                                          ' Texto *.txt ;; CSV *.csv ;; Todos os Arquivos *.* ')
        filename = aux[0]
        print "Caminho do arquivo: " , filename
        # conta as linhas do txt
        i = 0;
        with open(filename, 'r') as input:
            for line in input:
                if line.strip():
                    if len(line) > 0:
                        i += 1
        endereco2dxfpontos = filename


        print 'Arquivo de coordenadas (linhas): ', i

        self.tableWidget_dadosBrutos_2.setRowCount(i)
        self.tableWidget_dadosBrutos_2.setColumnCount(5)



        i = 0
        with open(filename, 'r') as input:
            for line in input:
                if line.strip():  # EXCLUI LINHAS COM APENAS ESPAÇOS
                    separador = self.lineEdit_separador.text()

                    if separador == "" or separador == " ":
                        line = line.split()

                        id = line[0]
                        des = line[1]
                        x = line[2]
                        y = line[3]
                        z = line[4]

                        #QtGui.QTableWidgetItem
                        item_pto = QTableWidgetItem(id)
                        self.tableWidget_dadosBrutos_2.setItem(i, 0, item_pto)
                        item_pto = QTableWidgetItem(des)
                        self.tableWidget_dadosBrutos_2.setItem(i, 1, item_pto)
                        item_pto = QTableWidgetItem(x)
                        self.tableWidget_dadosBrutos_2.setItem(i, 2, item_pto)
                        item_pto = QTableWidgetItem(y)
                        self.tableWidget_dadosBrutos_2.setItem(i, 3, item_pto)
                        item_pto = QTableWidgetItem(z)
                        self.tableWidget_dadosBrutos_2.setItem(i, 4, item_pto)
                        print "padrao:", separador
                        print len(separador)



                    else:

                        print "padrao:", separador
                        print len(separador)
                        line = line.split(separador)

                        id = line[0]
                        des = line[1]
                        x = line[2]
                        y = line[3]
                        z = line[4]

                        item_pto = QTableWidgetItem(id)
                        self.tableWidget_dadosBrutos_2.setItem(i, 0, item_pto)
                        item_pto = QTableWidgetItem(des)
                        self.tableWidget_dadosBrutos_2.setItem(i, 1, item_pto)
                        item_pto = QTableWidgetItem(x)
                        self.tableWidget_dadosBrutos_2.setItem(i, 2, item_pto)
                        item_pto = QTableWidgetItem(y)
                        self.tableWidget_dadosBrutos_2.setItem(i, 3, item_pto)
                        item_pto = QTableWidgetItem(z)
                        self.tableWidget_dadosBrutos_2.setItem(i, 4, item_pto)



                        print "nao é none"

                    i = i + 1

    # é o da aba pontos 2 dxf
    def gravapontosdxfcsv(self):

        global endereco2dxfpontos

        if self.radioButtonpontotodxf2d.isChecked():
            partefinaldonome = " 2D.dxf"
        if self.radioButtonponto2dxf3d.isChecked():
            partefinaldonome = " 3D.dxf"

        #print(endereco2dxfpontos); ''' /home/dclarks/TRANSCOR/teste/Q10262.txt '''
        nome_completo_do_arquivo_dxf = dxf.enderecoFinalParaSalvarDxf(endereco2dxfpontos,partefinaldonome)
        #print(nome_completo_do_arquivo_dxf)
        linhas = self.tableWidget_dadosBrutos_2.rowCount()

        vax = []; vay = []; vaz = []; descricao = []; indice =[]; descricao_layer=[]

        i = 0
        for i in range(linhas):
            valor_de_x = self.tableWidget_dadosBrutos_2.item(i, 2)
            valor_de_y = self.tableWidget_dadosBrutos_2.item(i, 3)
            valor_de_z = self.tableWidget_dadosBrutos_2.item(i, 4)
            indice_individual = self.tableWidget_dadosBrutos_2.item(i, 0)
            descricao_individual = self.tableWidget_dadosBrutos_2.item(i, 1)
            i = i + 1
            if valor_de_x and valor_de_y and indice_individual and descricao_individual:
                vax.append(valor_de_x.text())
                vay.append(valor_de_y.text())
                if self.radioButtonpontotodxf2d.isChecked():
                    vaz.append("0.0")
                else:
                    vaz.append(valor_de_z.text())
                indice.append(indice_individual.text())
                descricao.append(descricao_individual.text())
                descricao_layer.append("_" + descricao_individual.text())  # coloca underline na camada layer

        dxf.gravaPontosEmDxf(vax,vay,vaz,indice,descricao,descricao_layer,nome_completo_do_arquivo_dxf)






    def adiciona_na_tabela2(self,linha,coluna,variavel):

        item_pto = QTableWidgetItem(str(variavel))
        self.tableWidget_dadosBrutos_2.setItem(linha, coluna, item_pto)

    def reordenarTabela(self):

        linhas = self.tableWidget_dadosBrutos_2.rowCount()
        sequencia = self.lineEdit_padrao.text()

        print "Linhas da tabela: ", linhas
        a = []; b = []; c = []; d = []; e = []

        for i in range(linhas):

            itema = self.tableWidget_dadosBrutos_2.item(i, 0)
            itemb = self.tableWidget_dadosBrutos_2.item(i, 1)
            itemc = self.tableWidget_dadosBrutos_2.item(i, 2)
            itemd = self.tableWidget_dadosBrutos_2.item(i, 3)
            iteme = self.tableWidget_dadosBrutos_2.item(i, 4)

            if itema:
                itema = itema.text()
            if itemb:
                itemb = itemb.text()
            if itemc:
                itemc = itemc.text()
            if itemd:
                itemd = itemd.text()
            if iteme:
                iteme = iteme.text()

            a.append(itema)
            b.append(itemb)
            c.append(itemc)
            d.append(itemd)
            e.append(iteme)


        [aa,bb,cc,dd,ee] = my_functions.reordenaTabela(sequencia,a,b,c,d,e)

        for linha in range(linhas):
            print "linha: ", linha
            self.adiciona_na_tabela2(linha,0,str(aa[linha]))
            self.adiciona_na_tabela2(linha,1,str(bb[linha]))
            self.adiciona_na_tabela2(linha,2,str(cc[linha]))
            self.adiciona_na_tabela2(linha,3,str(dd[linha]))
            self.adiciona_na_tabela2(linha,4,str(ee[linha]))

        a = []; b = []; c = []; d = []; e = []



    def botaoTrocaVirgulaPonto(self):

        a = [self.lineEditEstacao_N.text(), self.lineEditEstacao_E.text(), self.lineEditEstacao_H.text(), self.lineEdit_6.text(), self.lineEditRe_E.text(), self.lineEditRe_H.text()]
        b = []
        for texto in a:
            texto = my_functions.trocaPontoVirgula(texto)
            b.append(texto)

        self.lineEditEstacao_N.setText(b[0])
        self.lineEditEstacao_E.setText(b[1])
        self.lineEditEstacao_H.setText(b[2])
        self.lineEdit_6.setText(b[3])
        self.lineEditRe_E.setText(b[4])
        self.lineEditRe_H.setText(b[5])

    def recalcularPoligonalporDoisPontos(self):
        proximaestacaox = 0
        proximaestacaoy = 0
        proximaestacaoz = 0
        proximaestacaonome = 0
        atualestacaox = 0
        atualestacaoy = 0
        atualestacaoz = 0
        xinicial = 0
        yinicial = 0
        zinicial = 0
        # estacao começa com 1 porque se for 1 e azimute for o hz
        # seu calculo vai ser só somar outros angulos hz para az
        # se azimute for so somar, dai a variavel azimutesosomar passa a ser 1
        # dai verificar com if se estacao =1 e azimutesosomar = 1
        # nos proximos tem que colocar estacao 2 e assim por diante
        estacao = 0
        azimuteinicial = 180
        alturadoinstrumento = 0

        azimute = None

        ''' 
            Procurar se tem PI
            Se tiver procura novamente pelo mesmo ponto e já faz o cálculo PD PI
            Pega indice da linha PI pra apagar ela
            E coloca na tabela o hz me PD
            Pegar xo yo zo da tabela.
            Procurar estacoes
            se achar proxima estacao 
        '''

        # conta as linhas e colunas na tabela de dados brutos para os laços for
        linhas = self.tableWidget_dadosBrutos.rowCount()
        colunas = self.tableWidget_dadosBrutos.columnCount()

        N_estacao = self.lineEditEstacao_N.text()
        E_estacao = self.lineEditEstacao_E.text()
        Z_estacao = self.lineEditEstacao_H.text()

        N_re = self.lineEdit_6.text()
        E_re = self.lineEditRe_E.text()
        Z_re = self.lineEditRe_H.text()

        if not N_re and not E_re and not Z_re:
            # print "dentro"
            # time.sleep(2)
            di_re = self.tableWidget_dadosBrutos.item(1, 4).text();
            di_re = float(di_re)
            hs_re = self.tableWidget_dadosBrutos.item(1, 6).text();
            hs_re = float(hs_re)
            alturadoinstrumento = self.tableWidget_dadosBrutos.item(0, 2).text().strip();
            alturadoinstrumento = float(alturadoinstrumento)
            vt_re = self.tableWidget_dadosBrutos.item(1, 3).text()
            vt_re = self.formata_angulo_tabela(vt_re)
            dh_calculado = ((di_re * math.sin(vt_re * math.pi / 180)));
            dh_calculado = float(dh_calculado)

            # print('di_re: ', di_re)
            # print('hs_re: ', hs_re)
            # print('vt_re: ', vt_re)
            # print('dh calculado ', dh_calculado)

            E_re = float(E_estacao)
            N_re = float(N_estacao) + dh_calculado
            Z_re = float(Z_estacao) + ((di_re * math.cos(vt_re * math.pi / 180)) + alturadoinstrumento - hs_re)

            E_re = round(E_re, 3);
            E_re = str(E_re)
            N_re = round(N_re, 3);
            N_re = str(N_re)
            Z_re = round(Z_re, 3);
            Z_re = str(Z_re)

            print('COORDENADAS DE ESTACAO: ', E_re, N_re, Z_re)
            print(" ")

            self.lineEdit_6.setText(N_re)
            self.lineEditRe_E.setText(E_re)
            self.lineEditRe_H.setText(Z_re)

            # print(self.lineEdit_6.text())

        if N_estacao:
            # se string nao vazia:
            yinicial = N_estacao
            print yinicial, 'y'

        if E_estacao:
            # se string nao vazia:
            xinicial = E_estacao
            print xinicial, 'x'

        if Z_estacao:
            # se string nao vazia:
            zinicial = Z_estacao
            print zinicial, 'z'

        # Azimute Inicial
        if not N_re and not E_re and not Z_re:
            azimuteinicial = 180
            self.lineEditAzimute.setText(str(azimuteinicial))
        else:
            azimuteinicial = f.azimuteAB(E_re, N_re, E_estacao, N_estacao)
            self.lineEditAzimute.setText(str(azimuteinicial))
            # print('Azimute Calculado de: E_re',E_re, 'N_re: ',N_re, 'E_estacao: ', E_estacao, 'N_estacao: ', N_estacao)
            # print('tipo: E_re',type(E_re), 'N_re: ',type(N_re), 'E_estacao: ', type(E_estacao), 'N_estacao: ', type(N_estacao))
            print('Azimute Inicial: ', azimuteinicial)
            print(" ")

        # Aqui vai as coordenadas das estacoes
        estacoes = []
        angulo_hz = []

        # pegamos o nome da estacao inicial e re inicial
        # id é o nome
        id_re = self.tableWidget_dadosBrutos.item(1, 0).text()
        id_est = self.tableWidget_dadosBrutos.item(0, 0).text()

        # colocamos na lista
        estacoes.append(id_re); estacoes.append(E_re); estacoes.append(N_re); estacoes.append(Z_re); estacoes.append(id_est)
        estacoes.append(E_estacao); estacoes.append(N_estacao); estacoes.append(Z_estacao)

        # se estiver vazio as coordenadas da estacao de re
        # tem que procurar o primeiro Hz, esse vai ser o azimute

        print "Coordenadas Iniciais:"
        print "X: ", xinicial
        print "Y: ", yinicial
        print "Z: ", zinicial
        print " "

        print "A tabela está com ", linhas, "linhas e ", colunas, " colunas."
        print " "

        self.tableWidget_coordenadasFinais.setRowCount(linhas)
        self.tableWidget_coordenadasFinais.setColumnCount(5)

        linhav = []
        m = 0;

        ############################################################################################3
        # CONTADOR DE ESTACOES E DE RÉS
        ############################################################################################3

        linhadaest = []
        linhadere = []

        for x in range(linhas):

            # print x

            id = self.tableWidget_dadosBrutos.item(x, 0)
            cod = self.tableWidget_dadosBrutos.item(x, 1)
            hz = self.tableWidget_dadosBrutos.item(x, 2)
            vt = self.tableWidget_dadosBrutos.item(x, 3)
            di = self.tableWidget_dadosBrutos.item(x, 4)
            dh = self.tableWidget_dadosBrutos.item(x, 5)
            hs = self.tableWidget_dadosBrutos.item(x, 6)

            if id and cod:
                id = id.text()
                cod = cod.text()

            if cod == "E" or cod == "est" or cod == "EST" or cod == "ESTACAO":
                linhadaest.append(x)

            if cod == "R" or cod == "Ré" or cod == "Re" or cod == "r":
                linhadere.append(x)



        if len(linhadaest) != len(linhadere):
            # print 'NÚMERO DE RÉ DIFERE DO NÚMERO DE ESTAÇÕES'
            # time.sleep(2)
            pass

        estacaoanterior = None
        for i in range(linhas):

            id = self.tableWidget_dadosBrutos.item(i, 0)
            cod = self.tableWidget_dadosBrutos.item(i, 1)
            hz = self.tableWidget_dadosBrutos.item(i, 2)
            vt = self.tableWidget_dadosBrutos.item(i, 3)
            di = self.tableWidget_dadosBrutos.item(i, 4)
            dh = self.tableWidget_dadosBrutos.item(i, 5)
            hs = self.tableWidget_dadosBrutos.item(i, 6)
            if cod and id:
                id = id.text()
                cod = cod.text()

            if cod == "E" or cod == "est" or cod == "ESTACAO" or cod == "EST" and not hs and not dh and not di:

                alturadoinstrumento = self.tableWidget_dadosBrutos.item(i, 2).text()
                alturadoinstrumento = float(alturadoinstrumento)
                estacaoatual = id
                print "ESTACAO ATUAL: ", estacaoatual

                try:
                    # print('EXISTE A ESTACAO "LISTA", ', id, ' NA LISTA: ', id in estacoes)
                    posicao_da_estacao = estacoes.index(id)
                    # print('O INDEX DA ESTACAO "LISTA": ', estacoes.index(id))
                    # print('ESTACAO: ', estacoes[posicao_da_estacao])
                    print('X,Y,Z "LISTA": ', estacoes[posicao_da_estacao + 1], estacoes[posicao_da_estacao + 2],
                          estacoes[posicao_da_estacao + 3])
                    xinicial = estacoes[posicao_da_estacao + 1]
                    yinicial = estacoes[posicao_da_estacao + 2]
                    zinicial = estacoes[posicao_da_estacao + 3]
                except:
                    print('VALOR NAO ENCONTRADO: ', id)


            elif id and cod and hz and vt and di and dh and hs and cod == "R" or cod == "RE" or cod == "Re" or cod == "re":
                hz_re = hz.text()
                hz_re = self.formata_angulo_tabela(hz_re)
                # print "363: hz_re é: ", hz_re

                vt = vt.text()
                vt = self.formata_angulo_tabela(vt)
                dh = dh.text()
                hs = hs.text()
                di = di.text()

                hs = hs.split('`')

                if len(hs) > 1:
                    hs = hs[-1]
                else:
                    hs = hs[0]

                # Codigo antigo
                # print('tipo azimuteinicial: ',azimuteinicial,type(azimuteinicial))
                # print('tipo hz_re', type(hz_re))
                # azimute = float(azimuteinicial) + float(hz_re) - 180
                # codigo antigo

                # print "RE ATUAL: ", id

                try:
                    # print('EXISTE A RE "LISTA", ', id, ' NA LISTA: ', id in estacoes)
                    posicao_da_estacao = estacoes.index(id)
                    # print('O INDEX DA RE "LISTA": ', estacoes.index(id))
                    print('ESTACAO: ', estacoes[posicao_da_estacao])
                    print('X,Y,Z: ', estacoes[posicao_da_estacao + 1], estacoes[posicao_da_estacao + 2],
                          estacoes[posicao_da_estacao + 3])
                    print('AZIMUTE AB "LISTA": ', id, estacaoatual,
                          f.azimuteAB(estacoes[posicao_da_estacao + 1], estacoes[posicao_da_estacao + 2], xinicial,
                                      yinicial))
                    azimuteinicial = f.azimuteAB(estacoes[posicao_da_estacao + 1], estacoes[posicao_da_estacao + 2],
                                                 xinicial, yinicial)
                    azimutedaprimeirare = f.azimuteAB(xinicial, yinicial, estacoes[posicao_da_estacao + 1],
                                                      estacoes[posicao_da_estacao + 2])
                    print " "
                    # print('AZIMUTE PRIMEIRA RE: ', azimutedaprimeirare, 'Azimute inicial: ', azimuteinicial)
                    # time.sleep(4)
                except:
                    print('VALOR NAO ENCONTRADO: ', id)
                    time.sleep(40)

                if azimutedaprimeirare < 0:
                    azimutedaprimeirare = azimutedaprimeirare + 360
                if azimutedaprimeirare > 360:
                    azimutedaprimeirare = azimutedaprimeirare - 360

                # print vt, dh, hs, di, azimute, hz_re

                if azimuteinicial < 0:
                    azimuteinicial = azimuteinicial + 360
                if azimuteinicial > 360:
                    azimuteinicial = azimuteinicial - 360
                # print "402: azimute inicial é: ", azimuteinicial
                # print "403: azimute calculado é: ", azimute
                # print "id: ", id

                x = float(xinicial) + float(dh) * math.sin((azimutedaprimeirare * math.pi) / 180)
                y = float(yinicial) + float(dh) * math.cos((azimutedaprimeirare * math.pi) / 180)
                z = float(zinicial) + ((float(di) * math.cos(float(vt) * math.pi / 180)) + float(hs) - float(hs))

                x = round(x, 3)
                y = round(y, 3)
                z = round(z, 3)

                self.adiciona_na_tabela(m, 0, id)
                self.adiciona_na_tabela(m, 1, cod)
                self.adiciona_na_tabela(m, 2, y)
                self.adiciona_na_tabela(m, 3, x)
                self.adiciona_na_tabela(m, 4, z)



            else:

                # SE HZ E VT ESTIVEREM VAZIOS E SE USARMOS .TEXT() ELE VAI DAR ERRO
                hz_va = self.tableWidget_dadosBrutos.item(i, 2)
                vt_va = self.tableWidget_dadosBrutos.item(i, 3)
                dh = self.tableWidget_dadosBrutos.item(i, 5)
                hs = self.tableWidget_dadosBrutos.item(i, 6)
                di = self.tableWidget_dadosBrutos.item(i, 4)
                if hz_va:
                    hz_va = self.formata_angulo_tabela(hz_va.text())
                if vt_va:
                    vt_va = self.formata_angulo_tabela(vt_va.text())
                if dh:
                    # print dh
                    dh = float(dh.text())
                    # print "381: dh é: ", dh
                if di:
                    di = float(di.text())
                if hs:
                    hs = hs.text()
                    hs = hs.split('`')

                    if len(hs) > 1:
                        hs = hs[-1]
                    else:
                        hs = hs[0]
                    hs = float(hs)

                # print "389: hz_re é: ", hz_re , "e hz_va é: ", hz_va
                if hz_va:
                    hz = hz_va - hz_re
                    if hz < 0:
                        hz = hz + 360
                    if hz > 360:
                        hz = hz - 360
                #    print "392: hz calculado é: ", hz
                # print "angulohorizontal ", angulohorizontal
                # print "dh", dh

                azimute = float(azimuteinicial) + float(hz) - 180

                if azimute < 0:
                    azimute = azimute + 360
                if azimute > 360:
                    azimute = azimute - 360
                # print "402: azimute inicial é: ", azimuteinicial
                # print "403: azimute calculado é: " , azimute
                # print "id: ", id

                x = float(xinicial) + dh * math.sin((azimute * math.pi) / 180)
                y = float(yinicial) + dh * math.cos((azimute * math.pi) / 180)
                z = float(zinicial) + ((di * math.cos(vt_va * math.pi / 180)) + alturadoinstrumento - hs)

                x = round(x, 3)
                y = round(y, 3)
                z = round(z, 3)

                # print "X: ", x
                # print "Y: ", y
                # print "Z: ", z

                cod = cod.split('`')

                if len(cod) > 1:
                    cod = cod[-1]
                else:
                    cod = cod[0]

                self.adiciona_na_tabela(m, 0, id)
                self.adiciona_na_tabela(m, 1, cod)
                self.adiciona_na_tabela(m, 2, y)
                self.adiciona_na_tabela(m, 3, x)
                self.adiciona_na_tabela(m, 4, z)

                if cod == "V" or cod == "van" or cod == "VANTE":
                    xmudanca = x
                    ymudanca = y
                    zmudanca = z
                    # azimutedemudanca = azimute;
                    # print "COORDENADAS DO VANTE: ", id, x, y, z
                    # print "AZIMUTE DE MUDANCA:   ", azimutedemudanca, 'EST V: ', id
                    estacoes.append(id)
                    estacoes.append(x)
                    estacoes.append(y)
                    estacoes.append(z)
                    angulo_sexagesimal = f.dec2sex(hz)
                    angulo_hz.append(id) ; angulo_hz.append(angulo_sexagesimal)

            m = m + 1

            if cod == "E" or cod == "EST" or cod == "ESTACAO" or cod == "estacao":
                m = m - 1

        print("")
        print("COORDENADAS DAS ESTAÇÕES: ")
        for lista in range(0, len(estacoes), 4):
            print(estacoes[lista], estacoes[lista + 1], estacoes[lista + 2], estacoes[lista + 3])
        print("")

        somatorio_angulos_internos = 0
        for lista in range(0,len(angulo_hz),2):
            print(angulo_hz[lista], angulo_hz[lista+1])
            somatorio_angulos_internos = somatorio_angulos_internos + angulo_hz[lista+1]
        print("Soma dos angulos internos: " , somatorio_angulos_internos)
        print("Executado pelo método def recalcularPoligonalporDoisPontos(self):")


f = ferramentas.Ferramentas()
#topo = topografia.Topografia()




app = QApplication([])
form = JanelaPrincipal()
#topo = topografia.Topografia()





form.show()
app.exec_()
