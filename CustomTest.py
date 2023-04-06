import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class CustomTest():

    def __init__(self):
        pass

    def login(self):
        print("Test")

    def run(self):
        root = ctk.CTk()
        root.geometry("500x350")

        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
        entry1.pack(pady=12, padx=10)

        entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        entry2.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text="Login", command=self.login)
        button.pack(pady=12, padx=10)

        checkbox = ctk.CTkCheckBox(master=frame,text="Remember Me")
        checkbox.pack(pady=12, padx=10)

        root.mainloop()

teste = CustomTest()
teste.run()
