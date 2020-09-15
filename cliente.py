import tkinter
from tkinter import * 
import socket 
import sys
import threading
import time 


#crea ventana
ventana=tkinter.Tk()
ventana.geometry("563x432")

#icono para la ventana grafica 
#ventana.iconbitmap("otacon.ico")
#------------no funciona por alguna razon --------------

	

#titulo de la ventana 
ventana.title("Pychat GUI V.0.2")

#fondo de pantalla otacon
fondo=PhotoImage(file="base_real.png")
imagen=Label(ventana,image=fondo).place(x=0,y=0)

#letras en pantalla :
nombre=tkinter.Label(ventana,text="Pychat GUI V.0.2").place(x=200,y=10)

#para sacar los mensajes de la caja 
my_msj=tkinter.StringVar()

#caja de entrada :
escribe_tu_msg=tkinter.Label(ventana,text="escribe tu mensaje aca :",bg="gray").place(x=22,y=280)
caja_entrada=tkinter.Entry(ventana,borderwidth=0,width=62,textvariable=my_msj)
caja_entrada.place(x=22,y=300)



#nombre de usuario

Name="usuario"
def name_change():
	
	global Name
	if Names.get() !="":
		Name=Names.get()
	else:
		Name="usuario"
	print(Name)


def quien_eres():
	global Names
	Names=tkinter.StringVar()
	print(Names)
	quien=tkinter.Tk()
	print(Names)
#	quien.transient(ventana)
	quien.title("usuario")
	usuarioN=tkinter.Label(quien,text="usuario").place(x=50,y=10)
	print(Names)
#	Names=tkinter.StringVar()
	entrada_N=tkinter.Entry(quien,textvariable=Names).place(x=20,y=60)
	print(Names)
	nombre_N=tkinter.Button(quien,text="cambia el nombre",command=lambda:name_change()).place(x=20,y=90)
	print(Names)

	quien.mainloop()

#	quien.geometry("250,200")



#extraer el texto de la caja de entrada 
def texto_salida():
	print("chat-cliente GUI con base a python \n by red_wolf 2020 ")
	texto=Name+" >>>"+my_msj.get()

	print(texto)
	my_msj.set("")
	caja_salida.insert(tkinter.END,texto)

#barra para moverte a travez de los mensajes 
barra=tkinter.Scrollbar()
barra.place(x=310,y=230)


#caja de salida :
caja_salida=tkinter.Listbox(height=12,width=43,bg="gray",borderwidth=0,yscrollcommand=barra.set)
caja_salida.place(x=18,y=57)




#boton de envio :
envio=tkinter.Button(ventana,text="Enviar",padx=10,pady=14,bg="red",command=lambda:texto_salida())
envio.place(x=465,y=280)

#animacion de otacon 
otacon=PhotoImage(file="otacon.png")
otakon=Label(ventana,image=otacon).place(x=400,y=50)

	
#usuario :
user=tkinter.Button(ventana,text="usuario",padx=8,pady=15,bg="blue",command=lambda:quien_eres())
user.place(x=465,y=335)




#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect((str(host), int(port)))

#msg_recv = threading.Thread(msg_recv)

#msg_recv.daemon = True
#msg_recv.start()


















#loop infinito que mantiene todo abierto
ventana.mainloop()