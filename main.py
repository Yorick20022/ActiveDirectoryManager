from functions.clearConsole import clearConsole
from functions.getAdGroupMember import getAdGroupMember
from functions.getGroupsMemberOf import getGroupsMemberOf
from functions.copyMemberOf import copyMemberOf
from functions.getPasswordStatus import getPasswordStatus
from functions.listDisabledUsers import listDisabledUsers
from functions.openGithub import openGithub
from functions.copyClipboard import copyClipboard
from functions.openExplorer import openExplorer
from functions.exitProgram import exitProgram
from functions.changeTheme import change_appearance_mode_event
from functions.consoleEntry import AppFunctions
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure fonts for buttons 
        self.button_font = customtkinter.CTkFont(size=14, weight="bold", family="Calibri")
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
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ActiveDirectory\nManager\n______________", font=customtkinter.CTkFont(size=22, weight="bold", family="Calibri"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command= lambda: openGithub(self), text="GitHub Repo", font=self.button_font)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w", font=self.button_font)
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=lambda new_appearance_mode: change_appearance_mode_event(self, new_appearance_mode), font=self.button_font)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # Actions tabview
        self.tabview_actions = customtkinter.CTkTabview(self, width=250)
        self.tabview_actions.grid(row=0, column=2, padx=(10, 20), pady=(5, 0), sticky="nsew")  # Adjusted padx
        self.tabview_actions.add("Actions")
        self.tabview_actions.tab("Actions").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        
        self.optionmenu_1 = customtkinter.CTkButton(self.tabview_actions.tab("Actions"), text="Copy to clipboard", command=lambda: copyClipboard(self), font=self.button_font)
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
    
        self.string_input_button = customtkinter.CTkButton(self.tabview_actions.tab("Actions"), text="Clear console", command=lambda: clearConsole(self), font=self.button_font)
        self.string_input_button.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.string_input_button = customtkinter.CTkButton(self.tabview_actions.tab("Actions"), text="Open file explorer", command=lambda: openExplorer(self), font=self.button_font)
        self.string_input_button.grid(row=5, column=0, padx=20, pady=(10, 10))

        self.string_input_button = customtkinter.CTkButton(self.tabview_actions.tab("Actions"), text="Exit", command=lambda: exitProgram(self), font=self.button_font)
        self.string_input_button.grid(row=6, column=0, padx=20, pady=(10, 10))

        # Scripts tabview
        self.tabview_scripts = customtkinter.CTkTabview(self, width=250)
        self.tabview_scripts.grid(row=1, column=2, padx=(10, 20), pady=(5, 0), sticky="nsew")  # Adjusted padx
        self.tabview_scripts.add("Scripts")
        self.tabview_scripts.tab("Scripts").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        
        self.optionmenu_2 = customtkinter.CTkButton(self.tabview_scripts.tab("Scripts"), text="Get members AD group", command=lambda: getAdGroupMember(self), font=self.button_font)
        self.optionmenu_2.grid(row=0, column=0, padx=20, pady=(20, 10))
    
        self.string_input_button = customtkinter.CTkButton(self.tabview_scripts.tab("Scripts"), text="Get groups of member", command=lambda: getGroupsMemberOf(self), font=self.button_font)
        self.string_input_button.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.string_input_button = customtkinter.CTkButton(self.tabview_scripts.tab("Scripts"), text="Copy user permissions", command=lambda: copyMemberOf(self), font=self.button_font)
        self.string_input_button.grid(row=5, column=0, padx=20, pady=(10, 10))

        self.string_input_button = customtkinter.CTkButton(self.tabview_scripts.tab("Scripts"), text="User password status", command=lambda: getPasswordStatus(self), font=self.button_font)
        self.string_input_button.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.string_input_button = customtkinter.CTkButton(self.tabview_scripts.tab("Scripts"), text="List disabled accounts", command=lambda: listDisabledUsers(self), font=self.button_font)
        self.string_input_button.grid(row=7, column=0, padx=20, pady=(10, 10))

        self.appearance_mode_optionemenu.set("Dark")
        
        # Console
        self.textbox = customtkinter.CTkTextbox(self, width=600, height=520, font=customtkinter.CTkFont(size=14, weight="bold", family="Consolas"))
        self.textbox.place(x=210, y=285, anchor="w")
        
        self.textbox.insert("0.0", "Welcome to ActiveDirectoryManager!")
        self.textbox.configure(state="disabled")

        # Console entry
        self.entry = customtkinter.CTkEntry(master=self, width=600, corner_radius=5, border_width=0, placeholder_text="> _ ", font=customtkinter.CTkFont(size=15, weight="bold", family="Consolas"))
        self.entry.place(x=210, y=572, anchor="w")
        app_functions = AppFunctions(self)  # Pass the instance of App to AppFunctions
        self.entry.bind("<Return>", lambda event: app_functions.execute_command(event))
        self.functions = app_functions  # Assign the functions instance to the App class
        self.process = None

if __name__ == "__main__":
    app = App()
    app.mainloop()
