import tkinter
from tkinter import *
import tkinter.messagebox as tkMessageBox
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os
import math

#----------------------------- CRIAÇÃO DA JANELA PRINCIPAL ---------------------
janela_principal=Tk() # Criando a tela principal, usando um objeto TKinter
janela_principal.title("FEE230 | Wireless Site Survey") # Função para alterar titulo da janela
janela_principal.geometry('1000x780') # Define o tamanho da janela
janela_principal.resizable(True, True) # Possibilita o redimensionamento da janela principal
#-------------------------------------------------------------------------------

#------------------------- CRIAÇÃO DA REGIÃO DE PARAMETRIZAÇÃO -----------------
reg_parametrizacao = Frame(master=janela_principal,borderwidth=1, relief='sunken') #cria um janela no rodapé da janela, define como master a janela principal(raiz)
reg_parametrizacao.place(x=10,y=10,width=300,height=350) #posiciona e define o tamanho dos janelas

titulo_parametrizacao = Label(reg_parametrizacao, font=("Arial", 14, "bold"),text = "CONFIGURAÇÕES",padx=5,pady=5).pack(side=TOP, anchor="n")
#-------------------------------------------------------------------------------

#---------------------- CRIAÇÃO DO INTERVALO DE MEDIDAS ------------------------
intervalo = Label(reg_parametrizacao, text = "Qtde. de Medidas", font=("Arial", 12))
intervalo.place(x=20,y=50)
valor_intervalo=Entry(reg_parametrizacao, width=10, font=("Arial", 12))
valor_intervalo.place(x=170,y=50)
valor_intervalo.insert(0, "0")

qtde_media_movel = Label(reg_parametrizacao, text = "N da Média Móvel", font=("Arial", 12))
qtde_media_movel.place(x=20,y=80)
valor_n_mm=Entry(reg_parametrizacao, width=10, font=("Arial", 12))
valor_n_mm.place(x=170,y=80)
valor_n_mm.insert(0, "5")

def captura_num_medidas():
    num_medidas = int(valor_intervalo.get())
    if(num_medidas == 0):
         num_medidas = 1000000

    return int(num_medidas)

def captura_num_mm():
    num_mm = int(valor_n_mm.get())
    if(num_mm == 0):
         num_mm = 5
         valor_n_mm.insert(0, "5")

    return int(num_mm)

#-------------------------------------------------------------------------------

#------------------------ CRIAÇÃO DA REGIÃO DE LIMIAR --------------------------
limiares = Label(reg_parametrizacao, text = "---------------------Limiares---------------------", font=("Arial", 12))
limiares.place(x=10, y=110)

# Limiar de RSSI Excelente
texto_limiar_otimo_rssi = Label(reg_parametrizacao, text = "RSSI Excelente >=", font=("Arial", 12))
texto_limiar_otimo_rssi.place(x=10, y=150)
limiar_otimo_rssi=Entry(reg_parametrizacao, width=5, font=("Arial", 12))
limiar_otimo_rssi.place(x=150,y=150)
limiar_otimo_rssi.insert(0, "-60")
Label(reg_parametrizacao, text = "dBm", font=("Arial", 12)).place(x=200,y=150)

# Limiar de RSSI Ruim
texto_limiar_ruim_rssi = Label(reg_parametrizacao, text = "RSSI Ruim         <=", font=("Arial", 12))
texto_limiar_ruim_rssi.place(x=10, y=180)
limiar_ruim_rssi=Entry(reg_parametrizacao, width=5, font=("Arial", 12))
limiar_ruim_rssi.place(x=150,y=180)
limiar_ruim_rssi.insert(0, "-80")
Label(reg_parametrizacao, text = "dBm", font=("Arial", 12)).place(x=200,y=180)

# Limiar de PSR Excelente
texto_limiar_otimo_psr = Label(reg_parametrizacao, text = "PSR Excelente >=", font=("Arial", 12))
texto_limiar_otimo_psr.place(x=10, y=220)
limiar_otimo_psr=Entry(reg_parametrizacao, width=5, font=("Arial", 12))
limiar_otimo_psr.place(x=150,y=220)
limiar_otimo_psr.insert(0, "90")
Label(reg_parametrizacao, text = "%", font=("Arial", 12)).place(x=200,y=220)

