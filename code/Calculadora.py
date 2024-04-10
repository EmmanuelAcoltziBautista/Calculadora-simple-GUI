'''
Creado por Emmanuel Acoltzi Bautista
Correo electronico: basedemma@gmail.com
Fecha de creacion: 09-04-2024

'''

#Importo la libreria para la interfaz
from tkinter import *

#creo un constructor osea para diseniar la GUI
class Constructor():
    def __init__(self,ventana):
        
        self.contenedor=""
        self.a=0
        self.b=0
        self.operador=""
        self.resultado=StringVar()
        #Esta es la caja de texto
        self.TEXTO1=Entry(ventana,text="",textvariable=self.resultado)
        #los botones
        self.BOTON1=Button(ventana,text="1",command=self.Boton1)
        self.BOTON2=Button(ventana,text="2",command=self.Boton2)
        self.BOTON3=Button(ventana,text="3",command=self.Boton3)
        self.BOTON4=Button(ventana,text="4",command=self.Boton4)
        self.BOTON5=Button(ventana,text="5",command=self.Boton5)
        self.BOTON6=Button(ventana,text="6",command=self.Boton6)
        self.BOTON7=Button(ventana,text="7",command=self.Boton7)
        self.BOTON8=Button(ventana,text="8",command=self.Boton8)
        self.BOTON9=Button(ventana,text="9",command=self.Boton9)
        self.BOTON0=Button(ventana,text="0",command=self.Boton0)
        self.BotonPunto=Button(ventana,text=".",command=self.BotonPunto)

#botones de los operadores
        self.BOTONSuma=Button(ventana,text="+",command=self.Suma)
        self.BOTONResta=Button(ventana,text="-",command=self.Resta)
        self.BOTONMultiplicacion=Button(ventana,text="X",command=self.Multiplicacion)
        self.BOTONDivicion=Button(ventana,text="/",command=self.Divicion)
        self.BOTONIgual=Button(ventana,text="=",command=self.Igual)
        #Pocicionamiento de cajas
        self.TEXTO1.place(x=5,y=5,width=100,height=30)
        self.BOTONSuma.place(x=10,y=40,width=20,height=20)
        self.BOTONResta.place(x=40,y=40,width=20,height=20)
        self.BOTONMultiplicacion.place(x=70,y=40,width=20,height=20)
        self.BOTONDivicion.place(x=100,y=40,width=20,height=20)
        self.BOTONIgual.place(x=130,y=40,width=20,height=20)

        #Numeros

        self.BOTON1.place(x=10,y=70,width=20,height=20)
        self.BOTON2.place(x=30,y=70,width=20,height=20)
        self.BOTON3.place(x=50,y=70,width=20,height=20)
        self.BOTON4.place(x=10,y=90,width=20,height=20)
        self.BOTON5.place(x=30,y=90,width=20,height=20)
        self.BOTON6.place(x=50,y=90,width=20,height=20)
        self.BOTON7.place(x=10,y=110,width=20,height=20)
        self.BOTON8.place(x=30,y=110,width=20,height=20)
        self.BOTON9.place(x=50,y=110,width=20,height=20)
        self.BOTON0.place(x=30,y=130,width=20,height=20)
        self.BotonPunto.place(x=50,y=130,width=20,height=20)

#Creo el funcionamiento de los botones
    def Boton1(self):
       #aqui recibo el texto
       var=self.TEXTO1.get()
       #y lo concateno
       self.contenedor+="1"
       #aqui lo agrego a la variable resultado que previamente defini
       self.resultado.set(self.contenedor)
       return 0
    
    def Boton2(self):
       var=self.TEXTO1.get()
       self.contenedor+="2"
       self.resultado.set(self.contenedor)
       return 0
    def Boton3(self):
       var=self.TEXTO1.get()
       self.contenedor+="3"
       self.resultado.set(self.contenedor)
       return 0
    def Boton4(self):
       var=self.TEXTO1.get()
       self.contenedor+="4"
       self.resultado.set(self.contenedor)

       return 0
    def Boton5(self):
       var=self.TEXTO1.get()
       self.contenedor+="5"
       self.resultado.set(self.contenedor)

       return 0
    def Boton6(self):
       var=self.TEXTO1.get()
       self.contenedor+="6"
       self.resultado.set(self.contenedor)

       return 0
    def Boton7(self):
       var=self.TEXTO1.get()
       self.contenedor+="7"
       self.resultado.set(self.contenedor)

       return 0
    def Boton8(self):
       var=self.TEXTO1.get()
       self.contenedor+="8"
       self.resultado.set(self.contenedor)

       return 0
    def Boton9(self):
       var=self.TEXTO1.get()
       self.contenedor+="9"
       self.resultado.set(self.contenedor)

       return 0
    def Boton0(self):
       var=self.TEXTO1.get()
       self.contenedor+="0"
       self.resultado.set(self.contenedor)
       return 0
    def BotonPunto(self):
       var=self.TEXTO1.get()
       self.contenedor+="."
       self.resultado.set(self.contenedor)

       return 0

#si toca el boton de la suma
    def Suma(self):
        self.operador="+"
        "solo agregamos el operador"
        self.a=float(self.TEXTO1.get())
        #redifinimos las variables
        self.resultado.set("")
        self.contenedor=""

        return 0
    def Resta(self):
        self.operador="-"
        self.a=float(self.TEXTO1.get())
        self.resultado.set("")
        self.contenedor=""
        return 0
    def Multiplicacion(self):
        self.operador="*"
        self.a=float(self.TEXTO1.get())
        self.resultado.set("")
        self.contenedor=""
        return 0
    def Divicion(self):
        self.operador="/"
        self.a=float(self.TEXTO1.get())
        self.resultado.set("")
        self.contenedor=""
        return 0
    



  #si presiona el boton de igual  
    def Igual(self):
        self.contenedor=""
#        self.resultado.set("")
        self.b=float(self.TEXTO1.get())
        c=0
        #recupero valores
        print("a:",self.a)
        print("b:",self.b)
        #ubico el operador para realizar la operacion para asignar a c
        if self.operador=="+":
          c=self.a+self.b
        if self.operador=="-":
          c=(self.a)-(self.b)
        if self.operador=="*":
          c=self.a*self.b
        if self.operador=="/":
          c=self.a/self.b
          
#          agrego a c el resultado de la operacion
        self.resultado.set(c)
        print(c)
        
        #print("resultado: ",self.resultado)
        #self.resultadoE.set(c)
        return 0

#aqui solo creo la interfaz gradica
ventana=Tk()
ventana.title("Calculadora")
#ventana.resizable(width=none,height=none)
llamado=Constructor(ventana)
ventana.mainloop()
        
        