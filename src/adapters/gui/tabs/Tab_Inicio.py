import customtkinter
import state
import awesometkinter as atk
from src.adapters.gui.widgets.cards_three import CardsThree



def Tab_Inicio() :
    consumidos = 10
    ate = 15

    scrollable = customtkinter.CTkScrollableFrame(
        state.frames[state.TELAS[0]], 
        bg_color=state.FM_BG,
        fg_color=state.FM_BG
    )
    RadialFrame = customtkinter.CTkFrame(
        scrollable,
        corner_radius=16,
        bg_color="transparent",
        fg_color=state.RD_BG
    )
    GridFrame = customtkinter.CTkFrame(
        scrollable,
        fg_color=state.RD_BG,
        bg_color=state.RD_BG
    )
    

    radial = atk.RadialProgressbar(
        RadialFrame, 
        fg="#7C6CF6",
        bg="#2A2B36",
        text_fg=state.TEXT_MAIN,
        font=("Segoe UI", 34, "bold"),
        parent_bg=state.RD_BG,
        size=(250, 250),
    )
    Caption = customtkinter.CTkLabel(RadialFrame, 
        text=f"{consumidos}GB de {ate}GB",
        font=("Segoe UI", 14),
        text_color=state.TEXT_SUB,
        bg_color=state.RD_BG
    )

    Caption.place(in_=radial, relx=0.5, rely=0.68, anchor="n")
    radial.pack( side="left", padx=50, pady=50)
    radial.set(63)
    

    cards = CardsThree(RadialFrame)
    cards.pack(padx=0, pady=0)

    
    RadialFrame.pack(fill="x", padx=0, pady=0)
    GridFrame.pack(fill="y", padx=0, pady=20)
    scrollable.pack(fill="both", expand=True, padx=0, pady=0)