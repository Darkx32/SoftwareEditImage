"""
    Autor: Darkzin
    Libs: PIL
"""

from PIL import Image

class Edit:
    def __init__(self, file:str) -> None:
        """Create class for edit Image and save in class.

        Args:
            file (str): Name of the file.
        """
        self.file = file
        self.image = Image.open(self.file)

    def rotate(self, grau: float) -> Image:
        """Rotate image saved.

        Args:
            grau (float): angle for rotate.

        Returns:
            Image: return Image class.
        """
        return self.image.rotate(grau)

    def resize(self, size: tuple[int, int]) -> Image:
        """Resize image saved.

        Args:
            size (tuple[int, int]): Width and Height in tuple.

        Returns:
            Image: return Image class.
        """
        return self.image.resize(size)