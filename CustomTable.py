import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
 
class Table(customtkinter.CTk):
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = customtkinter.CTkEntry(root, width=120, fg_color="blue",
                               font=customtkinter.CTkFont(size=24, weight="bold"))
                self.e.grid(row=i, column=j)
                self.e.insert(customtkinter.END, lst[i][j])
 
# take the data
lst = [(1,"Raj","Mumbai",19),
       (2,"Aaryan","Pune",18),
       (3,"Vaishnavi","Mumbai",20),
       (4,"Rachna","Mumbai",21),
       (5,"Shubham","Delhi",21)]
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = customtkinter.CTk()
t = Table(root)
root.mainloop()
