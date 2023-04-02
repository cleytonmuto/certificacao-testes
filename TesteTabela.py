import PySimpleGUI as sg

class TesteTabela:
   
    def __init__(self):
       pass

    def draw(self):
        sg.set_options(font=("Arial Bold", 14))
        toprow = ['ID', 'Nome', 'Idade', 'Nota']
        rows = [[1, 'Fulano', 23, 78],
                [2, 'Beltrano', 21, 66],
                [3, 'Sincrano', 22, 60],
                [4, 'Deltrano', 20, 75]]
        layout = [
            [sg.Table(values=rows, headings=toprow,
                # auto_size_columns=True,
                col_widths=1,
                display_row_numbers=False,
                justification='center', key='-TABLE-',
                selected_row_colors='black on white',
                enable_events=True,
                expand_x=True,
                expand_y=True,
                enable_click_events=True)]
        ]
        window = sg.Window("Teste Tabela", layout, size=(715, 200), resizable=True)
        while True:
            event, values = window.read()
            print("event:", event, "values:", values)
            if event == sg.WIN_CLOSED:
                break
            if '+CLICKED+' in event:
                sg.popup("Voce clicou na linha {} e coluna {}".format(event[2][0], event[2][1]))
        window.close()

teste = TesteTabela()
teste.draw()
