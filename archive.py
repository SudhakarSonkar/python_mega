import FreeSimpleGUI as sg


sg.theme('DarkBlue')

label1 = sg.Text("Select archive file:")
input1 = sg.Input()
cloose_button = sg.FileBrowse("Browse", key='archive_file')

label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
cloose_button = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract", key='extract')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, cloose_button],
                            [label2, input2, cloose_button],
                            [extract_button, output_label]])


window.read()
window.close()
                   
                   