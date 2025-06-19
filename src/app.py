import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

from image_utils import (
    apply_grayscale,
    apply_invert,
    apply_mirror,
    apply_rotate,
    apply_brightness
)

class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Imágenes")
        self.root.geometry("900x650")

        self.image_paths = []
        self.index = 0
        self.current_image = None
        self.original_image = None

        self.image_label = tk.Label(self.root)
        self.image_label.pack(expand=True)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        tk.Button(self.button_frame, text="Seleccionar Imágenes", command=self.load_images).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Anterior", command=self.show_previous).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Siguiente", command=self.show_next).pack(side="left", padx=5)

        self.effects_frame = tk.Frame(self.root)
        self.effects_frame.pack(pady=10)

        tk.Button(self.effects_frame, text="Blanco y Negro", command=self.apply_bw).pack(side="left", padx=5)
        tk.Button(self.effects_frame, text="Invertir", command=self.apply_invert).pack(side="left", padx=5)
        tk.Button(self.effects_frame, text="Espejo", command=self.apply_mirror).pack(side="left", padx=5)
        tk.Button(self.effects_frame, text="Rotar 90°", command=self.apply_rotate).pack(side="left", padx=5)
        tk.Button(self.effects_frame, text="+ Brillo", command=lambda: self.adjust_brightness(1.3)).pack(side="left", padx=5)
        tk.Button(self.effects_frame, text="– Brillo", command=lambda: self.adjust_brightness(0.7)).pack(side="left", padx=5)
        tk.Button(self.effects_frame, text="Restaurar Original", command=self.restore_original).pack(side="left", padx=5)
        tk.Button(self.effects_frame, text="Guardar", command=self.save_image).pack(side="left", padx=5)

    def load_images(self):
        filetypes = [("Imágenes", "*.png *.jpg *.jpeg *.gif")]
        files = filedialog.askopenfilenames(title="Seleccionar imágenes", filetypes=filetypes)
        if files:
            self.image_paths = list(files)
            self.index = 0
            self.show_image()

    def show_image(self):
        if self.image_paths:
            try:
                image = Image.open(self.image_paths[self.index])
                self.original_image = image.copy()
                self.current_image = image
                self.display_image(image)
            except Exception as e:
                print("Error al cargar imagen:", e)
                messagebox.showerror("Error", f"No se pudo cargar la imagen:\n{e}")

    def display_image(self, image):
        image_resized = image.resize((800, 500), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image_resized)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def show_previous(self):
        if self.image_paths:
            self.index = (self.index - 1) % len(self.image_paths)
            self.show_image()

    def show_next(self):
        if self.image_paths:
            self.index = (self.index + 1) % len(self.image_paths)
            self.show_image()

    def apply_bw(self):
        if self.current_image:
            self.current_image = apply_grayscale(self.current_image)
            self.display_image(self.current_image)

    def apply_invert(self):
        if self.current_image:
            self.current_image = apply_invert(self.current_image)
            self.display_image(self.current_image)

    def apply_mirror(self):
        if self.current_image:
            self.current_image = apply_mirror(self.current_image)
            self.display_image(self.current_image)

    def apply_rotate(self):
        if self.current_image:
            self.current_image = apply_rotate(self.current_image)
            self.display_image(self.current_image)

    def adjust_brightness(self, factor):
        if self.current_image:
            self.current_image = apply_brightness(self.current_image, factor)
            self.display_image(self.current_image)

    def restore_original(self):
        if self.original_image:
            self.current_image = self.original_image.copy()
            self.display_image(self.current_image)

    def save_image(self):
        if self.current_image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg *.jpeg"), ("All files", "*.*")]
            )
            if file_path:
                try:
                    self.current_image.save(file_path)
                    messagebox.showinfo("Guardado", "Imagen guardada con éxito.")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo guardar la imagen.\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()
