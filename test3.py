import subprocess

# Replace this command with your actual command-line string
meshroom_dir = r'C:\Users\mada\Downloads\Meshroom-2023.2.0-win64\Meshroom-2023.2.0'
command_line_string = "cd " + meshroom_dir

# Run the command-line string
try:
    result = subprocess.run(command_line_string, shell=True, capture_output=True, text=True)
except:
    print("fuck")
# Print the output
print("Output:", result.stdout)