# Limiar de RSSI Ruim
texto_limiar_ruim_psr = Label(reg_parametrizacao, text = "PSR Ruim         <=", font=("Arial", 12))
texto_limiar_ruim_psr.place(x=10, y=250)
limiar_ruim_psr=Entry(reg_parametrizacao, width=5, font=("Arial", 12))
limiar_ruim_psr.place(x=150,y=250)
limiar_ruim_psr.insert(0, "50")
Label(reg_parametrizacao, text = "%", font=("Arial", 12)).place(x=200,y=250)
#-------------------------------------------------------------------------------

#------------------------------ GRAVACAO DOS COMANDOS --------------------------
def grava_comandos(condicao_start):
    arquivo_txt = os.path.join(os.path.dirname(__file__), '../NIVEL_4/PARAMETROS.txt') # está dando nome para o arquivo txt
    s = open(arquivo_txt,'w')
    s.write(str(condicao_start)+"\n")
    s.write(str(captura_num_medidas())+"\n")
    s.write(str(captura_num_mm())+"\n")
    s.close()
#-------------------------------------------------------------------------------

#------------------------------ CRIAÇÃO DO BOTÃO -------------------------------
global valor_otimo_rssi, valor_ruim_rssi, valor_otimo_psr, valor_ruim_psr
valor_otimo_rssi = -60.0
valor_ruim_rssi  = -80.0
valor_otimo_psr = 90
valor_ruim_psr = 50

def iniciar_teste():
    num_medidas = valor_intervalo.get()
    if(num_medidas == 0):
         num_medidas = 1000000
    global valor_otimo_rssi, valor_ruim_rssi, valor_otimo_psr, valor_ruim_psr
    valor_otimo_rssi = float(limiar_otimo_rssi.get())
    valor_ruim_rssi  = float(limiar_ruim_rssi.get())

    valor_otimo_psr = float(limiar_otimo_psr.get())
    valor_ruim_psr = float(limiar_ruim_psr.get())
    grava_comandos(1)

bot_ini_teste=Button(reg_parametrizacao,text="INICIAR TESTE",font=("Arial", 14, "bold"), width=20,command=iniciar_teste)
bot_ini_teste.place(x=25,y=295)
bot_ini_teste.config(state="normal")
#-------------------------------------------------------------------------------

#------------------------- CRIAÇÃO DA REGIÃO DE DESEMPENHO ---------------------
reg_desempenho = Frame(master=janela_principal,borderwidth=1, relief='sunken') #cria um janela no rodapé da janela, define como master a janela principal(raiz)
reg_desempenho.place(x=10,y=370,width=300,height=240) #posiciona e define o tamanho dos janelas

titulo_desempenho = Label(reg_desempenho, font=("Arial", 14, "bold"),text = "DESEMPENHO DA REDE",padx=5,pady=5).pack(side=TOP, anchor="n")


abstracao_rssi = ["0"]*8
global media_movel_rssi
media_movel_rssi = []

string_max_rssi = StringVar()
string_min_rssi = StringVar()
string_media_rssi = StringVar()
string_desv_pad_rssi = StringVar()
string_psr_dl = StringVar()
string_psr_ul = StringVar()

label_max_rssi = Label(reg_desempenho, font=("Arial", 12),textvariable = string_max_rssi,padx=5,pady=5)
label_max_rssi.place(x=5, y=50)

label_min_rssi = Label(reg_desempenho, font=("Arial", 12),textvariable = string_min_rssi,padx=5,pady=5)
label_min_rssi.place(x=5, y=80)

label_media_rssi = Label(reg_desempenho, font=("Arial", 12),textvariable = string_media_rssi,padx=5,pady=5)
label_media_rssi.place(x=5, y=110)

label_desv_pad_rssi = Label(reg_desempenho, font=("Arial", 12),textvariable = string_desv_pad_rssi,padx=5,pady=5)
label_desv_pad_rssi.place(x=5, y=140)

label_psr_dl = Label(reg_desempenho, font=("Arial", 12),textvariable = string_psr_dl,padx=5,pady=5)
label_psr_dl.place(x=5, y=170)
label_psr_ul = Label(reg_desempenho, font=("Arial", 12),textvariable = string_psr_ul,padx=5,pady=5)
label_psr_ul.place(x=5, y=200)
#-------------------------------------------------------------------------------

