import PySimpleGUI as psg

class TesteColumn:
   
   def __init__(self):
      pass
   
   def draw(self):
        psg.set_options(font=("Arial Bold",10))
        l=psg.Text("Enter Name")
        l1=psg.Text("Address for Correspondence")
        l2=psg.Text("Permanent Address")
        t=psg.Input("", key='-NM-')
        a11=psg.Input(key='-a11-')
        a12=psg.Input(key='-a12-')
        a13=psg.Input(key='-a13-')
        col1=[[l1],[a11], [a12], [a13]]
        a21=psg.Input(key='-a21-')
        a22=psg.Input(key='-a22-')
        a23=psg.Input(key='-a23-')
        col2=[[l2],[a21], [a22], [a23]]
        layout=[[l,t],[psg.Column(col1), psg.Column(col2)], [psg.OK(), psg.Cancel()]]
        window = psg.Window('Column Example', layout, size=(715,200))
        while True:
            event, values = window.read()
            print (event, values)
            if event in (psg.WIN_CLOSED, 'Exit'):
                break
        window.close()
    
teste = TesteColumn()
teste.draw()
