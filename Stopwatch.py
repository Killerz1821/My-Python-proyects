import PySimpleGUI as sg
from time import time

def create_window():
    sg.theme('Black')
    layout = [
        [sg.VPush()],
        [sg.Text('', font= 'Franklin 50', key= 'TIME')],
        [
        sg.Button('Start', button_color= ('#FFFFFF','#FF0000'), key= 'STARTSTOP')
        ,sg.Button('Lap', button_color= ('#FFFFFF','#FF0000'), key= 'LAP', visible= False)
        ],
        [sg.Column([[]], key= 'LAPS')],
        [sg.VPush()]
    ]
    
    return sg.Window(
        'StopWatch', 
        layout, 
        size = (350,350), 
        no_titlebar = True, 
        element_justification = 'Center') 

window = create_window()

start_time = 0
active = False
lap_amount = 1

while True: 
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, 'Start'):
        break
    
    if event == 'STARTSTOP':
        if active:
            #from active to stop
            active = False
            window['STARTSTOP'].update('Reset')
            window['LAP'].update(visible = False)
        else:
            # from stop to reset
            if start_time > 0:
                 window.close()
                 window = create_window 
                 start_time = 0
            # from start to active
            else:
                start_time = time()
                active = True
                window['STARTSTOP'].update('Stop')
                window['LAP'].update(visible = True)

    if active:
        elapsed_time = round(time() - start_time,1)
        window['TIME'].update(elapsed_time)
    
    if event == "LAP":
        window.extend_layout(window['LAPS'], [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(elapsed_time)]])
        lap_amount += 1 

window.close()