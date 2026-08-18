import customtkinter
import time
import state
from src.domain.adapters.gui.tabs.tab_home import tab_home


def main():

    state.app = customtkinter.CTk()
    state.app.title("AutoBackup")
    state.app.geometry("400x730+6500px-15px")

    tab_home()

    state.app.columnconfigure(0, weight=1)
    state.app.mainloop()


if __name__ == "__main__":
    main()
