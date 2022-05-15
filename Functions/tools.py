"""
    Autor: Darkx
    Libs: Pillow
"""
from PIL import ImageFilter

class Filters(ImageFilter):
    pass

class Vars:
    TYPEFILES = (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif", ".svg", ".avif", ".eps")

def GetAllFilesInPath(path: str) -> tuple:
    listForReturn = []
    import os
    for files in os.listdir(path):
        if files.endswith(Vars.TYPEFILES):
            listForReturn.append(files)
    return listForReturn
