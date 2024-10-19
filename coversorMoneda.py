import tkinter as tk
from tkinter import messagebox

#Tasa de conversion Dolar a Colones del dia 18 de octubre del 2024
tasaConversion = 513.70

# Conversion (Caso I)
def convertirCRC():
    try:
        # Obtener el valor ingresado por el usuario
        montoUSD = float(entradaUSD.get())
        
        # Operacion de la conversion
        montoCRC = montoUSD * tasaConversion
        
        # Mostrar de la convercion
        etiquetaResultado.config(text=f"{montoCRC:.2f} CRC (Colones)")
    except ValueError:
        # Mostrar mensaje de error si el valor ingresado no es válido (Caso II)
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

# limpiat terminal
def limpiar():
    entradaUSD.delete(0, tk.END)
    etiquetaResultado.config(text="")

# Cerrar ventana (Caso III)
def confirmarSalida():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres cerrar la aplicación?"):
        ventana.destroy()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Moneda USD a CRC")
ventana.geometry("400x200")
ventana.protocol("WM_DELETE_WINDOW", confirmarSalida)

# Entrada de monto en USD
etiquetaUsd = tk.Label(ventana, text="Ingrese monto en USD:")
etiquetaUsd.grid(row=0, column=0, padx=10, pady=10)

entradaUSD = tk.Entry(ventana)
entradaUSD.grid(row=0, column=1, padx=10, pady=10)

# Botón para realizar la conversión
botonConvertir = tk.Button(ventana, text="Convertir", command=convertirCRC)
botonConvertir.grid(row=1, column=0, padx=10, pady=10)

# Botón para limpiar los campos
botonLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
botonLimpiar.grid(row=1, column=1, padx=10, pady=10)

# Etiqueta para mostrar el resultado
etiquetaResultado = tk.Label(ventana, text="")
etiquetaResultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la ventana
ventana.mainloop()