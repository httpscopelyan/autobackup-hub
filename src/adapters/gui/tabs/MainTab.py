import customtkinter
import state
from src.adapters.gui.widgets.segmented_bar import SegmentedBar
from src.adapters.gui.tabs.Tab_Inicio import Tab_Inicio

def MainTab():
    state.maintab = customtkinter.CTkTabview(master=state.app,
        bg_color="#16171D",
        fg_color="#16171D"
    )

    state.maintab.columnconfigure(0, weight=1)
    state.maintab._segmented_button.grid_configure(padx=20, pady=(20, 0))

    for nome in state.TELAS:
        frame = state.maintab.add(nome)
        frame.configure(fg_color="#16171D")
        frame.columnconfigure(0, weight=1)
        state.frames[nome] = frame

    state.maintab._segmented_button.grid_forget()

    bar = SegmentedBar(state.app, state.TELAS)

    bar.pack(padx=20, pady=20)
    
    Tab_Inicio()

    state.maintab.pack(fill="both", expand=True, padx=20, pady=20)
    state.maintab.set(state.TELAS[0])