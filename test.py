import subprocess
import os

def run_meshroom(meshroom_path, input_path, output_path, config_path=None, forceCompute=True):
    os.makedirs(output_path, exist_ok=True)
    
    meshroom_cmd = [
        meshroom_path, 
        '-i', input_path,
        '-o', output_path
    ]

    # Add params option if a config file is specified
    if config_path:
        meshroom_cmd.extend(['--overrides', config_path])

    if forceCompute:
        meshroom_cmd.append('--forceCompute')

    try:
        # Run Meshroom command
        result = subprocess.run(meshroom_cmd, shell=True, capture_output=True, text=True)
        print("Meshroom processing completed successfully.")
        # print("Output:", result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error running Meshroom: {e}")

if __name__ == "__main__":

    meshroom_dir = r'C:\Users\mada\Downloads\Meshroom-2023.2.0-win64\Meshroom-2023.2.0\meshroom_batch.exe'
    input_directory = r"C:\Users\mada\Documents\photogrammetry\photogrammetry_data\2024-01-04-11-56-57-3854\images"
    output_directory = r"C:\Users\mada\Documents\photogrammetry\Meshroom-Test"
    config_file = r"C:\Users\mada\Documents\photogrammetry\Meshroom-Test\settings_override"
    print("input: " + input_directory)
    print("output: " + output_directory)
    run_meshroom(meshroom_dir, input_directory, output_directory, config_file)