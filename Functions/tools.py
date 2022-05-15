"""
    Autor: Darkx, Waitofu
    Libs: Pillow
"""
from distutils.log import error
from ftplib import error_perm
from PIL import ImageFilter
from datetime import date

class Vars:
    TYPEFILES = (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif", ".svg", ".avif", ".eps")

class log:
    def on_error(error, warning):
        erro = f'[ERROR {date.today()}]\n{error}'
        aviso = f'[WARNING {date.today()}]\n{warning}'
        log = f'[LOG {date.today()}]\n'
        if __name__ == '__main__':
            open('log.txt', 'w').write(f'{erro}\n{aviso}\n{log}')

def GetAllFilesInPath(path: str) -> tuple:
    listForReturn = []
    import os
    for files in os.listdir(path):
        if files.endswith(Vars.TYPEFILES):
            listForReturn.append(files)
    return listForReturn

