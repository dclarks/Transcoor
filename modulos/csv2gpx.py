
entrada = '/home/thiago/scripts/python/android/IgaTracker/Igreja Maranata Boa Vista.txt'
saida = '/home/thiago/scripts/python/android/IgaTracker/IGREJA_BOAVISTA.gpx'

a = open(entrada)
print a
b = open(saida,'w')
b.close()
tabela = []
for line in a:
    # strip() remove os '\n'
    tabela.append(line.strip().split(','))
# 81 linhas

tam_lin = len(tabela)-1
print tam_lin

i = 0
while i <= tam_lin:
    print tabela[i][0]
    i = i + 1

print type(tabela[0])

b = open(saida,'a')
linha_um = '<?xml version="1.0" encoding="UTF-8" ?> \n'
linha_do = '<gpx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.topografix.com/GPX/1/0" xsi:schemaLocation="http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd" version="1.0"  creator="IgaTracker"> \n'
b.write(linha_um)
b.write(linha_do)
b.write("\n")
# Transforma os Waypoints
i = 0
j = 0
while i < tam_lin:
    print i
    
    if (tabela[i][3] != 'PONTO'):
        b.write('<wpt lat="' + str(tabela[i][0]) +'" ' + 'lon="'+ str(tabela[i][1]) + '">' + '<ele>' + str(tabela[i][2]) + '</ele>' + '<name>' + str(tabela[i][3]) + '</name> </wpt> \n'  )
        j = j + 1
    i = i + 1        

# Transforma os Tracks
i = 0
j = 0
# tem = 0 indica que nao tem tracks - PONTO
tem = 0
while i < tam_lin:
    print i
    
    if (tabela[i][3] == 'PONTO'):
        tem = 1
        break
    i = i + 1

if tem == 1:
    b.write('<trk> \n \t <trkseg>')
    i = 0
    while i < tam_lin:
        b.write('<trkpt lat="' + str(tabela[i][0]) +'" ' + 'lon="'+ str(tabela[i][1]) + '">' + '</trkpt>' + '<ele>' + str(tabela[i][2]) + '</ele> \n')
        i = i + 1
b.write('</trkseg> \n </trk>')
b.write('</gpx>')
b.close()