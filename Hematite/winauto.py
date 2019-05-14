# -*- coding: utf-8 -*-
from pywinauto import application
import time
app = application.Application()
app.start("Notepad.exe")
time.sleep(2)
app.Notepad.edit.type_keys("Este é um teste", with_spaces = True)
time.sleep(2)
app.Notepad.menu_select("Arquivo ->Salvar")
app.Salvar.edit.set_edit_text("pywinauto.txt")
app.Salvar.Salvar.click()
'''app = application.Application()
app.start("Calc.exe")'''

