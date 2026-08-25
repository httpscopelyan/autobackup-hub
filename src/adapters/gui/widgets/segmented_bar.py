import customtkinter as ctk
import state


TRILHO      = "#EDECF7"  
PILL        = "#FFFFFF"   
PILL_HOVER  = "#FFFFFF"
INATIVO_BG  = "#EDEDED"  
ATIVO_BG    = "#c2c2c2"
INATIVO_HV  = "#E4E2F2"
TXT_ATIVO   = "#2ab" 
TXT_INATIVO = "#A3A1BF"   


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
            # 10px nas pontas: com padx=3 o canvas do botao invadia o canto
            # arredondado do trilho e sobrava um retangulo claro
            padx = (10 if i == 0 else 5, 10 if i == len(tabs) - 1 else 3)
            btn.grid(row=0, column=i, padx=padx, pady=4)
            self.buttons[nome] = btn

            if nome == "Inicio":
                btn.configure(fg_color=ATIVO_BG, text_color=TXT_ATIVO)
            

    def select(self, nome): 
        self.on_select = state.tabhome.set(nome)
        for i, btn in self.buttons.items():
            if i == nome:
                btn.configure(fg_color=ATIVO_BG, text_color=TXT_ATIVO)
            else: 
                btn.configure(fg_color=INATIVO_BG, text_color=TXT_INATIVO)


