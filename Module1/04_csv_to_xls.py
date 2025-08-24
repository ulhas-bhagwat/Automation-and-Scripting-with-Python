import os
import subprocess

for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        xls_filename = filename.replace('.csv', '.xls')
        # Use a subprocess to call a command-line tool to convert CSV to XLS
        #subprocess.run(['ssconvert', filename, xls_filename], check=True)
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'xls', filename], check=True)

        print(f"Converted {filename} to {xls_filename}")
    else:
        print(f"Skipping {filename}, not a CSV file.")
