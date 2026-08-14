import customtkinter
import time

def textout(): 
    print("Olá Mundo!")
    time.sleep(1)
    print("Ou Hello World!")



def main():
    app = customtkinter.CTk()

    app.title("AutoBackup")
    app.geometry("400x730")

    button = customtkinter.CTkButton(app, text="Clique!", command=textout)
    button.grid(row=50, column=5, padx=20, pady=20)

    app.columnconfigure(0, weight=1)

    button.grid(row=0, column=0)
    

    app.mainloop()


main()