#------------------------- CRIAÇÃO DA REGIÃO DE FALHA --------------------------
reg_falha = Frame(master=janela_principal,borderwidth=1, relief='sunken') #cria um janela no rodapé da janela, define como master a janela principal(raiz)
reg_falha.place(x=10,y=620,width=300,height=150) #posiciona e define o tamanho dos janelas

titulo_falha = Label(reg_falha, font=("Arial", 14, "bold"),text = "FALHA",padx=5,pady=5).pack(side=TOP, anchor="n")

string_status_rssi = StringVar()
string_status_psr_dl = StringVar()
string_status_psr_ul = StringVar()

C = Canvas(reg_falha, height=120, width=300)

global rssi_color, rssi_text, psr_color_dl, psr_color_ul, psr_text_dl, psr_text_ul

def atualiza_falha():
    global rssi_color, rssi_text, psr_color_dl, psr_color_ul, psr_text_dl, psr_text_ul
    rssi_color="green"
    rssi_text ="Ótima"
    psr_color_dl="green"
    psr_color_ul="green"
    psr_text_dl="Ótima"
    psr_text_ul="Ótima"
    # print(abstracao_rssi[2])
    if (float(abstracao_rssi[2]) < float(valor_otimo_rssi) and float(abstracao_rssi[2]) > float(valor_ruim_rssi)):
        rssi_color="yellow"
        rssi_text="Satisfatória"
    elif (float(abstracao_rssi[2]) <= float(valor_ruim_rssi)):
        rssi_color="red"
        rssi_text="Ruim"

    if (float(abstracao_rssi[4]) < float(valor_otimo_psr) and float(abstracao_rssi[4]) > float(valor_ruim_psr)):
        psr_color_dl="yellow"
        psr_text_dl="Satisfatória"
    elif (float(abstracao_rssi[4]) <= float(valor_ruim_psr)):
        psr_color_dl="red"
        psr_text_dl="Ruim"

    if (float(abstracao_rssi[5]) < float(valor_otimo_psr) and float(abstracao_rssi[5]) > float(valor_ruim_psr)):
        psr_color_ul="yellow"
        psr_text_ul="Satisfatória"
    elif (float(abstracao_rssi[5]) <= float(valor_ruim_psr)):
        psr_color_ul="red"
        psr_text_ul="Ruim"


    C.create_oval(20,10,40,30,fill=rssi_color)
    texto_sobre_rssi = Label(reg_falha, font=("Arial", 12),textvariable = string_status_rssi,padx=5,pady=5)
    texto_sobre_rssi.place(x=50, y=40)
    string_status_rssi.set("A RSSI Média está " + rssi_text)

    C.create_oval(20,45,40,65,fill=psr_color_dl)
    texto_sobre_psr_dl = Label(reg_falha, font=("Arial", 12),textvariable = string_status_psr_dl,padx=5,pady=5)
    texto_sobre_psr_dl.place(x=50, y=75)
    string_status_psr_dl.set("A PSR DL está " + psr_text_dl)

    C.create_oval(20,80,40,100,fill=psr_color_ul)
    texto_sobre_psr_ul = Label(reg_falha, font=("Arial", 12),textvariable = string_status_psr_ul,padx=5,pady=5)
    texto_sobre_psr_ul.place(x=50, y=110)
    string_status_psr_ul.set("A PSR UL está " + psr_text_ul)
    C.pack()
# C.grid()
# C.place()

#-------------------------------------------------------------------------------

#---------------------------- CRIAÇÃO DA REGIÃO DE GRÁFICO ---------------------
reg_grafico = Frame(master=janela_principal,borderwidth=1, relief='sunken') #cria um janela no rodapé da janela, define como master a janela principal(raiz)
reg_grafico.place(x=320,y=10,width=670,height=740) #posiciona e define o tamanho dos janelas
#-------------------------------------------------------------------------------

#----------------------------- CRIAÇÃO DO GRÁFICO DE RSSI ----------------------
style.use("ggplot")

