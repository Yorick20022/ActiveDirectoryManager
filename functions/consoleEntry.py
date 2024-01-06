import subprocess
import threading

class AppFunctions:
    def __init__(self, app_instance):
        self.app_instance = app_instance

    def execute_command(self, event):
        self.app_instance.textbox.configure(state="normal")
        self.app_instance.textbox.delete("0.0", "end")
        # Get the command from the entry widget
        command = self.app_instance.entry.get()

        if command.strip().lower() == 'cls':
            self.app_instance.textbox.delete("0.0", "end")
            self.app_instance.entry.delete(0, "end")
            return

        # Start a new process and run it in a separate thread
        self.app_instance.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

        # Start a separate thread to read and display the output in real-time
        threading.Thread(target=self.update_output).start()

        # Clear the entry widget for the next command
        self.app_instance.entry.delete(0, "end")

    def update_output(self):
        # Read the output line by line
        for line in self.app_instance.process.stdout:
            # Append the line to the textbox
            self.app_instance.textbox.configure(state="normal")
            self.app_instance.textbox.insert("end", line)
            self.app_instance.textbox.configure(state="disabled")

    def process_command(self, command):
        try:
            # Execute the command using subprocess
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            # If there's an error, capture the output
            result = e.output

        return result
