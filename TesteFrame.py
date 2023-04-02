import PySimpleGUI as psg

class TesteFrame:

    def __init__(self):
        pass

    def draw(self):
        psg.set_options(font=("Arial Bold", 14))
        l1 = psg.Text("Enter Name")
        l2 = psg.Text("Faculty")
        l3 = psg.Text("Subjects")
        l4 = psg.Text("Category")
        l5 = psg.Multiline(" ", expand_x=True, key='-OUT-',  expand_y=True, justification='left')
        t1 = psg.Input("", key='-NM-')
        rb = []
        rb.append(psg.Radio("Arts", "faculty", key='arts',  enable_events=True, default=True))
        rb.append(psg.Radio("Commerce", "faculty", key='comm', enable_events=True))
        rb.append(psg.Radio("Science", "faculty", key='sci', enable_events=True))
        cb = []
        cb.append(psg.Checkbox("History", key='s1'))
        cb.append(psg.Checkbox("Sociology", key='s2'))
        cb.append(psg.Checkbox("Economics", key='s3'))
        b1 = psg.Button("OK")
        b2 = psg.Button("Exit")
        rlo = psg.Frame("Faculty", [rb], title_color='blue')
        clo = psg.Frame("Subjects", [cb], title_color='blue')
        layout = [[l1, t1], [rlo], [clo], [b1, l5, b2]]
        window = psg.Window('Frame Example', layout, size=(715, 300))
        while True:
            event, values = window.read()
            print(event, values)
            if event in (psg.WIN_CLOSED, 'Exit'):
                break
        window.close()

teste = TesteFrame()
teste.draw()
