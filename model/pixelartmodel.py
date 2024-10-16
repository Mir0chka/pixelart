from PIL import Image


class PixelArtModel:
    def __init__(self, width, height, pixel_size):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.image = Image.new('RGB', (width, height), 'white')
        self.pixels = self.image.load()

    def set_pixel(self, x, y, color):
        self.pixels[x, y] = color

    def load_image(self, image):
        """Load the image and update the pixel data."""
        image = image.convert("RGB")
        image = image.resize((self.width, self.height), Image.NEAREST)
        self.image = image
        self.pixels = self.image.load()

    def erase_pixel(self, x, y):
        self.pixels[x, y] = (255, 255, 255)

    def get_image(self):
        return self.image  # Return the image object
