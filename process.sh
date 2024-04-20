#!/bin/bash

# Set the path to your Google Cloud Storage bucket
GCS_BUCKET="gs://dataset-ryu"

# Set the path to the directory containing the tar files and extracted folders
BASE_DIR="009.립리딩(입모양)_음성인식_데이터/01.데이터/1.Training/원천데이터"

# Iterate over the tar files
for TAR_FILE in "$BASE_DIR"/*.tar; do
    # Extract the tar file
    echo "Extracting $TAR_FILE..."
    tar -xf "$TAR_FILE" -C "$BASE_DIR"
    echo "Extraction complete."

    # Get the directory name from the tar file
    dir_name=$(basename "$TAR_FILE" .tar)

    # Iterate over the subdirectories and process the files
    echo "Processing files in $dir_name..."
    find "$BASE_DIR/$dir_name" -type d -exec bash -c 'for subdir in "$@"; do
        echo "Processing files in $subdir..."
        # Remove mp4 files
        echo "Removing MP4 files..."
        rm -f "$subdir"/*.mp4

        # Convert wav files to flac and remove the original wav files
        for wav_file in "$subdir"/*.wav; do
            echo "Converting $wav_file to FLAC..."
            flac "$wav_file"
            echo "Removing original WAV file..."
            rm -f "$wav_file"
        done
    done' bash {} +
    echo "File processing complete."

    # Move the original tar file to GCS or delete it
    if [ -n "$GCS_BUCKET" ]; then
        echo "Moving $TAR_FILE to $GCS_BUCKET..."
        gsutil -m mv "$TAR_FILE" "$GCS_BUCKET"
        echo "Move complete."
        echo "Deleting $TAR_FILE..."
        rm -f "$TAR_FILE"
        echo "Deletion complete."
    else
        echo "GCS NOT FOUND!!"
    fi
done
