import unittest
from unittest.mock import Mock, patch
from PIL import Image
from controller.pixelartcontroller import PixelArtController
from model.pixelartmodel import PixelArtModel
from view.pixelartview import PixelArtView


class TestPixelArtController(unittest.TestCase):
    def setUp(self):
        self.model = Mock(spec=PixelArtModel)
        self.view = Mock(spec=PixelArtView)
        self.controller = PixelArtController(self.model, self.view)

    # Перевірка фарбування пікселя кнопкою миші
    def test_handle_click(self):
        event = Mock()
        event.x = 50
        event.y = 30

        self.model.pixel_size = 10

        self.controller.handle_click(event)

        self.model.set_pixel.assert_called_with(5, 3, self.controller.selected_color)
        self.view.update_view.assert_called_once()

    @patch('tkinter.colorchooser.askcolor')
    # Перевірка вибору кольору
    def test_choose_color(self, mock_askcolor):
        mock_askcolor.return_value = ((255, 0, 0), "#ff0000")

        self.controller.choose_color()

        self.assertEqual(self.controller.selected_color, (255, 0, 0))

    @patch('tkinter.filedialog.asksaveasfilename')
    # Перевірка збереження зображення в правильному форматі
    def test_save_image(self, mock_asksaveasfilename):
        mock_asksaveasfilename.return_value = "test_image.png"

        mock_image = Mock(spec=Image.Image)
        self.model.get_image.return_value = mock_image

        self.controller.save_image()

        mock_image.save.assert_called_with("test_image.png", format='PNG')

    @patch('tkinter.filedialog.askopenfilename')
    @patch('PIL.Image.open')



    # Перевірка відкриття зображення в правильному форматі
    def test_open_image(self, mock_image_open, mock_askopenfilename):
        mock_askopenfilename.return_value = "test_image.png"

        mock_image = Mock(spec=Image.Image)
        mock_image_open.return_value = mock_image

        self.controller.open_image()

        self.model.load_image.assert_called_with(mock_image)
        self.view.update_view.assert_called_once()


if __name__ == '__main__':
    unittest.main()
