import customtkinter
import state
import awesometkinter as atk
from src.adapters.gui.widgets.cards_three import CardsThree
import re



def Tab_Inicio() :
    consumidos = 10
    ate = 15
    i = 0

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

    GridDisplay = ["GridFrame1", "GridFrame2"]
    frames = {}

    for name in GridDisplay:
        frame = customtkinter.CTkFrame(
            scrollable,
            fg_color=state.RD_BG,
            bg_color=state.RD_BG,
            height=300
        )
        frame.pack(side="left", fill="both", expand=True, padx=10, pady=20, anchor="center")
        frame.pack_propagate(False)
        frames[name] = frame

    LimitLabel = customtkinter.CTkLabel(
        frames["GridFrame1"],
        text="LIMITE DE ARMAZENAMENTO",
        text_color=state.TEXT_SUB,
        font=("Arial", 13, "bold"),
    )
    SaveLabel = customtkinter.CTkLabel(
        frames["GridFrame1"],
        text="Guardar no máximo: ",
        text_color=state.TEXT_LABEL,
        font=("Arial", 11, "bold"),
    )
    LimitSaveLabel = customtkinter.CTkLabel(
        frames["GridFrame1"],
        text="Ao atingir o limite",
        text_color=state.TEXT_LABEL,
        font=("Arial", 11, "bold"),
    )
    OptionMenu = customtkinter.CTkOptionMenu(
        frames["GridFrame1"],
        fg_color=state.CD_BG,
        button_color=state.CD_BG,
        button_hover_color=state.ACCENT_HOVER,
        dropdown_fg_color=state.CD_BG,
        dropdown_hover_color=state.BORDER_DEFAULT,
        dropdown_text_color=state.TEXT_MAIN,
        text_color=state.TEXT_MAIN,
    )
    EntryNumber = customtkinter.CTkEntry(
        frames["GridFrame1"],
        placeholder_text="GB",
        fg_color=state.CD_BG,
        border_color=state.BORDER_DEFAULT,
        text_color=state.TEXT_MAIN,
        placeholder_text_color=state.TEXT_SUB,
    )

    def salvar(event=None):
        valor = EntryNumber.get()

        if re.fullmatch(r"\d+(,\d+)?", valor):
            numero = float(valor.replace(",", "."))
            LimitLabel.configure(text=f"O valor é {numero}")
        else:
            EntryNumber.delete(0, "end")
            LimitLabel.configure(text="Insira um valor numérico (inteiro ou com vírgula)!")

    def ao_focar(event=None):
        EntryNumber.configure(border_color=state.BORDER_FOCUS)

    def ao_desfocar(event=None):
        EntryNumber.configure(border_color=state.BORDER_DEFAULT)

    LimitLabel.pack(anchor="w", padx=35, pady=20)
    SaveLabel.pack(anchor="w",padx=35, pady=0)
    EntryNumber.pack(anchor="nw",fill="x", expand=True, padx=35, pady=0)
    EntryNumber.bind("<Return>", salvar)
    EntryNumber.bind("<FocusIn>", ao_focar)
    EntryNumber.bind("<FocusOut>", ao_desfocar)
    LimitSaveLabel.pack(anchor="w", padx=35, pady=0)
    OptionMenu.pack(side="top", anchor="n",fill="x", expand=True, padx=35, pady=0)


    

    
    scrollable.pack(fill="both", expand=True, padx=0, pady=0)