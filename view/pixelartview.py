import tkinter as tk


class PixelArtView:
    def __init__(self, root, model):
        self.model = model
        self.canvas = tk.Canvas(root, width=model.width * model.pixel_size, height=model.height * model.pixel_size)
        self.canvas.pack()
        self.update_view()

    def update_view(self):
        self.canvas.delete("all")
        for x in range(self.model.width):
            for y in range(self.model.height):
                color = self.model.pixels[x, y]
                self.canvas.create_rectangle(
                    x * self.model.pixel_size,
                    y * self.model.pixel_size,
                    (x + 1) * self.model.pixel_size,
                    (y + 1) * self.model.pixel_size,
                    fill=self.rgb_to_hex(color),
                    outline=''
                )

    def bind_click(self, callback):
        self.canvas.bind('<Button-1>', callback)

    def bind_erase(self, callback):
        self.canvas.bind('<Button-3>', callback)

    def rgb_to_hex(self, rgb):
        return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
