import os
import math
import statistics
import time

file_gerencia = os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_gerencia.txt')
file_abstracao = os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_abstracao.txt')
# file_media_movel = os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_media_movel.txt')

if os.path.exists(file_abstracao):
   os.remove(file_abstracao)

Gerencia = open(file_gerencia, 'a+')
Gerencia.close()
Abstracao = open(file_abstracao, 'a+')
Abstracao.close()
# MediaMovel = open(file_media_movel, 'a+')
# MediaMovel.close()

# s = open(file_abstracao,'w')
# s.write("0"+"\n")
# s.write("0"+"\n")
# s.write("0"+"\n")
# s.close()

global max_rssi, min_rssi, rssi_media_dbm, desv_pad_rssi_dbm, num_mm
num_mm = 0
global PSR_DL
global PSR_UL
max_rssi = -100.0
min_rssi = -10.0
rssi_media_dbm = 0
desv_pad_rssi_dbm = 0
PSR_DL = 0
PSR_UL = 0

def grava_abstracao():
    s = open(file_abstracao,'w')
    s.write(str(max_rssi)+"\n")
    s.write(str(min_rssi)+"\n")
    s.write(str(rssi_media_dbm)+"\n")
    s.write(str(desv_pad_rssi_dbm)+"\n")
    s.write(str(PSR_DL)+"\n")
    s.write(str(PSR_UL)+"\n")
    s.close()


def calcula_maximo_minimo(valor):
    global max_rssi, min_rssi

    if (valor > max_rssi):
        max_rssi = valor

    if (valor < min_rssi):
        min_rssi = valor

def captura_dados():
    dados = open(file_gerencia,'r')
    global s1
    global rssi_media_dbm
    global max_rssi, min_rssi
    global desv_pad_rssi_dbm
    global PSR_DL
    global PSR_UL

    x = []
    y = []
    z= []

    for line in dados:
        line=line.strip()
        Y = line.split(';')
        y.append(Y)
    # print(len(y))
    rssi_w = 0
    rssi_media_w = 0
    rssi_media_dbm = 0
    max_rssi = -100.0
    min_rssi = -10.0
    for i in range(len(y)):
        if((y[i][1])!='')and((y[i][2])!=''):
            rssi_dbm = float(y[i][1])
            x.append(rssi_dbm)
            z.append(int(y[i][0]))
            if (len(x) > num_mm): 
                rssi_w = [10**(i/10) for i in x]
                rssi_media_w = sum(rssi_w[-num_mm:])/num_mm
                rssi_media_dbm = 10*math.log(rssi_media_w,10)

                # print(rssi_media_dbm)
                # print(len(x))
            calcula_maximo_minimo(rssi_dbm)


    if (len(x) > 1):
        desv_pad_rssi_dbm = statistics.stdev(x)
        PSR_DL = y[-1][2]
        PSR_UL = y[-1][3]
        # psr = round((1-((len(y) - len(x)) / len(y)))*100,2)
    
    grava_abstracao()
    dados.close()

ultima_condicao_start = 0
print("NIVEL 5 Iniciado")
while True:
    param_n6_n1 = open(os.path.join(os.path.dirname(__file__), '../NIVEL_4/PARAMETROS.txt'), 'r')
    condicao_start = param_n6_n1.readline()
    num_mm = param_n6_n1.readline()
    num_mm = param_n6_n1.readline()
    if (num_mm != ''):
        num_mm = int(num_mm)
    if (condicao_start != ''):
        condicao_start = int(condicao_start)
        param_n6_n1.close()

    if(ultima_condicao_start == 1 and condicao_start == 0):
        grava_abstracao()
    
    if(ultima_condicao_start == 0 and condicao_start == 1):
        Abstracao = open(file_abstracao, 'w').close()
    
    if(condicao_start == 1):
        time.sleep(.05)
        # s = open(file_abstracao,'w')
        # s.write("0"+"\n")
        # s.write("0"+"\n")
        # s.write("0"+"\n")
        # s.write("0"+"\n")
        # s.write("0"+"\n")
        # s.close()
        captura_dados()

    ultima_condicao_start = condicao_start