import customtkinter
import time
import state
from src.domain.adapters.gui.tabs.tab_home import tab_home



def main():

    state.app = customtkinter.CTk(fg_color="#2a2a2a")
    state.app.title("AutoBackup")
    state.app.geometry("1020x620+6500px-15px")

    tab_home()
    state.app.columnconfigure(0, weight=1)
    state.app.mainloop()


if __name__ == "__main__":
    main()
