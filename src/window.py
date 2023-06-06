from ctypes import windll
from keyboard import add_hotkey
from os import system, path

def hideWindow():
    hWnd = windll.kernel32.GetConsoleWindow()
    windll.user32.ShowWindow(hWnd, 0)

def showWindow():
    hWnd = windll.kernel32.GetConsoleWindow()
    windll.user32.ShowWindow(hWnd, 5)