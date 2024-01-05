import subprocess
import customtkinter

def getGroupsMemberOf(self):
    self.textbox.configure(state="normal")

    # Get the input from the dialog
    dialog = customtkinter.CTkInputDialog(text="Name of the user:", title="GetGroupsMemberOf")
    adUser = dialog.get_input()

    # Specify the path to your PowerShell script
    powershell_script = r'scripts\getGroupsMemberOf.ps1'

    try:
        # Run the PowerShell script and pass the input as a parameter
        scriptOutput = subprocess.check_output(['powershell', '-File', powershell_script, '-adUser', adUser], text=True, stderr=subprocess.STDOUT)

        # Update the text in the custom Textbox with the PowerShell script output
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", scriptOutput)
    except subprocess.CalledProcessError as e:
        # Handle any errors that occurred during script execution
        self.textbox.insert("0.0", f"Error: {e.output}")
    finally:
        # Update the state of the custom Textbox to disabled
        self.textbox.configure(state="disabled")
