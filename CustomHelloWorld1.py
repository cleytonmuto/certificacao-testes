import customtkinter
import CustomHelloWorld2

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class CustomHelloWorld1(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("320x240+100+100")
        self.title("Hello World 1")

        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=20, pady=0)

        self.label = customtkinter.CTkLabel(self.frame, text="Hello World 1",
            font=customtkinter.CTkFont(size=24, weight="bold") )
        self.label.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.button = customtkinter.CTkButton(self.frame, corner_radius=0,
            height=40, border_spacing=10, text="Open Hello 2", fg_color="blue",
            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            command=self.printHello)
        self.button.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

        self.mainloop()
    
    def printHello(self):
        print("Hello World 1")
        self.destroy()
        CustomHelloWorld2.CustomHelloWorld2()

if __name__ == "__main__":
    CustomHelloWorld1()
