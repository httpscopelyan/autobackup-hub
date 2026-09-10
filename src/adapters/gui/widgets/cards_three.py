import customtkinter
import state

class CardsThree(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        CardTransparente = customtkinter.CTkFrame(
            self,
            bg_color="transparent",
            fg_color="transparent",
            width=600,
            height=20,
        )
        CardTransparente.pack(padx=0, pady=0)

        bolds = []
        texto = []

        for i, n in zip(state.CD_Variants, state.CD_Content):
            splited = n.split(" ", maxsplit=2 )
            removido = None

            removido = splited.pop(0)
            texto_final = " ".join(splited)
      
            
            icone_cor = state.ICON_BG.get(i, "#2C2650")
            icone_txt = state.ICON_TXT.get(i, "📦")
            i = CardsFrame = customtkinter.CTkFrame(
                    self,
                    bg_color=state.RD_BG,
                    fg_color=state.CD_BG,
                    corner_radius=16,
                    width=600,
                    height=60,
                )
            IconFrame = customtkinter.CTkFrame(
                CardsFrame,
                bg_color=state.CD_BG,
                fg_color=icone_cor,
                corner_radius=12,
                width=42,
                height=42,
            )
            IconFrame.place(relx=0.045, rely=0.5, anchor="w")
            IconLabel = customtkinter.CTkLabel(
                IconFrame,
                text=icone_txt,
                font=("Segoe UI Emoji", 18),
                bg_color=icone_cor,
            )
            IconLabel.place(relx=0.5, rely=0.5, anchor="center")

            BoldLabel = customtkinter.CTkLabel(
                CardsFrame,
                text=f"{removido}",
                font=("Segoe UI", 19, "bold"),
                text_color=state.TEXT_MAIN,
                bg_color=state.CD_BG
            )


            InfoLabel = customtkinter.CTkLabel(
                CardsFrame,
                text=f"{texto_final}",
                font=("Segoe UI", 15, "bold"),
                text_color=state.TEXT_MAIN,
                bg_color=state.CD_BG
            )

            BoldLabel.place(in_=CardsFrame, relx=0.19, rely=0.5, anchor="w")
            InfoLabel.place(in_=CardsFrame, relx=0.31, rely=0.5, anchor="w")
            CardsFrame.pack(side="top", pady=10)