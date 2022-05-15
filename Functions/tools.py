"""
    Autor: Darkx, Waitofu
    Libs: datetime
"""
from datetime import date

class Vars:
    TYPEFILES = (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif", ".svg", ".avif", ".eps")

class log:
    ERROR = "ERROR"
    WARN = "WARN"
    LOG = "LOG"

    def on_error(error: str, Type: str, file: str):
        open(file, 'a').write(f'[{Type}] {date.today()}: {error}')

    def clearLog(file:str):
        open(file).write("")

def GetAllFilesInPath(path: str) -> tuple:
    listForReturn = []
    import os
    for files in os.listdir(path):
        if files.endswith(Vars.TYPEFILES):
            listForReturn.append(files)
    return listForReturn

