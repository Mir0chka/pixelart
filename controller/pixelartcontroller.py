from tkinter import colorchooser, filedialog
from PIL import Image


class PixelArtController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.selected_color = (0, 0, 0)

        self.view.bind_click(self.handle_click)

    def handle_click(self, event):
        x = event.x // self.model.pixel_size
        y = event.y // self.model.pixel_size

        self.model.set_pixel(x, y, self.selected_color)
        self.view.update_view()

    def handle_erase(self, event):
        x = event.x // self.model.pixel_size
        y = event.y // self.model.pixel_size
        self.model.erase_pixel(x, y)
        self.view.update_view()

    def choose_color(self):
        color = colorchooser.askcolor()[0]
        if color:
            self.selected_color = tuple(map(int, color))

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"),
                                                              ("All files", "*.*")])
        if file_path:
            self.model.get_image().save(file_path, format='PNG')  # Save as PNG

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"),
                                                           ("All files", "*.*")])
        if file_path:
            image = Image.open(file_path)
            self.model.load_image(image)
            self.view.update_view()
