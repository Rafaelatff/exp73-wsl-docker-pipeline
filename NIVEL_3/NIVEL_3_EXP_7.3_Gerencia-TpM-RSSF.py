# Python para o Radiuino over Arduino
##import serial
import math
import time
import struct
import socket
from time import localtime, strftime
import os

contador_DL = 0 # Contador de sucesso de pacotes de DL recebidos
contador_UL = 0 # Contador de sucesso de pacotes de UL recebidos
PKTdown = 0

perdas_totais = 0
perdas_DL_totais    = 0
perdas_UL_totais    = 0

# Para tratamento de bursts de perdas
perdas_parciais = 0
perdas_DL_parciais  = 0
perdas_UL_parciais  = 0

ultimo_pacote_UL = 0 # Ultimo pacote recebido antes da situação de falha
falha_na_comunicacao = False

#========================Definições da tecnologia de comunicação========================================
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.settimeout(0.5)

HOST = input("Digite o endereco IP do sensor:")  # Endereco IP do Sensor
PORT = input("Digite A porta do Socket:")            # Porta que o Servidor esta
HOST2 = ''  #endereço do Servidor socket

Sensor = (HOST, int(PORT))   #conjunto endereço e porta utilizado para o envio da informação
orig = (HOST2, int(PORT))     ##conjunto endereço e porta utilizado para o recebimento da informação

udp.bind(orig) #  Inicializa o socket de escuta

