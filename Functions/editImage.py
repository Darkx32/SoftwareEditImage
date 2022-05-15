"""
    Autor: Darkzin
    Libs: Pillow
"""
from PIL import Image, ImageFilter
from Functions.tools import *

class Edit:
    def __init__(self, file:str = None) -> None:
        """Create class for edit Image and save in class.

        Args:
            file (str): Name of the file.
        """
        if file.endswith(".gif") or file.endswith(Vars.TYPEFILES):
            return Exception("Error: Type file is not compatible.")
        if len(file.split("\\")) > 1:
            self.filename = file.replace(file.split("\\")[len(file.split("\\"))], "")
        else:
            self.filename = file
        self.file = file
        self.image = Image.open(self.file)

    def rotate(self, grau: float) -> Image:
        """Rotate image saved.

        Args:
            grau (float): angle for rotate.

        Returns:
            Image: return Image class.
        """
        self.image = self.image.rotate(grau)
        return Edit(self.file)

    def resize(self, size: tuple[int, int]) -> Image:
        """Resize image saved.

        Args:
            size (tuple[int, int]): Width and Height in tuple.

        Returns:
            Image: return Image class.
        """
        self.image = self.image.resize(size)
        return Edit(self.file)

    def GetImage(self) -> Image:
        """return Image saved in class.

        Returns:
            Image: return Image class.
        """
        return self.image

    def Show(self, title: str = None) -> None:
        """Show image.

        Args:
            title (str, optional): title of the image. Defaults to None.
        """
        if title != None: self.image.show(title)
        else: self.image.show()

    def Convert(self, convert: str = "png", pathToSave: str = None) -> Image:
        """Convert image and save in path locale.

        Args:
            convert (str, optional): type for image convert. Defaults to "png".
            pathToSave (str, optional): locale for save new image. Defaults to None.

        Returns:
            Image: return Image class.
        """
        if pathToSave == None:
            pathToSave = self.file.replace(f"\\{self.filename}", "")
        image = self.image.convert("RGB")
        image.save(pathToSave.split(".")[0] + f'.{convert}')
        return Edit(pathToSave.split(".")[0] + f'.{convert}')

    def cut(self, box:tuple[int, int, int, int], Save:bool = False) -> Image:
        """Cutting image.

        Args:
            box (tuple[int, int, int, int]): x: int, y: int, width: int, height: int.
            Save (bool, optional): Save in the variabel of the class. Defaults to False.

        Returns:
            Image: return Image class.
        """
        if Save:
            self.image = self.image.crop(box)
            return self.image
        else:
            return self.image.crop(box)

    def addFilter(self, filter: ImageFilter):
        self.image = self.image.filter(filter)


if __name__ == "__main__":
    edit = Edit("Functions/Images/flower.jpg")
    a = edit.cut((0, 0, 100, 100), False)
    a.show()