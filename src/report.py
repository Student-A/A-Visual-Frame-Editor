import ctypes

def SendErrorMessage( title, text ):
    ctypes.windll.user32.MessageBoxA(0, text, title, 0)
