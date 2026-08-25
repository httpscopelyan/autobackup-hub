import customtkinter
import state
import awesometkinter as atk
from src.adapters.gui.widgets.segmented_bar import SegmentedBar

def tab_home():
    state.tabhome = customtkinter.CTkTabview(master=state.app,
        fg_color="#2a2a2a"
    )

    state.tabhome.columnconfigure(0, weight=1)
    state.tabhome._segmented_button.grid_configure(padx=20, pady=(20, 0))

    frames = {}
    for nome in state.TELAS:
        frame = state.tabhome.add(nome)
        frame.configure(fg_color="#2a2a2a")
        frame.columnconfigure(0, weight=1)
        frames[nome] = frame

    state.tabhome._segmented_button.grid_forget()

    bar = SegmentedBar(state.app, state.TELAS)
    button = customtkinter.CTkButton(frames[state.TELAS[0]], text="Olá")

    bar.pack(padx=20, pady=20)
    button.pack(padx=20, pady=20)
    state.tabhome.pack(fill="both", expand=True, padx=20, pady=20)
    state.tabhome.set(state.TELAS[0])


    # div = customtkinter.CTkFrame(master=frame1, corner_radius=10, fg_color="#2b2f2f")
    # div.pack(padx=20, pady=5, fill="x")
    # atk.RadialProgressbar(frame1, fg="#750994", parent_bg="#2a2a2a", size=120).grid(row=0, column=0, padx=10, pady=10)