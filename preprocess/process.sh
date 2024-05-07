#!/bin/bash

GCS_BUCKET="gs://dataset-ryu"

BASE_DIR="009.립리딩(입모양)_음성인식_데이터/01.데이터/1.Training/원천데이터"

for TAR_FILE in "$BASE_DIR"/*.tar; do
    # Extract the tar file
    echo "Extracting $TAR_FILE..."
    tar -xf "$TAR_FILE" -C "$BASE_DIR"
    echo "Extraction complete."

    dir_name=$(basename "$TAR_FILE" .tar)

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
