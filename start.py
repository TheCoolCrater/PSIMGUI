import PySimpleGUI as pg

pg.theme("DarkAmber")


layout = [
    [pg.Text("Enter Name")],
    [pg.InputText()],
    [pg.Button("OK"), pg.Button("CANCEL")]
]


window = pg.Window("Winform", layout)


while True:
    event, values = window.read()
    if event == "CANCEl" or event == pg.WIN_CLOSED:
        break
    print(values[0])


window.close()

