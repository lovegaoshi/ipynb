import os
import ctypes
import win32api
import time

from pynput.mouse import Button, Controller
mouse = Controller()

mouse_button_map = {
   'left' : Button.left,
   'right' : Button.right,
   }
def mouse_click(button):
   mouse.click(mouse_button_map[button])

def set_mouse_pos(x, y):
   mouse.position = (x, y)

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def press_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

dic ={
    "esc": 0x01,
    "1": 0x02,
    "2": 0x03,
    "3": 0x04,
    "4": 0x05,
    "5": 0x06,
    "6": 0x07,
    "7": 0x08,
    "8": 0x09,
    "9": 0x0A,
    "0": 0x0B,
    "-": 0x0C,
    "=": 0x0D,
    "backspace": 0x0E,
    "tab": 0x0F,
    "q": 0x10,
    "w": 0x11,
    "e": 0x12,
    "r": 0x13,
    "t": 0x14,
    "y": 0x15,
    "u": 0x16,
    "i": 0x17,
    "o": 0x18,
    "p": 0x19,
    "[": 0x1A,
    "]": 0x1B,
    "enter": 0x1C,
    "ctrl": 0x1D,
    "a": 0x1E,
    "s": 0x1F,
    "d": 0x20,
    "f": 0x21,
    "g": 0x22,
    "h": 0x23,
    "j": 0x24,
    "k": 0x25,
    "l": 0x26,
    ";": 0x27,
    "'": 0x28,
    "`": 0x29,
    "shift": 0x2A,
    "\\": 0x2B,
    "z": 0x2C,
    "x": 0x2D,
    "c": 0x2E,
    "v": 0x2F,
    "b": 0x30,
    "n": 0x31,
    "m": 0x32,
    ",": 0x33,
    ".": 0x34,
    "/": 0x35,
    "shiftr": 0x36,
    "*": 0x37,
    "alt": 0x38,
    "space": 0x39,
    "capslock": 0x3A,
    "f1": 0x3B,
    "f2": 0x3C,
    "f3": 0x3D,
    "f4": 0x3E,
    "f5": 0x3F,
    "f6": 0x40,
    "f7": 0x41,
    "f8": 0x42,
    "f9": 0x43,
    "f10": 0x44,
    "numlock": 0x45,
    "scrolllock": 0x46,
    "7num": 0x47,
    "8num": 0x48,
    "9num": 0x49,
    "-num": 0x4A,
    "4num": 0x4B,
    "5num": 0x4C,
    "6num": 0x4D,
    "+num": 0x4E,
    "1num": 0x4F,
    "2num": 0x50,
    "3num": 0x51,
    "0num": 0x52,
    ".num": 0x53,
    "f11": 0x57,
    "f12": 0x58,
    "f13": 0x64,
    "f14": 0x65,
    "f15": 0x66,
    "kana": 0x70,
    "convert": 0x79,
    "no convert": 0x7B,
    "¥": 0x7D,
    "=": 0x8D,
    "^": 0x90,
    "@": 0x91,
    ":": 0x92,
    "_": 0x93,
    "kanji": 0x94,
    "stop": 0x95,
    "(japan ax)": 0x96,
    "(j3100)": 0x97,
    "enter (numpad)": 0x9C,
    "ctrl (right)": 0x9D,
    ", (numpad)": 0xB3,
    "/ (numpad)": 0xB5,
    "sys rq": 0xB7,
    "alt (right)": 0xB8,
    "pause": 0xC5,
    "home": 0xC7,
    "up": 0xC8,
    "page up": 0xC9,
    "left": 0xCB,
    "right": 0xCD,
    "end": 0xCF,
    "down": 0xD0,
    "page down": 0xD1,
    "insert": 0xD2,
    "delete": 0xD3,
    "windows": 0xDB,
    "windowsr": 0xDC,
    "menu": 0xDD,
    "power": 0xDE,
    "sleep": 0xDF,

}

def press(key, pressing = 0.05, wait = 0.15):
    try:
        key = dic[key]
        press_key(key)
        time.sleep(pressing)
        release_key(key)
        time.sleep(wait)
    except:
        return

def combo(keys, pressing = 0.05, wait = 0.1):
    #rejsires
    try:
        for i in range(len(keys)):
            keys[i] = dic[keys[i]]
        for i in keys:
            press_key(i)
            time.sleep(pressing)
        for i in keys:
            release_key(i)
            time.sleep(pressing)
        time.sleep(wait)
    except:
        return

#import dxinput
#dxinput.press()
#dxinput.combo(['ctrl', 'a'])
