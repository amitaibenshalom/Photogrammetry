import subprocess
import os
import json

def run_meshroom(input_path, output_path, config_path=None):
    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Define the Meshroom command
    meshroom_cmd = [
        'meshroom_batch.exe',  # Replace with the actual Meshroom batch command
        '--input', input_path,
        '--output', output_path
    ]

    # Add params option if a config file is specified
    if config_path:
        meshroom_cmd.extend(['--params', config_path])

    try:
        # Run Meshroom command
        subprocess.run(meshroom_cmd, check=True)
        print("Meshroom processing completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Meshroom: {e}")

if __name__ == "__main__":

    meshroom_dir = 'C:/Users/amita/Downloads/Meshroom-2021.1.0-win64/Meshroom-2021.1.0'

    input_directory = 'D:/Amitai_D/museum/photogrammetria/tests/test31_8_2023/pictures_31_8_2023_0'

    # Replace 'path/to/output' with the desired output path
    output_directory = 'D:/Amitai_D/museum/photogrammetria/tests/test_14_11_2023'

    # Replace 'path/to/your/config.json' with the actual path to your JSON configuration file
    config_file = 'C:/Users/amita/PycharmProjects/Meshroom-Test/meshroom_settings.JSON'

    run_meshroom(input_directory, output_directory, config_file)
