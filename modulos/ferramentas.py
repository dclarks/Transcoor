#!/usr/bin/env python   # (if running from bash)
import math
class Ferramentas:
    
    def __init__(self):
       pass 

    def numero_linhas(self,inputfile):

        "Conta o numero de linhas do arquivo"
        num_lines = sum(1 for line in open(inputfile))
        return num_lines

    def distancia(self,xa,ya,xb,yb):
        dist = math.sqrt( math.pow(xb-xa,2) + math.pow(yb-ya,2)   )
        return dist


    def azimuteAB(self,xa,ya,xb,yb):
        # Converte de string para float
        xa = float(xa)
        ya = float(ya)
        xb = float(xb)
        yb = float(yb)
        # Calcula numerador e denominador
        numerador = xb - xa
        denominador = yb - ya
        if (xa == xb == yb == ya):
            print("Os pontos precisam ser diferentes")

        if (numerador == 0 and denominador != 0):
            if denominador < 0:
                angulo = 180
            else:
                angulo = 360
            #print('AzimuteAB: ', angulo)
            return angulo

        if (denominador == 0 and numerador != 0):

            angulo = 0
            return angulo
            #print('AzimuteAB: ', angulo)

        if (numerador > 0) and (denominador > 0):
            numerador = math.fabs(numerador)
            denominador = math.fabs(denominador)
            angulo = (math.atan2(numerador,denominador)) * 180 / math.pi
            #print('AzimuteAB: ', angulo)
            return angulo

        if (numerador > 0) and (denominador < 0):
            numerador = math.fabs(numerador)
            denominador = math.fabs(denominador)
            angulo = 180 - ((math.atan2(numerador,denominador)) * 180 / math.pi)
            #print('AzimuteAB: ', angulo)
            return angulo

        if (numerador < 0) and (denominador < 0):
            numerador = math.fabs(numerador)
            denominador = math.fabs(denominador)
            angulo = 180 + ((math.atan2(numerador,denominador)) * 180 / math.pi)
            #print('AzimuteAB: ', angulo)
            return angulo
            
        if (numerador < 0) and (denominador > 0):
            numerador = math.fabs(numerador)
            denominador = math.fabs(denominador)
            angulo = 360 - ((math.atan2(numerador,denominador)) * 180 / math.pi)
            #print('AzimuteAB: ', angulo)
            return angulo


    def azimuteBA(self,xa,ya,xb,yb):
        # Converte de string para float
        xa = float(xa)
        ya = float(ya)
        xb = float(xb)
        yb = float(yb)
        # Calcula numerador e denominador
        numerador = xa - xb
        denominador = ya - yb

        if (numerador > 0) and (denominador > 0):
            numerador = math.fabs(numerador)
            denominador = math.fabs(denominador)
            angulo = (math.atan2(numerador,denominador)) * 180 / math.pi
            return angulo

        if (numerador > 0) and (denominador < 0):
            numerador = math.fabs(numerador)
            denominador = math.fabs(denominador)
            angulo = 180 - ((math.atan2(numerador,denominador)) * 180 / math.pi)
            return angulo

        if (numerador < 0) and (denominador < 0):
            numerador = math.fabs(numerador)
            denominador = math.fabs(denominador)
            angulo = 180 + ((math.atan2(numerador,denominador)) * 180 / math.pi)
            return angulo
            
        if (numerador < 0) and (denominador > 0):
            numerador = math.fabs(numerador)
            denominador = math.fabs(denominador)
            angulo = 360 - ((math.atan2(numerador,denominador)) * 180 / math.pi)
            return angulo



    def sex2dec(self,angulo):
        float(angulo)
        resto, inteiro = math.modf(angulo)
        grau = inteiro
        #print "Grau decimal: " , grau
        minuto_g = resto * 100
        resto, inteiro = math.modf(minuto_g)
        minuto = inteiro / 60
        #print "Minutos: " , minuto
        segundos_g = resto * 100
        segundos = segundos_g / 3600
        #print "Segundos: " , segundos
        grau_decimal = grau + minuto + segundos
        return grau_decimal


    def dec2sex(self,angulo):
        float(angulo)
        resto, inteiro = math.modf(angulo)
        grau = inteiro
        aux = resto * 60
        resto, minuto = math.modf(aux)
        segundos = resto * 60
        graus = grau + minuto/100 + segundos/ 10000
        return graus


    def conta_estacoes(self):
        texto = open('/home/thiago/scripts/TopoPy/tcl.txt','r')
        contador = 0
        a = 0
        b = 0

        linha_estacao = []
        contador = 0
        distancia = 0
        for line in texto:

            b = b + 1
            a = line.find('EST:')
            if a != -1:
                contador = contador + 1;
                linha_estacao.append(b) 

        
        #for i,line in enumerate(open("/home/thiago/scripts/TopoPy/tcl.txt")):
        #    print i,line[0:10]

        return linha_estacao   


    def leituras_por_estacao(self):
        texto = open('/home/thiago/scripts/TopoPy/tcl.txt','r')
        
        achou_estacao = 0
        contador = 0
        pv = 0
        col_di = 0
        di = 0.0
        i = 0
        j = 0
        est = 0
        leituras = []
        for line_zero in texto:
            j = j + 1
        
        # Tem que abrir de novo, parece que o 'texto' se esgota no loop anterior
        texto = open('/home/thiago/scripts/TopoPy/tcl.txt','r')
        for line in texto:
            i = i + 1
            pv = line.find('PV :')  
            col_di = line.find('DI=') 
