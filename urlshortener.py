import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("600x300")
root.title("URL Shortener")
root.configure(bg="#494")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="My URLShortener", font="poppins").pack(pady=15)
Entry(root, textvariable=url).pack(pady=15)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=15)
Entry(root, textvariable=url_address).pack(pady=15)
Button(root, text="Copy URL", command=copyurl).pack(pady=5)

root.mainloop()