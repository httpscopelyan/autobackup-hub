import customtkinter as ctk
import state


TRILHO      = "#1E1F27"
PILL        = "#292A36"
PILL_HOVER  = "#323443"
INATIVO_BG  = "#1E1F27"
ATIVO_BG    = "#353745"
INATIVO_HV  = "#262833"
TXT_ATIVO   = "#40E0D0"
TXT_INATIVO = "#9295A6"


class SegmentedBar(ctk.CTkFrame):
    def __init__(self, master, tabs, on_select=0, **kw):
        super().__init__(master, fg_color=TRILHO, corner_radius=22, **kw,)
        self.on_select = on_select
        self.buttons = {}

        for i, nome in enumerate(tabs):
            btn = ctk.CTkButton(
                self,
                text=nome,
                fg_color=INATIVO_BG,
                hover_color=INATIVO_HV,
                text_color=TXT_INATIVO,
                font=ctk.CTkFont(size=13),
                corner_radius=18,
                height=36, 
                border_width=0,
                command= lambda n = nome: self.select(n)
            )
            
            padx = (10 if i == 0 else 5, 10 if i == len(tabs) - 1 else 3)
            btn.grid(row=0, column=i, padx=padx, pady=4)
            self.buttons[nome] = btn

            if nome == state.TELAS[0]:
                btn.configure(fg_color=ATIVO_BG, text_color=TXT_ATIVO)
            

    def select(self, nome): 
        self.on_select = state.maintab.set(nome)
        for i, btn in self.buttons.items():
            if i == nome:
                btn.configure(fg_color=ATIVO_BG, text_color=TXT_ATIVO)
            else: 
                btn.configure(fg_color=INATIVO_BG, text_color=TXT_INATIVO)


