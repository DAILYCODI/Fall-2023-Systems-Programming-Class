from command_runner import CommandRunner

command = CommandRunner()
command.helloworld()
result = command.run_command("ls -l")
print(result)
command.parse_ls_output("command_runner.py test.py")
command.parse_ps_output("ps aux")