def grafico_rssi(f,c):
        global s1
        global valor_otimo_rssi, valor_ruim_rssi, valor_otimo_psr, valor_ruim_psr
        global rssi_color, rssi_text, psr_color_dl, psr_color_ul, psr_text_dl, psr_text_ul, media_movel_rssi

        f.clear()
    
        x = []
        y = []
        z= []
        psr_dl=[]
        psr_ul=[]
        media_movel_rssi= []
        dados = open(os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_gerencia.txt'),'r')
        for line in dados:
            line=line.strip()
            Y = line.split(';')
            y.append(Y)

        for i in range(len(y)):
            if((y[i][1])!='')and((y[i][2])!=''):
                x.append(float(y[i][1]))
                psr_dl.append(float(y[i][2]))
                psr_ul.append(float(y[i][3]))
                z.append(int(y[i][0]))
        
        if (len(x) > captura_num_mm()):
            for i in range(len(x) - captura_num_mm() + 1):
                rssi_w = [10**(i/10) for i in x]
                janela = rssi_w[i : i + captura_num_mm()]
                media_rssi_w = sum(janela)/captura_num_mm()
                media_rssi_dbm = 10*math.log(media_rssi_w,10)
                media_movel_rssi.append(media_rssi_dbm)
                # print(media_movel_rssi)media_rssi_dbm

        axis = f.add_subplot(211)
        # media_movel_rssi.append(abstracao_rssi[2])
        # print(len(media_movel_rssi))
        axis.plot(z,x,label='RSSI')
        axis.plot(media_movel_rssi,label='Média Móvel')
        axis.set_ylabel('RSSI (dBm)')
        axis.axhline(y=valor_otimo_rssi, color='green', linestyle='dashed',xmin=0.0, xmax=20.0)
        axis.axhline(y=valor_ruim_rssi, color='black', linestyle='dashed',xmin=0.0, xmax=20.0)
        

        axis1 = f.add_subplot(212)
        axis1.plot(z,psr_dl,label='PSR DL')
        axis1.plot(z,psr_ul,label='PSR UL')
        axis1.set_ylim([0,105])
        # axis1.set_xlim([0,50])
        axis1.legend()
        axis1.set_ylabel('PSR(%)')
        axis1.axhline(y=valor_otimo_psr, color='green', linestyle='dashed',xmin=0, xmax=40)
        axis1.axhline(y=valor_ruim_psr, color='black', linestyle='dashed',xmin=0, xmax=40)

        file_abstracao = open(os.path.join(os.path.dirname(__file__), '../NIVEL_4/dados_abstracao.txt'), 'r') # leitura do arquivo de comandos
        index = 0
        for line in file_abstracao:
            line=line.strip()
            abstracao_rssi[index] = str(round(float(line)*100)/100)
            index+=1
        file_abstracao.close()

        # axis.axhline(y=float(abstracao_rssi[2]), color='blue', linestyle=":", xmin=0.0, xmax=20.0, label="RSSI Média")
        axis.legend()
        # print(abstracao_rssi[2])
        string_max_rssi.set("RSSI Máxima = " + abstracao_rssi[0] + " dBm")
        string_min_rssi.set("RSSI Mínima = " + abstracao_rssi[1] + " dBm") 
        string_media_rssi.set("RSSI Média = " + abstracao_rssi[2] + " dBm")
        string_desv_pad_rssi.set("Desv. Pad. da RSSI = " + abstracao_rssi[3] + " dBm")
        string_psr_dl.set("PSR DL: " + abstracao_rssi[4] + "%")
        string_psr_ul.set("PSR UL: " + abstracao_rssi[5] + "%")
        atualiza_falha()

# =====================================================
        f.subplots_adjust(left=0.12, bottom=0.09, right=0.7, top=0.95, wspace=None, hspace=None)
        c.draw()
        dados.close()
        janela_principal.after(800, grafico_rssi,f,c)

def callback():
    if tkMessageBox.askokcancel("Sair", "Tem certeza que deseja sair?"):
        # Interrompe a transmissão de dados
        grava_comandos(0)
        janela_principal.destroy()

fig = Figure(figsize=(9, 7.5), facecolor='white')
canvas = FigureCanvasTkAgg(fig, master=reg_grafico)
canvas.get_tk_widget().grid(row=3, column=1, columnspan=3, sticky='NSEW')
grafico_rssi(fig,canvas)  

#-------------------------------- RODA A JANELA PRINCIPAL ----------------------
janela_principal.protocol("WM_DELETE_WINDOW", callback)
janela_principal.mainloop()
janela_principal.update_idletasks()