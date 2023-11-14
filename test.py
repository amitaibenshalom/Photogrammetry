import subprocess
import os
import json

def run_meshroom(meshroom_path, input_path, output_path, config_path=None):
    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)
    
    # # Define the Meshroom command
    meshroom_cmd = [
        meshroom_path, 
        '-i', input_path,
        '-o', output_path
    ]

    # Add params option if a config file is specified
    if config_path:
        meshroom_cmd.extend(['-p', config_path])

    try:
        # Run Meshroom command
        result = subprocess.run(meshroom_cmd, shell=True, capture_output=True, text=True)
        print("Meshroom processing completed successfully.")
        print("Output:", result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error running Meshroom: {e}")

if __name__ == "__main__":

    meshroom_dir = r' C:\Users\mada\Downloads\Meshroom-2023.2.0-win64\Meshroom-2023.2.0\meshroom_batch.exe'
    # meshroom_dir = r'C:\Users\mada\Downloads\Meshroom-2023.2.0-win64\Meshroom-2023.2.0'
    input_directory = r"C:\Users\mada\Documents\photogrammetry\photogrammetry_data\2023-11-13-19-11-02-4916\images"

    # Replace 'path/to/output' with the desired output path
    output_directory = r"C:\Users\mada\Documents\photogrammetry\Meshroom-Test"
    print(meshroom_dir)
    print(input_directory)
    print(output_directory)
    print("\n\n")
    # Replace 'path/to/your/config.json' with the actual path to your JSON configuration file
    # config_file = 'C:/Users/mada/Documents/photogrammetry/musem_photogrametry_project/settings_override.json'
    run_meshroom(meshroom_dir, input_directory, output_directory)
