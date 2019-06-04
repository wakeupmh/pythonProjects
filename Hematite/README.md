# RPA-Electron-Python
This is a simple example of windows automation using the electron as GUI and python as executor of the same.

## Install 🎴
```
npm install electron
```
More details about get started in [Electron Documentation](https://electronjs.org/).

## Imports :snake:
```
#to execute applications
from pywinauto import application
#to wait execution
import time
```
## Requires :atom_symbol:
In your script adding this require for execute a python file:
```
require('child_process').exec;
```
## Outputs :crystal_ball:
- Open notepad;
- Input the text: 'Este é um teste';
- Save in documents;

## Observation :space_invader:
My windows is PT-BR distribution, if you using a different distribution change these lines in *winauto.py* to correct format.
```
app.Notepad.menu_select("Arquivo ->Salvar")
app.Salvar.edit.set_edit_text("pywinauto.txt")
app.Salvar.Salvar.click()
```
It's quiet and free to do your best. :shipit: 
