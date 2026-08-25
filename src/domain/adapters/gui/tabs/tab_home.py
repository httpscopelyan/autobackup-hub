import customtkinter
import state
import awesometkinter as atk
from src.domain.adapters.gui.button.button import SegmentedBar

def tab_home():
    state.tabhome = customtkinter.CTkTabview(master=state.app,
        fg_color="#2a2a2a"
    )

    state.tabhome.columnconfigure(0, weight=1)
    state.tabhome._segmented_button.grid_configure(padx=20, pady=(20, 0))


    for i in state.TELAS: 
        frames = state.tabhome.add(i)

    state.tabhome._segmented_button.grid_forget()

    bar = SegmentedBar(
        state.app,
        state.TELAS,
    )
    bar.pack(padx=20, pady=20)

    button = customtkinter.CTkButton(frames, text="Olá")
    button.pack(padx=20, pady=20)

    frames.configure(fg_color="#2a2a2a")
    frames.columnconfigure(0, weight=1)


    
    state.tabhome.pack(fill="both", expand=True, padx=20, pady=20)
    state.tabhome.set("Inicio")


    # div = customtkinter.CTkFrame(master=frame1, corner_radius=10, fg_color="#2b2f2f")
    # div.pack(padx=20, pady=5, fill="x")
    # atk.RadialProgressbar(frame1, fg="#750994", parent_bg="#2a2a2a", size=120).grid(row=0, column=0, padx=10, pady=10)