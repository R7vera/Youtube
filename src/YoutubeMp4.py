
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import os

# Simular certificado SSL desactivando la verificación
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def descargar_video():
    url = url_entry.get()
    ruta_destino = os.path.join(os.getcwd(), "Musica")

    try:
        yt = YouTube(url)
        
        # Obtener la corriente (stream) que contiene un archivo mp4
        stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        
        # Descargar el video en formato mp4 en la ruta especificada
        stream.download(output_path=ruta_destino)
        
        messagebox.showinfo("Descarga completada", f"El video se ha descargado correctamente.\nSe guardó en: {ruta_destino}")
    except RegexMatchError:
        messagebox.showerror("Error", "No se pudo encontrar el video.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear ventana principal
root = tk.Tk()
root.title("Descargar video de YouTube")

# Crear y posicionar widgets
url_label = tk.Label(root, text="URL del video de YouTube:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

descargar_button = tk.Button(root, text="Descargar video", command=descargar_video)
descargar_button.pack()

# Ejecutar la interfaz
root.mainloop()