#apaga o arquivo de medidas
if os.path.exists(os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_gerencia.txt')):
   os.remove(os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_gerencia.txt'))

# NOME ANTIGOaplicacao
#if os.path.exists("medidas.txt"):
#   os.remove("medidas.txt")
   ################################################
# Cria os arquivos de log
# filename1 = os.path.join(os.path.dirname(__file__), strftime("../NIVEL_4/Medidas_%Y_%m_%d_%H-%M-%S.txt"))
filename2 = os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_gerencia.txt')
filename3 = os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_aplicacao.txt')

Gerencia = open(filename2, 'a+')
Gerencia.close()

# Entra com quantas medidas vai realizar
# num_medidas = input('Entre com o número de medidas = ')

def reiniciar_psr():
   global contador_DL
   global contador_UL
   global falha_na_comunicacao
   global ultimo_pacote_UL
   global perdas_totais
   global perdas_DL_totais  
   global perdas_UL_totais  
   global perdas_parciais
   global perdas_DL_parciais
   global perdas_UL_parciais  
   global PKTdown

   contador_DL = 0
   contador_UL = 0 
   falha_na_comunicacao = 0
   ultimo_pacote_UL = 0
   perdas_totais = 0
   perdas_DL_totais = 0
   perdas_UL_totais = 0
   perdas_parciais = 0
   perdas_DL_parciais = 0
   perdas_UL_parciais = 0
   PKTdown = 0

def grava_comandos(condicao_start):
    arquivo_txt = os.path.join(os.path.dirname(__file__), '../NIVEL_4/PARAMETROS.txt') # está dando nome para o arquivo txt
    s = open(arquivo_txt,'w')
    s.write(str(condicao_start)+"\n")
    s.close()

def leitura_socket(num_medidas):
   global contador_DL
   global contador_UL
   global falha_na_comunicacao
   global ultimo_pacote_UL
   global perdas_totais
   global perdas_DL_totais  
   global perdas_UL_totais  
   global perdas_parciais
   global perdas_DL_parciais
   global perdas_UL_parciais 
   global PKTdown

   filename4 = os.path.join(os.path.dirname(__file__), strftime("../NIVEL_4/LOG_gerencia_%Y_%m_%d_%H-%M-%S.txt"))

   print ("Arquivo de LOG de gerencia: %s" % filename4)
   LOG_gerencia = open(filename4, 'w')
   print ('Time stamp;Contador;RSSI_DL;PSR', file=LOG_gerencia)
#====================================TUNELAMENTO=================================
   # Camada de Aplicação
   byte34 = 0 # LED verde
   byte37 = 0 # LED amarelo
   byte40 = 0 # LED vermelho

   # Camada de Transporte
   byte12 = 0
   byte13 = 0
   byte14 = 0
   perda_PK_RX = 0 # contador de pacotes perdidos na recepção

   # Camada de Rede
   byte8 = 1
   byte10 = 0

   # Cria o vetor Pacote
   PacoteTX =[0]*52
   PacoteRX=[0]*52


   # Cria Pacote de 52 bytes com valor zero em todas as posições
   for i in range(52): # faz um array com 52 bytes
      PacoteTX[i] = 0
      PacoteRX[i] = 0

   # Camada de Aplicação
   PacoteTX[16] = 16
   PacoteTX[17] = 17
   PacoteTX[18] = 18
   PacoteTX[34] = byte34
   PacoteTX[37] = byte37
   PacoteTX[40] = byte40

   # Camada de rede
   PacoteTX[8] = int (byte8) #origem
   PacoteTX[10] = int (byte10) #destino

   #inicializa variáveis auxiliares
   w = int(num_medidas)+1
   i = 0

# param_n6_n3 = open(os.path.join(os.path.dirname(__file__), '../NIVEL_4/PARAMETROS_N6-N3.txt'), 'r') # leitura do arquivo de comandos
# condicao_limpeza_arquivos = int(param_n6_n3.readline())
# param_n6_n3.close()

# while condicao_limpeza_arquivos != 1:
#    param_n6_n3 = open(os.path.join(os.path.dirname(__file__), '../NIVEL_4/PARAMETROS_N6-N3.txt'), 'r') # leitura do arquivo de comandos
#    comando = param_n6_n3.readline()
#    if (comando != ''):
#       condicao_limpeza_arquivos = int(comando)
#    param_n6_n3.close()


         # while byte34 != 1:
         #    param_n6_n1 = open(os.path.join(os.path.dirname(__file__), '../NIVEL_4/PARAMETROS_N6-N1.txt'), 'r') # leitura do arquivo de comandos
         #    comando = param_n6_n1.readline()
         #    if (comando != ''):
         #       byte34 = int(comando)
         #    param_n6_n1.close()

   try:
      # ============ Camada Física - Transmite o pacote        
      for j in range(1,w):

         
         
         # ==== Camada de Transporte contagem de pacotes de descida
         PKTdown += 1
         contador_DL += 1
         if PKTdown == 256:
            PKTdown = 0
         byte13 = PKTdown
         PacoteTX[12] = int(byte12)
         PacoteTX[13] = int(byte13)

      # ============= Camada de Aplicação comandos para a placa
         param_n6_n1 = open(os.path.join(os.path.dirname(__file__), '../NIVEL_4/PARAMETROS.txt'), 'r') # leitura do arquivo de comandos
         byte34 = int(param_n6_n1.readline())
         param_n6_n1.close()

         PacoteTX[34] = byte34
         # PacoteTX[37] = byte37
         # PacoteTX[40] = byte40            
         # PacoteTX[43] = byte43


      # ============= CAMDA FÍSICA TRANSMITE O PACOTE            
      ##            for k in range(52): # transmite pacote
      ##               TXbyte = chr(PacoteTX[k])
      ##               udp.sendto (bytes(PacoteTX[k]), Sensor) #Envio do Pacote por Socket udp
      ##               print(TXbyte.encode('latin1'))
         udp.sendto (bytes(PacoteTX), Sensor) #Envio do Pacote por Socket udp
      ##               ser.write(TXbyte.encode('latin1'))

         
         # Aguarda a resposta do sensor
         #time.sleep(0.1)
         

      # ============= Camada Física - Recebe o pacote
      ##            Pacote_RX = ser.read(52) # faz a leitura de 52 bytes do buffer que recebe da serial pela COM
         try:
            Pacote_RX, cliente = udp.recvfrom(1024)  # Recebe pacote do Socket
         except socket.timeout as e: # trata erro
            Pacote_RX = [0]
   ##         udp.close()
   ##         udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   ##         udp.settimeout(0.5)
   ##         udp.bind(orig)
   ##         time.sleep(0.5)
   ##         print(bytes(PacoteTX))
            pass

         if len(Pacote_RX) == 52:
            # RSSI Uplink
            byte0 = Pacote_RX[0]
            if byte0 > 128:
               RSSIu = ((byte0-256)/2.0)-74
            else:
               RSSIu = (byte0/2.0)-74
            # RSSI Downlink
            byte2 = Pacote_RX[2]
            if byte2 > 128:
               RSSId = ((byte2-256)/2.0)-74
            else:
               RSSId = (byte2/2.0)-74

      # ============= Camada MAC
            byte4 = Pacote_RX[4]
            byte5 = Pacote_RX[5]
            byte6 = Pacote_RX[6]
            byte7 = Pacote_RX[7]

      # ============= Camada Rede
            byte8 = Pacote_RX[8]
            byte9 = Pacote_RX[9]
            byte10 = Pacote_RX[10]
            byte11 = Pacote_RX[11]
            
      # ============= Camada Transporte

            byte12 = Pacote_RX[12]
            byte14 = Pacote_RX[14]
            byte15 = Pacote_RX[15]
            PKTup = byte15
            contador_UL+=1 

      # ============= Camada Aplicação
            luminosidade = 1023 -(Pacote_RX[17]*256+ Pacote_RX[18])
            #byte17 = ((Pacote_RX[17]*256+ Pacote_RX[18])/100.0)
            Status_VERDE = Pacote_RX[34]
            Status_AMARELO = Pacote_RX[37]
            Status_VERMELHO = Pacote_RX[40]

            if (falha_na_comunicacao == True):
               # Tratamento de overflow
               if (ultimo_pacote_UL + perdas_parciais > 255):
                  print("OVERFLOW: ", PKTup, ultimo_pacote_UL)
                  # PKTup_esperado = ultimo_pacote_UL + perdas_parciais - 255
                  if (PKTup > ultimo_pacote_UL):
                     perdas_DL_parciais += PKTup - ultimo_pacote_UL + perdas_parciais - 1
                  else:
                     perdas_DL_parciais += perdas_parciais - ((PKTup + 255) - ultimo_pacote_UL)
                  
                  perdas_UL_parciais += perdas_parciais - perdas_DL_parciais
               else:
                  perdas_UL_parciais += PKTup - ultimo_pacote_UL - 1
                  perdas_DL_parciais += perdas_parciais - perdas_UL_parciais
                  
               # contador_UL = contador_UL + perdas_UL
               perdas_UL_totais += perdas_UL_parciais
               perdas_DL_totais += perdas_DL_parciais
               contador_UL += perdas_UL_parciais

               falha_na_comunicacao = False
               perdas_parciais = 0
               perdas_UL_parciais = 0
               perdas_DL_parciais = 0

            ultimo_pacote_UL = PKTup

            PSR_DL = (1 - (perdas_DL_totais/contador_DL)) * 100
            PSR_UL = (1 - (perdas_UL_totais/contador_UL)) * 100
            

            # print ('Cont = ', j,' RSSI = ', RSSId,' PSR DL = ', PSR_DL, ' PSR UL = ', PSR_UL, 'VERDE= ',Status_VERDE,' AMARELO= ',Status_AMARELO, 'VERMELHO=',Status_VERMELHO)
            print (' Cont = ', j,' RSSI = ', RSSId,' PSR DL = ', PSR_DL, ' PSR UL = ', PSR_UL, '\n',
                     ' Perdas totais:', perdas_totais,' Perdas parciais:', perdas_parciais, '\n',
                     ' Contador DL:',contador_DL, ' Contador UL:',contador_UL)

            # Salva no arquivo de log
            print (time.asctime(),';',j,';',RSSId,';',PSR_DL,';',PSR_UL, file=LOG_gerencia)

            Gerencia = open(filename2, 'a+')
            print (j,';',RSSId,';',PSR_DL,';',PSR_UL, file=Gerencia)
            Gerencia.close()

      
         else: #Caso perda de pacote
            perdas_parciais+=1
            perdas_totais+=1
            falha_na_comunicacao = True
            # perda_PK_RX = perda_PK_RX+1
            # PSR = round((1-(perda_PK_RX / j))*100,2)
            # print ('Cont = ', j,' RSSI = -- PSR = ', PSR, ' Status do LED do NodeMCU = -- Status do LED do Esp = --')
            
            # # Salva no arquivo de log
            # print (time.asctime(),';',j,';;',PSR,';;',file=LOG_gerencia)
            # Medidas = open(filename2, 'a+')
            # print (j,';;',PSR,file=Medidas)
            # Medidas.close()
         
         if(byte34 == 0):
            break

      print ('Fim da Execução')  # escreve na tela
      grava_comandos(0)

      time.sleep(0.5)
      abstracao_rssi = [0]*8
      file_abstracao = open(os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_abstracao.txt'), 'r') # leitura do arquivo de comandos
      # file_abstracao.flush()
      index = 0
      for line in file_abstracao:
         line=line.strip()
         abstracao_rssi[index] = str(round(float(line)*100)/100)
         index+=1
      file_abstracao.close()

      print("RSSI MAXIMA;RSSI MINIMA;RSSI MEDIA;DESV_PAD_RSSI", file=LOG_gerencia)
      print(abstracao_rssi[0],";",abstracao_rssi[1],";",abstracao_rssi[2],";",abstracao_rssi[3], file=LOG_gerencia)
      print ('Pacotes enviados = ',j,' Pacotes perdidos = ',perda_PK_RX)
      LOG_gerencia.close()


   except KeyboardInterrupt:
      LOG_gerencia.close()
      udp.close()

ultima_condicao_start = 0 

while True:
   param_n6_n1 = open(os.path.join(os.path.dirname(__file__), '../NIVEL_4/PARAMETROS.txt'), 'r')
   condicao_start = param_n6_n1.readline()
   if (condicao_start != ''):
      condicao_start = int(condicao_start)
   
   num_medidas = param_n6_n1.readline()
   param_n6_n1.close()

   if(condicao_start != ultima_condicao_start and condicao_start == 1):
      Gerencia = open(filename2, 'w').close()
      reiniciar_psr()
      time.sleep(0.2)
   
   if(condicao_start == 1):
      leitura_socket(num_medidas)

   ultima_condicao_start = condicao_start
   # if KeyboardInterrupt:
   #    LOG_gerencia.close()
   #    udp.close()
   #    print("Interrupcao por tecla pressionada")
   #    break

''' SIGNIFICADO DOS BYTES DO PACOTE DE DESCIDA
byte0
byte1
byte2
byte3
byte4
byte5
byte6
byte7
byte8
byte9
byte10
byte11
byte12
byte13
byte14
byte15
byte16
byte17
byte18
byte19
byte20
byte21
byte22
byte23
byte24
byte25
byte25
byte26
byte27
byte28
byte29
byte30
byte31
byte32
byte33
byte34
byte35
byte36
byte37
byte38
byte39
byte41
byte42
byte43
byte44
byte45
byte46
byte47
byte49
byte49
byte50
byte51
'''
