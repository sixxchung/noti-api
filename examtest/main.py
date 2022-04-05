from typing import Text
from window import Window
from textfile import TextFile
from database import Database

tf = TextFile()
db = Database()

w = Window(storage=tf)
# w = Window(storage=TextFile())
# w = Window(TextFile())

w.write_text("Hello DI!")
w.show_window()
w.save_text()
