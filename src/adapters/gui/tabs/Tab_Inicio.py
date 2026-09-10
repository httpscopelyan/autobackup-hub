import customtkinter
import state
import awesometkinter as atk


RD_BG = "#282828"
FM_BG = "#2a2a2a"
CD_BG = "#3F3F3F"


def Tab_Inicio() :
    CD_Variants = ["CD_1", "CD_2", "CD_3"]
    CD_Content = ["1.247 arquivos transferidos", "8,4GB armazenamento usado", "25% economizados na compactação" ]  
    consumidos = 10
    ate = 15

    scrollable = customtkinter.CTkScrollableFrame(
        state.frames[state.TELAS[0]], 
        bg_color=FM_BG,
        fg_color=FM_BG
    )
    RadialFrame = customtkinter.CTkFrame(
        scrollable,
        bg_color=RD_BG,
        fg_color=RD_BG
    )
    GridFrame = customtkinter.CTkFrame(
        scrollable,
        fg_color=RD_BG,
        bg_color=RD_BG
    )
    

    radial = atk.RadialProgressbar(
        RadialFrame, 
        fg="#750994", 
        parent_bg=RD_BG,
        size=(250, 250),
    )
    Caption = customtkinter.CTkLabel(RadialFrame, 
        text=f"{consumidos}GB de {ate}GB",
        font=("Arial", 16, "bold"),
        text_color="#fff",
        bg_color=RD_BG
    )

    Caption.place(in_=radial, relx=0.5, rely=0.7, anchor="n")
    radial.pack( side="left", padx=50, pady=50)
    radial.set(63)
    

    CardTransparente = customtkinter.CTkFrame(
        RadialFrame,
        bg_color="transparent",
        fg_color="transparent",
        width=600,
        height=30,
    )
    CardTransparente.pack(padx=0, pady=0)

    for i, n in zip(CD_Variants, CD_Content):
        i = CardsFrame = customtkinter.CTkFrame(
                RadialFrame,
                bg_color=CD_BG,
                fg_color=CD_BG,
                width=600,
                height=50,
            )
        CardLabel = customtkinter.CTkLabel(
            CardsFrame,
            text=f"{n}",
            font=("Arial", 16, "bold"),
            text_color="#fff",
            bg_color=CD_BG
        )
        CardLabel.place(in_=CardsFrame, relx=0.10, rely=0.23)
        CardsFrame.pack(side="top", pady=12)

    RadialFrame.pack(row=0, column=0, fill="x", padx=0, pady=0)
    GridFrame.pack(fill="y", padx=0, pady=20)
    scrollable.pack(fill="both", expand=True, padx=0, pady=0)
