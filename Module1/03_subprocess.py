#! usr/bin/env python3

import subprocess
# Use grep to find lines containing "error" in a log file
grep_process = subprocess.Popen(['grep', 'error', 'log_file.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# pass the output to another command, like wc to count the number of lines
wc_process = subprocess.Popen(['wc', '-l'], stdin=grep_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Number of lines containing 'error':", wc_process.communicate()[0].decode().strip())

# pass the output of grep to a python script
python_process = subprocess.Popen(['python3', 'process_output.py'], stdin=grep_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

python_process.wait()  # Wait for the python script to finish
output, error = python_process.communicate()
  


