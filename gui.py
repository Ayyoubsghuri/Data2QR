from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import webbrowser
from reader import read_excel,clearAll
from scanQr import start_scanning
from fontTools.ttLib import TTFont

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("867x601")
window.configure(bg = "#FFFFFF")

font = TTFont('fonts/Righteous-Regular.ttf')
font.save


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 601,
    width = 867,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    494.0,
    626.0,
    fill="#F7F7F7",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    670.0,
    285.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    665.0,
    84.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: start_scanning(entries),
    relief="flat"
)
button_1.place(
    x=503.0,
    y=243.0,
    width=339.0,
    height=86.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clearAll(entries),
    relief="flat"
)
button_2.place(
    x=534.0,
    y=396.0,
    width=283.2883605957031,
    height=46.347389221191406
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: read_excel(),
    relief="flat"
)
button_3.place(
    x=336.0,
    y=536.0,
    width=139.0,
    height=62.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    137.0,
    46.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    235.0,
    195.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    238.0,
    468.0,
    image=image_image_5
)

canvas.create_text(
    58.0,
    84.0,
    anchor="nw",
    text="Nom:",
    fill="#717171",
    font=("LibreBaskerville Regular", 20 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    226.0,
    127.36363220214844,
    image=image_image_6
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    226.0,
    131.8636360168457,
    image=entry_image_1
)
entry_1 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=65.0,
    y=116.7272720336914,
    width=322.0,
    height=28.272727966308594
)

canvas.create_text(
    58.0,
    147.0,
    anchor="nw",
    text="Prenom:",
    fill="#717171",
    font=("LibreBaskerville Regular", 20 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    226.0,
    190.36363220214844,
    image=image_image_7
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    226.0,
    194.86362838745117,
    image=entry_image_2
)
entry_2 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=65.0,
    y=179.72726440429688,
    width=322.0,
    height=28.272727966308594
)

canvas.create_text(
    58.0,
    210.0,
    anchor="nw",
    text="Cine:",
    fill="#717171",
    font=("LibreBaskerville Regular", 20 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    226.0,
    253.36363220214844,
    image=image_image_8
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    226.0,
    257.8636283874512,
    image=entry_image_3
)
entry_3 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=65.0,
    y=242.72726440429688,
    width=322.0,
    height=28.272727966308594
)
entries = [entry_1 , entry_2, entry_3]

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open('https://github.com/AyoubSghuri/DATA2QR'),
    relief="flat"
)
button_4.place(
    x=781.0,
    y=519.0,
    width=67.0,
    height=79.0
)
window.resizable(False, False)
window.mainloop()
