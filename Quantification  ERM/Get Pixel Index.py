import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def get_pixel_index(event):
    x, y = event.x, event.y
    pixel_color = image.getpixel((x, y))
    pixel_index = f"픽셀 위치: ({x}, {y}), 색상 값: {pixel_color}"
    index_label.config(text=pixel_index)

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global image
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        image_label.pack()
        canvas.config(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("이미지 클릭 및 픽셀 인덱스 확인")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

image_label = tk.Label(canvas)
index_label = tk.Label(root, text="", font=("Arial", 12))
index_label.pack()

open_button = tk.Button(root, text="이미지 열기", command=open_image)
open_button.pack()

canvas.bind("<Button-1>", get_pixel_index)

root.mainloop()
