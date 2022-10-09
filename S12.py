from tkinter import*
import smtplib

ventana = Tk()
ventana.title('Mensajeria')
ventana.config(bg= "gray")


def enviar():
    try:
        username = usuario.get()
        password = contrasenia.get()
        to = para.get()
        subject = asunto.get()
        body = cuerpo.get()
        if(username=="" or password=="" or to=="" or subject=="" or body==""):
            alert.config(text="Todos los campos deben llenarse")
            return
        else:
            msj = 'Subject: {}\n\n{}'.format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, msj)
            alert.config(text="El mensaje se envio con exito...", fg="green")
    except Exception as e:
        alert.config(text="Error al enviar mensaje", fg="red")
        print(e)

def borrar():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    alert.destroy()


Label(ventana, text="Bienvenido... ", font=('Roboto', 14)).grid(row=0, sticky=N)
Label(ventana, text="Para enviar un correo llena los siguientes campos:", font=('Roboto',11)).grid(row=1, sticky=W, padx=5, pady=10)

Label(ventana, text="Correo:", font=('Roboto',11)).grid(row=2, sticky=W, padx=10)
Label(ventana, text="Contrase;a:", font=('Roboto',11)).grid(row=3, sticky=W, padx=10)
Label(ventana, text="Para:", font=('Roboto',11)).grid(row=4, sticky=W, padx=10)
Label(ventana, text="Asunto:", font=('Roboto',11)).grid(row=5, sticky=W, padx=10)
Label(ventana, text="Mensaje:", font=('Roboto',11)).grid(row=6, sticky=W, padx=10)


alert = Label(ventana, text="", font=('Roboto', 11), fg="red")
alert.grid(row=9, sticky=S)

usuario = StringVar()
contrasenia = StringVar()
para = StringVar()
asunto = StringVar()
cuerpo = StringVar()

entry1 = Entry(ventana, textvariable=usuario)
entry1.grid(row=2, column=0)
entry2 = Entry(ventana, textvariable=contrasenia)
entry2.grid(row=3, column=0)
entry3 = Entry(ventana, textvariable=para)
entry3.grid(row=4, column=0)
entry4 = Entry(ventana, textvariable=asunto)
entry4.grid(row=5, column=0)
entry5 = Entry(ventana, textvariable=cuerpo)
entry5.grid(row=6, column=0)

Button(ventana, command=enviar, text="Enviar").grid(row=8, sticky=W, pady=15, padx=25)
Button(ventana, command=borrar, text="Borrar").grid(row=8)

ventana.mainloop()