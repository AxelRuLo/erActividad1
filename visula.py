import tkinter as tk
import back as er
window = tk.Tk()
window.title("sintaxis")
window.geometry("500x500")
window.resizable(False, False)
window.config(bg="#D3C3C3")

# entrysvalue

verbo = tk.StringVar()
resultado = tk.StringVar()

# functions
def comprobar():
    oracion = verbo.get()
    # resultadoBack = back.recorrerOracion(oracion.lower())
    # if(resultadoBack):
    #     resultado.set("correcto")
    # else:
    #     resultado.set("incorrecto")
    

# labels
tk.Label(window,text="Activdad 1 expreciones regulares",font=('Calibri', 14),background="#D3C3C3").place(x=130,y=50)
tk.Label(window,text="validacion de correos electronicos",font=('Calibri', 14),background="#D3C3C3").place(x=130,y=100)
tk.Label(window,text="escribe el correo",font=('Calibri', 14),background="#D3C3C3").place(x=185,y=150)
tk.Label(window,text="el correo es",font=('Calibri', 14),background="#D3C3C3").place(x=200,y=250)
tk.Label(window,textvariable=resultado,font=('Calibri', 14),background="#D3C3C3").place(x=200,y=290)

# entrys

tk.Entry(window,textvariable=verbo,font=('Calibri', 14)).place(x=150,y=200)

# buton
tk.Button(window,font=('Calibri', 14),text="comprobar",command=comprobar,).place(x=200,y=380)


window.mainloop()