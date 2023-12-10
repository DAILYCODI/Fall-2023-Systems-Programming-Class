import subprocess

class CommandRunner():
    def __init__(self) -> None:
        pass

    def helloworld(self):
        print("hello world")

    def run_command(self, cmd: str) -> str:
        # Implement command execution using subprocess.Popen
        command = cmd.split()
        print(f"Running command: {command}")
        # Execute the command using subprocess.Popen
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
            
        # Check if the command executed successfully
        if process.returncode != 0:
            print(f"error: {error}")  # Return no output and error message
        else:
            return output

    def parse_ls_output(self, output):
        # Implement parsing of ls -l output
        lines = output.split('\n')
        print(f"file name from: {output} ")
        file_names = [line.split()[-1] for line in lines if line]
        return file_names        

    def parse_ps_output(self, output):
        # Implement parsing of ps aux output
        lines = output.split('\n')
        print(f"file name from: {output} ")
        command_names = [line.split()[-1] for line in lines[1:] if line]  # Skip the header line
        return command_names
        