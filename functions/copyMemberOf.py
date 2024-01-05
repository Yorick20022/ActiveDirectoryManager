import subprocess
import customtkinter

def copyMemberOf(self):
    self.textbox.configure(state="normal")

    # Get the input from the dialog
    existingUser = customtkinter.CTkInputDialog(text="Name of the existing user:", title="Existing user")
    existingUserInput = existingUser.get_input()

    newUser = customtkinter.CTkInputDialog(text="Name of the new user:", title="New user")
    newUserInput = newUser.get_input()

    # Specify the path to your PowerShell script
    powershell_script = r'scripts\copyMemberOf.ps1'

    try:
        # Run the PowerShell script and pass the input as a parameter
        scriptOutput = subprocess.check_output(['powershell', '-File', powershell_script, '-existingUser', existingUserInput, '-newUser', newUserInput], text=True, stderr=subprocess.STDOUT)

        # Update the text in the custom Textbox with the PowerShell script output
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", scriptOutput)
    except subprocess.CalledProcessError as e:
        # Handle any errors that occurred during script execution
        self.textbox.insert("0.0", f"Error: {e.output}")
    finally:
        # Update the state of the custom Textbox to disabled
        self.textbox.configure(state="disabled")
