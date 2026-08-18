import customtkinter
import state


def tab_home():
    tabhome = customtkinter.CTkTabview(master=state.app,
        segmented_button_selected_color="#750994",
        segmented_button_selected_hover_color="#7509aa"
    )
    tabhome.grid(padx=20, pady=20)

    frame1 = tabhome.add("Home")
    frame2 = tabhome.add("Configuration")

    tabhome.set("Home")

    tabhome.pack(fill="both", expand=True, padx=20, pady=20)

    customtkinter.CTkLabel(frame1, text="Home").grid(padx=10, pady=10)
    frame1.columnconfigure(0, weight=1)
    customtkinter.CTkButton(frame2, text="Clique!").grid(padx=10, pady=2)