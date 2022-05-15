"""
    Autor: Darkzin
    Libs: Pillow
"""
from PIL import Image, ImageFilter
try:
    from tools import *
except:
    from Functions.tools import *

class Edit:
    def __init__(self, name: str, file:str = None, size:tuple[int, int] = None, Color:str = "white", pathLog:str = "logs.txt") -> None:
        """Create class for edit Image and save in class.

        Args:
            file (str): Name of the file.
        """
        self.name = name
        self.__Nones()
        self.pathLog = pathLog

        if file != None:
            if file.endswith(".gif"):
                return log.on_error(f"File is not compatible [{self.name}]", log.ERROR, self.pathLog)
            if len(file.split("\\")) > 1:
                self.filename = file.replace(file.split("\\")[len(file.split("\\"))], "")
            else:
                self.filename = file
            self.file = file
            self.image = Image.open(self.file)
        else:
            self.size = [600, 500] if size == None else size
            self.image = Image.new("RGB", self.size, Color)

    def __Nones(self):
        self.file = None
        self.filename = None
        self.image = None
        self.size = None

    def rotate(self, grau: float) -> Image:
        """Rotate image saved.

        Args:
            grau (float): angle for rotate.

        Returns:
            Image: return Image class.
        """
        self.image = self.image.rotate(grau)
        log.on_error(f"Image rotated [{self.name}].", log.LOG, self.pathLog)
        return Edit(self.file)

    def resize(self, size: tuple[int, int]) -> Image:
        """Resize image saved.

        Args:
            size (tuple[int, int]): Width and Height in tuple.

        Returns:
            Image: return Image class.
        """
        self.image = self.image.resize(size)
        log.on_error(f"Image resized [{self.name}].", log.LOG, self.pathLog)
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
        log.on_error(f"Image Showned [{self.name}].", log.LOG, self.pathLog)

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
        log.on_error(f"Image converted to {convert} [{self.name}].", log.LOG, self.pathLog)
        return Edit(self.filename if self.filename != None else (self.name + " - Resized"),
        file=pathToSave.split(".")[0] + f'.{convert}')

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
            log.on_error(f"Image cupped and save [{self.name}].", log.LOG, self.pathLog)
            return self.image
        else:
            log.on_error(f"Image cupped [{self.name}].", log.LOG, self.pathLog)
            return self.image.crop(box)

    def addFilter(self, filter: ImageFilter) -> Image:
        """Add filter in image.

        Args:
            filter (ImageFilter): Type filter for add.

        Returns:
            Image: return Image class.
        """
        log.on_error(f"Filter add in image [{self.name}].", log.LOG, self.pathLog)
        self.image = self.image.filter(filter)
        return self.image


if __name__ == "__main__":
    edit = Edit("dog",Color="black")
    edit.Show()