#            print "coluna de DI:", col_di
            est = line.find('EST:')  

            if (pv != -1) and (col_di != -1):
                di = float(line[col_di+4:col_di+13])
#                print "distancia encontrada: ",di
                if di > 1.00:
                    contador = contador + 1;
            
            if (est != -1) :
                
                leituras.append(contador)
                contador = 0
                achou_estacao = achou_estacao + 1

            if j == i:
                leituras.append(contador)
                # Apaga o primeiro valor que eh zero, jah que tem est no inicio do arquivo
                del leituras[0]
        return leituras        
#        print "leituras"
#        print leituras    
#        print achou_estacao
        #for i,line in enumerate(open("/home/thiago/scripts/TopoPy/tcl.txt")):
        #    print i,line[0:10]

    #####################################################################################################

    #####################################################################################################    


    #Exemplo para mostrar linhas especificas
    #print(''.join(open('/home/thiago/scripts/TopoPy/tcl.txt', 'r').readlines()[0:10])),

    # Contar as leituras para criar as matrizes
    def conta_leituras(self):
        print("oi")

    def cria_matriz(m, n):
        # Apenas diz '_' para usar e ignorar a variavel
        return [[0]*n for _ in range(m)]

    #####################################################################################################  
    # do vetor cria matrizes
    #a = cria_matriz(2, 3)
    
    #####################################################################################################


    def pontos_por_estacao(self):
        texto = open('/home/thiago/scripts/TopoPy/tcl.txt','r')
        
        achou_estacao = 0
        contador = 0
        pv = 0
        col_di = 0
        di = 0.0
        i = 0
        j = 0
        est = 0
        leituras = []
        for line_zero in texto:
            j = j + 1
        
        # Tem que abrir de novo, parece que o 'texto' se esgota no loop anterior
        texto = open('/home/thiago/scripts/TopoPy/tcl.txt','r')
        for line in texto:
            i = i + 1
            pv = line.find('PV :')  
            col_di = line.find('DI=') 
#            print "coluna de DI:", col_di
            est = line.find('EST:')  

            if (pv != -1) and (col_di != -1):
                di = float(line[col_di+4:col_di+13])
#                print "distancia encontrada: ",di
                if di > 1.00:
                    contador = contador + 1;
            
            if (est != -1) :
                
                leituras.append(contador)
                contador = 0
                achou_estacao = achou_estacao + 1

            if j == i:
                leituras.append(contador)
                # Apaga o primeiro valor que eh zero, jah que tem est no inicio do arquivo
                del leituras[0]
        tam = len(leituras)
        i = 0
        
        for i in range(tam):
            if leituras[i] % 2 == 0:
                continue
            else:
                print("Problema de contagem de linhas na estacao: ", i)
        return leituras
    #####################################################################################################

    #####################################################################################################


    
