import PySimpleGUI as sg

sg.theme("DarkTeal")

layout = [[sg.Text("")], [sg.Text("Choose the folder you want to sort: ", size=(20, 1)), sg.InputText(readonly = True), sg.FolderBrowse()], [sg.Text("")], [sg.Button("Submit", size=(8, 1))]]

window = sg.Window("FileSort", layout, size=(600,200))
    
while True:
    event, values = window.read()

    if values[0] == '':
        print("Please select a folder -_-")
        continue
    
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    
    elif event == "Submit":
        source=values[0]
        
        break