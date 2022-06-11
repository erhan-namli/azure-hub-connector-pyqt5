from PyQt5 import uic


with open("MainPage.py", "w", encoding="utf-8") as fout:
    uic.compileUi('MainPage.ui', fout)