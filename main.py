import tkinter as tk
from model.pixelartmodel import PixelArtModel
from view.pixelartview import PixelArtView
from controller.pixelartcontroller import PixelArtController


class PixelArtApp:
    def __init__(self, root):
        self.model = PixelArtModel(100, 100, 10)
        self.view = PixelArtView(root, self.model)
        self.controller = PixelArtController(self.model, self.view)

        self.create_menu(root)

    def create_menu(self, root):
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        color_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Колір", menu=color_menu)
        color_menu.add_command(label="Вибрати колір", command=self.controller.choose_color)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Відкрити", command=self.controller.open_image)
        file_menu.add_command(label="Зберегти", command=self.controller.save_image)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pixel Art Creator")
    app = PixelArtApp(root)
    root.mainloop()
