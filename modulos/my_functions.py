#--coding: utf-8 --

def add(a, b):
    return a + b

def trocaPontoVirgula(argumento):

    argumento = argumento.strip()
    argumento = argumento.replace(',','.')

    return argumento

def reordenaTabela(sequencia,a,b,c,d,e):
    if sequencia:
        sequencia = sequencia.split()
        if len(sequencia) == 5:
            #print len(sequencia)
            aa = str(sequencia[0])
            #print "aa vale: ", aa
            if aa == "a":
                aa = a
            elif aa == "b":
                aa = b
            elif aa == "c":
                aa = c
            elif aa == "d":
                aa = d
            elif aa == "e":
                aa = e

            bb = str(sequencia[1])
            if bb == "a":
                bb = a
            elif bb == "b":
                bb = b
            elif bb == "c":
                bb = c
            elif bb == "d":
                bb = d
            elif bb == "e":
                bb = e

            cc = str(sequencia[2])
            if cc == "a":
                cc = a
            elif cc == "b":
                cc = b
            elif cc == "c":
                cc = c
            elif cc == "d":
                cc = d
            elif cc == "e":
                cc = e

            dd = str(sequencia[3])
            if dd == "a":
                dd = a
            elif dd == "b":
                dd = b
            elif dd == "c":
                dd = c
            elif dd == "d":
                dd = d
            elif dd == "e":
                dd = e

            ee = str(sequencia[4])
            if ee == "a":
                ee = a
            elif ee == "b":
                ee = b
            elif ee == "c":
                ee = c
            elif ee == "d":
                ee = d
            elif ee == "e":
                ee = e

            #print " estou no if"
        else:
            aa = a

            bb = b
            cc = c
            dd = d
            ee = e
            #print "estou no else"

    return aa,bb,cc,dd,ee


def filtraLinhasM21(line):
    line = line.replace('_+', '')
    line = line.replace('_ ?+', '@')
    line = line.replace('_*', '@')
    line = line.replace('_,', '@')

    line = line.replace('m', '@')
    line = line.replace('d+', '@')
    line = line.replace(',', '@')
    line = line.replace('t', '@')
    line = line.replace('+', '@')
    line = line.replace('_', '')
    line = line.replace("'", '')
    line = line.replace('-', '@')

    return line

def filtraLinhasM21Estacao(line):
    line = line.replace('(','@')
    line = line.replace(')','@')
    line = line.replace('_', '')
    line = line.replace("'", '')
    #line = line.split('@') #separa no @
    return line


def contaArrobas(line):
    i = 0;
    for j in line:
        if j == "@":
            i = i + 1
    return i
