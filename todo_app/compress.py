import FreeSimpleGUI as sg


label1 = sg.Text("Select file to compress")
input_box1 = sg.InputText(tooltip="Enter file path")
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select file to save compressed data")
input_box2 = sg.InputText(tooltip="Enter output file path")
choose_button2 = sg.FilesBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window('File Compression Tool', 
                   layout=[[label1, input_box1, choose_button1],
                            [label2, input_box2, choose_button2],
                            [compress_button]])


window.read()

window.close()
