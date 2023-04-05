import PySimpleGUI as sg


def main():
    sg.theme('DarkAmber')

    intro = 'This initial text box is to be replaced with the table of results generated after the button press'
    heading = [' File ', ' Parameter ', ' foo ', ' bar ', ' baz ', ' bam ', ' biz ']

    layout = [[sg.Text('Enter Parameter Name')],
             [sg.Combo(size=(200, 20), key='-INPUT-', enable_events=True, values=[])],
             [sg.Button('Search'), sg.Button('Exit')],
             [sg.Column([[sg.Multiline(intro, size=(200,25), key="-OUTPUT-")]], k='-COLM-')],
             [sg.Column([[sg.Table([['' for row in range(7)]for col in range(10)], headings=heading,
                       key='-TABLE-', auto_size_columns = True, visible=False, hide_vertical_scroll=True, 
                       max_col_width=250, def_col_width = 20)]], k='-COLT-', background_color='light blue')]]
     # Create the Window
    window = sg.Window('Table demo', layout, return_keyboard_events=True, background_color='light green')
    event, values = window.read()
    window['-INPUT-'].set_focus()
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break
        # omited for brevity: search and auto-complete on keyboard entry into combo box
        if event == 'Search':
            output = [['A', 'ParameterNameToLongToFitIntoAColumn', 'C', 'D', 'E', 'F', 'G']]
            window['-COLM-'].hide_row() # hides the intro
            window['-TABLE-'].update(output, visible=True) # doesn't change column width
            window['-TABLE-'].AutoSizeColumns = False  # doesn't help
            window['-TABLE-'].ColumnWidths = [20, 150, 20, 20, 20, 20, 20]  # doesn't work
            window['-TABLE-'].expand(expand_x = True, expand_row = True) # doesn't help either


    window.close()


if __name__ == "__main__":
    main()