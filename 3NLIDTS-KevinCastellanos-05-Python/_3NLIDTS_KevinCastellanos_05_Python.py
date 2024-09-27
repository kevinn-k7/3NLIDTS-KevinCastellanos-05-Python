
import tkinter as tk
from tkinter import messagebox
import re

def sies_numero_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def sies_numero_decimal(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def sies_telefono_valido(valor):
    return valor.isdigit() and len(valor) == 10

def sies_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))


def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    var_genero.set(None)



def validar_entrada():
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    telefono = entry_telefono.get().strip()
    estatura = entry_estatura.get().strip()
    edad = entry_edad.get().strip()
    genero = var_genero.get()

    if not nombre or not apellido or not telefono or not estatura or not edad or not genero:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return False

    if not sies_texto_valido(nombre) or not sies_texto_valido(apellido):
        messagebox.showerror("Error", "El nombre y apellido solo deben contener letras.")
        return False

    if not sies_telefono_valido(telefono):
        messagebox.showerror("Error", "El teléfono debe contener 10 dígitos numericos.")
        return False

    if not sies_numero_entero(edad):
        messagebox.showerror("Error", "La edad debe ser un número entero.")
        return False

    if not sies_numero_decimal(estatura):
        messagebox.showerror("Error", "La estatura debe ser un número decimal.")
        return False

    return True


def guardar():
    if validar_entrada():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        estatura = entry_estatura.get()
        edad = entry_edad.get()
        genero = "Hombre" if var_genero.get() == "Hombre" else "Mujer"
        
        datos = f"Nombre: {nombre}\nApellido: {apellido}\nTeléfono: {telefono}\nEstatura: {estatura}\nEdad: {edad}\nGénero: {genero}\n"
        
        with open("FormularioDatos.txt", "a") as archivo:
            archivo.write(datos + "\n")
        
        messagebox.showinfo("Guardado", f"Datos guardados exitosamente:\n\n{datos}")
        limpiar_campos()


def cancelar():
    limpiar_campos()


ventana = tk.Tk()
ventana.title("Formulario Datos")
ventana.geometry("500x300")


tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Apellido:").grid(row=1, column=0)
entry_apellido = tk.Entry(ventana)
entry_apellido.grid(row=1, column=1)

tk.Label(ventana, text="Teléfono:").grid(row=2, column=0)
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=2, column=1)

tk.Label(ventana, text="Estatura (cm):").grid(row=3, column=0)
entry_estatura = tk.Entry(ventana)
entry_estatura.grid(row=3, column=1)

tk.Label(ventana, text="Edad:").grid(row=4, column=0)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=4, column=1)

tk.Label(ventana, text="Género:").grid(row=5, column=0)
var_genero = tk.StringVar(value=None)
tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value="Hombre").grid(row=5, column=1, sticky=tk.W)
tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value="Mujer").grid(row=5, column=1, sticky=tk.E)


btn_guardar = tk.Button(ventana, text="Guardar", command=guardar)
btn_guardar.grid(row=6, column=0)

btn_cancelar = tk.Button(ventana, text="Cancelar", command=cancelar)
btn_cancelar.grid(row=6, column=1)


ventana.mainloop()

