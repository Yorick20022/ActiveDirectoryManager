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
import customtkinter
from PIL import Image
import subprocess
import threading

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

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
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=lambda new_appearance_mode: self.change_appearance_mode_event(new_appearance_mode), font=self.button_font)
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
        
        self.textbox.insert("0.0", "Welcome to ActiveDirectoryManager!\n")
        self.textbox.configure(state="disabled")

        # Entry
        self.entry = customtkinter.CTkEntry(master=self, width=600, corner_radius=5, border_width=0, placeholder_text="> _ ", font=customtkinter.CTkFont(size=15, weight="bold", family="Consolas"))
        self.entry.place(x=210, y=572, anchor="w")
        self.entry.bind("<Return>", lambda event: self.execute_command(event))
        self.process = None

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def execute_command(self, event):
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        # Get the command from the entry widget
        command = self.entry.get()

        if command.strip().lower() == 'cls':
            self.textbox.delete("0.0", "end")
            self.entry.delete(0, "end")
            return

        # Start a new process and run it in a separate thread
        self.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

        # Start a separate thread to read and display the output in real-time
        threading.Thread(target=self.update_output).start()

        # Clear the entry widget for the next command
        self.entry.delete(0, "end")

    def update_output(self):
        # Read the output line by line
        for line in self.process.stdout:
            # Append the line to the textbox
            self.textbox.configure(state="normal")
            self.textbox.insert("end", line)
            self.textbox.configure(state="disabled")
        
    def process_command(self, command):
        try:
            # Execute the command using subprocess
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            # If there's an error, capture the output
            result = e.output

        return result

    
        
if __name__ == "__main__":
    app = App()
    app.mainloop()