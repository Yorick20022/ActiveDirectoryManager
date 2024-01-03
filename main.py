from functions.clearConsole import clearConsole
from functions.getAdGroupMember import getAdGroupMember
from functions.openGithub import openGithub 
from functions.copyClipboard import copyClipboard
from functions.playYoutube import playYoutube
from functions.exportCsv import exportCSV
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("ActiveDirectoryManager")
        self.geometry(f"{1100}x{600}")
        self.resizable(False, False)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ActiveDirectory\nManager\n______________", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command= lambda: openGithub(self), text="My Github")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: playYoutube(self), text="Secret")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=lambda new_appearance_mode: self.change_appearance_mode_event(new_appearance_mode))
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(5, 0), sticky="nsew")
        self.tabview.add("Actions")
        self.tabview.tab("Actions").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        self.optionmenu_1 = customtkinter.CTkButton(self.tabview.tab("Actions"), text="Copy to Clipboard", command=lambda: copyClipboard(self))
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Actions"), text="Do something", command=lambda: getAdGroupMember(self))
        self.string_input_button.grid(row=3, column=0, padx=20, pady=(10, 10))
        
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Actions"), text="Clear console", command=lambda: clearConsole(self))
        self.string_input_button.grid(row=4, column=0, padx=20, pady=(10, 10))

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Scripts")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nwes")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        customtkinter.CTkButton(master=self.scrollable_frame, text="Get Members AD Group", command=lambda: getAdGroupMember(self)).grid(row=0, column=0, padx=20, pady=(5, 10))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Script 2", command=lambda: getAdGroupMember(self)).grid(row=1, column=0, padx=20, pady=(10, 10))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Script 3", command=lambda: getAdGroupMember(self)).grid(row=2, column=0, padx=20, pady=(10, 10))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Script 4", command=lambda: getAdGroupMember(self)).grid(row=3, column=0, padx=20, pady=(10, 10))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Script 5", command=lambda: getAdGroupMember(self)).grid(row=4, column=0, padx=20, pady=(10, 10))
        
        self.appearance_mode_optionemenu.set("Dark")
        
        self.textbox.insert("0.0", "Welcome to ActiveDirectoryManager!\n")
        self.textbox.configure(state="disabled")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()