import PySimpleGUI as sg

sg.theme('LightGrey1')
sg.set_options(font= 'Franklin 14', button_element_size= (6,3))
button_size = (6,3)
layout= [
    [sg.Text('', font= 'Franklin 26', expand_x= True, justification= 'right', pad= (10,20), key = '-TEXT-')],
    [sg.Button('Clear', expand_x= True), sg.Button('Enter', expand_x= True)],
    [sg.Button(7, size = button_size),sg.Button(8, size= button_size),sg.Button(9, size= button_size),sg.Button("/", size= button_size)],
    [sg.Button(4, size = button_size),sg.Button(5, size= button_size),sg.Button(6, size= button_size),sg.Button("*g", size= button_size)],
    [sg.Button(1, size = button_size),sg.Button(2, size= button_size),sg.Button(3, size= button_size),sg.Button("-", size= button_size)],
    [sg.Button(0, expand_x= True),sg.Button('.', size= button_size),sg.Button('+',size= button_size)]
]

window = sg.Window('Calculator',layout)

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        
        window['-TEXT-'].update(num_string)

    if event in ['/','*','-','+']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-TEXT-'].update('')

    if event == "Enter":
        full_operation.append(''.join(current_num))
        result = eval(' '.join(full_operation))
        window['-TEXT-'].update(result)
        full_operation = []
    
    if event == 'Clear':
        current_num = []
        full_operation = []
        window['-TEXT-'].update('')

window.close()