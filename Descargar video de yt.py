import tkinter as tk
from tkinter import simpledialog
from pytube import YouTube

root = tk.Tk()
root.configure(bg='#222222')
root.geometry("500x200")
root.title("Descarga de Video")

my_font = ('Arial', 14)

url_label = tk.Label(root, text="Ingresa la URL del video de YouTube", font=my_font, bg='#222222', fg='white')
url_entry = tk.Entry(root, font=my_font, bg='#333333', fg='white')

quality_label = tk.Label(root, text='''Elija la calidad de descarga escribiendo un número:
(0) Calidad BAJA (1) Calidad MEDIA (2) Calidad ALTA''', font=my_font, bg='#222222', fg='white')
quality_entry = tk.Entry(root, font=my_font, bg='#333333', fg='white')

download_button = tk.Button(root, text="Descargar", font=my_font, bg='#555555', fg='white', command=lambda: download(url_entry.get(), quality_entry.get()))

# Colocamos los widgets en la ventana
url_label.pack()
url_entry.pack()
quality_label.pack()
quality_entry.pack()
download_button.pack()

def download(url, quality):
    yt = YouTube(url)
    videos = yt.streams.filter(progressive=True).all()

    for i, video in enumerate(videos):
        print(i, video)

    video = videos[int(quality)]
    video.download()
    print("Video descargado con éxito")

root.mainloop()
