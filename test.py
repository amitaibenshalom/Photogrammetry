import subprocess
import os

def run_meshroom(input_path, output_path):
    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Define the Meshroom command
    meshroom_cmd = [
        'meshroom_batch',  # Replace with the actual Meshroom batch command
        '--input', input_path,
        '--output', output_path
    ]

    try:
        # Run Meshroom command
        subprocess.run(meshroom_cmd, check=True)
        print("Meshroom processing completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Meshroom: {e}")

if __name__ == "__main__":
    # Replace 'path/to/your/images' with the actual path to your images
    input_directory = 'path/to/your/images'

    # Replace 'path/to/output' with the desired output path
    output_directory = 'path/to/output'

    run_meshroom(input_directory, output_directory)
