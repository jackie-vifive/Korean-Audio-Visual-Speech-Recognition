import json
import os
from tqdm import tqdm

def process_json_files(label_dir, audio_dir, output_dir, data_type):
    # Use a data-specific subdirectory for outputs
    output_subdir = os.path.join(output_dir, data_type)
    if not os.path.exists(output_subdir):
        os.makedirs(output_subdir)

    # Iterate over all directories and files in label_dir
    for root, dirs, files in tqdm(os.walk(label_dir), desc=f'Processing {data_type} directories'):
        for file in tqdm(files, desc=f'Processing {data_type} files', leave=False):
            if file.endswith('.json'):
                json_path = os.path.join(root, file)
                process_single_json(json_path, root, audio_dir, output_subdir, data_type)

def process_single_json(json_path, label_root, audio_dir, output_dir, data_type):
    with open(json_path, 'r') as f:
        data = json.load(f)

    text = []
    wav_scp = []
    utt2spk = []

    speaker_id = data[0]['speaker_info']['speaker_ID']
    audio_name = data[0]['Audio_info']['Audio_Name'].replace('.wav', '.flac')
    # Compute the relative path to the audio file from label directory structure
    # print(label_root)
    # print(audio_dir)
    # rel_path = os.path.relpath(label_root, label_dir)
    audio_path = os.path.join(label_root, audio_name)

    for sentence in data[0]['Sentence_info']:
        utterance_id = f"{data_type}_{speaker_id}_{sentence['ID']}"
        text.append(f"{utterance_id} {sentence['sentence_text']}")
        wav_scp.append(f"{utterance_id} {audio_path}")
        utt2spk.append(f"{utterance_id} {speaker_id}")

    # Append data to files
    append_to_file(os.path.join(output_dir, 'text'), text)
    append_to_file(os.path.join(output_dir, 'wav.scp'), wav_scp)
    append_to_file(os.path.join(output_dir, 'utt2spk'), utt2spk)

def append_to_file(file_path, data_list):
    with open(file_path, 'a') as f:
        f.write("\n".join(data_list) + "\n")

def main():
    base_dir = '/home/jupyter/Korean-Audio-Visual-Speech-Recognition/data'
    output_dir = 'kaldi_formatted_data2'
    
    # Process training data
    print("Processing Training Data")
    training_label_dir = os.path.join(base_dir, '1.Training/label')
    training_audio_dir = os.path.join(base_dir, '1.Training/src')
    process_json_files(training_label_dir, training_audio_dir, output_dir, 'train')

    # Process validation data
    print("Processing Validation Data")
    valid_label_dir = os.path.join(base_dir, '2.Validation/label')
    valid_audio_dir = os.path.join(base_dir, '2.Validation/src')
    process_json_files(valid_label_dir, valid_audio_dir, output_dir, 'valid')

if __name__ == "__main__":
    main()
