import tkinter as tk

# 1. crear y configurar la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera App grafica")
ventana.geometry("350x250")  # Tamano: ancho x alto en pixeles

# 2. Texto de instruccion (Label)
instruccion = tk.Label(ventana, text="Escribe tu nombre abajo:", font=("Arial", 12))
instruccion.pack(pady=10)

# 3. Caja de entrada de texto (Entry)
caja_nombre = tk.Entry(ventana, font=("Arial", 12))
caja_nombre.pack(pady=5)

# 4. texto que cambiara cuando presiones el boton
resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))

# 5. funcion que se activa al presionar el boton
def saludar():
    nombre = caja_nombre.get() # Obtiene el texto escrito en la caja
    if nombre:
        resultado.config(text=f"Hola, {nombre}! Bienvenid@.")
    else:
        resultado.config(text="Porfavor escribe un nombre.")

# 6. Boton para ejecutar la funcion (Button)
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

# 7. Iniciar el bucle principal de la ventana
ventana.mainloop()

