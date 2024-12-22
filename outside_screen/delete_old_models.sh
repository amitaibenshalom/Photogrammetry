#!/bin/bash

# Define the parent folder path
PARENT_FOLDER="/mnt/shared_in/photogrammetry_data"

# Define the age threshold for deletion (in days)
AGE_THRESHOLD=50

# Define the minimum number of subfolders to keep
MIN_SUBFOLDERS=30

# Get a list of subfolders in the parent folder
SUBFOLDERS=($(find "$PARENT_FOLDER" -mindepth 1 -maxdepth 1 -type d))

# Get the total number of subfolders
TOTAL_SUBFOLDERS=${#SUBFOLDERS[@]}

# Check if there are more than the minimum number of subfolders
if [ "$TOTAL_SUBFOLDERS" -gt "$MIN_SUBFOLDERS" ]; then
    # Loop through each subfolder and check its age
    for SUBFOLDER in "${SUBFOLDERS[@]}"; do
        # Get the last modification time of the subfolder in days
        FOLDER_AGE=$(find "$SUBFOLDER" -maxdepth 0 -type d -mtime +$AGE_THRESHOLD)

        # If the folder is older than the threshold, delete it
        if [ -n "$FOLDER_AGE" ]; then
            echo "Deleting folder: $SUBFOLDER"
            # rm -rf "$SUBFOLDER"
        fi
    done
else
    echo "There are less than $MIN_SUBFOLDERS, skipping deletion."
fi

