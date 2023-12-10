import subprocess

command_write = ['echo', 'Hello World' , '>', 'test.txt']
process_white = subprocess.Popen(' '.join(command_write), shell=True)
process_white.wait() # waits for the child process to return before continuing 

print("Using Popen to echo 'Hello World' to a file")

command_read = ['cat', 'test.txt']
process_read = subprocess.Popen(command_read, stdout=subprocess.PIPE)
file_contents, _ = process_read.communicate()

print("Using Popen to cat test.txt")
print("Contents of test.txt:")
print(file_contents.decode())