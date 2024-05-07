import os
import subprocess
import json
from hangul_romanize import Transliter
from hangul_romanize.rule import academic

load_dotenv()

aihub_id = os.environ.get('AIHUB_ID')
aihub_pw = os.environ.get('AIHUB_PW')

def korean_to_roman(korean_text):
    transliter = Transliter(academic)
    return transliter.translit(korean_text)

def download_and_process_tar_files(dataset_key, file_key_pairs, download_dir, output_dir):
    for label_key, source_key in file_key_pairs:
        label_download_command = f'/home/br2543/Korean-Audio-Visual-Speech-Recognition/aihubshell -mode d -datasetkey {dataset_key} -filekey {label_key}'
        source_download_command = f'/home/br2543/Korean-Audio-Visual-Speech-Recognition/aihubshell -mode d -datasetkey {dataset_key} -filekey {source_key}'
        subprocess.run(label_download_command, shell=True, cwd=download_dir)
        subprocess.run(source_download_command, shell=True, cwd=download_dir)

        for root, dirs, files in os.walk(download_dir):
            for file_name in files:
                if file_name.endswith('.tar'):
                    tar_file = os.path.join(root, file_name)
                    process_extracted_data(tar_file, output_dir)

def process_extracted_data(tar_file, output_dir):
    subprocess.run(['tar', '-xvf', tar_file, '-C', output_dir])

    for root, dirs, files in os.walk(output_dir, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            if file_name.endswith('.wav'):
                flac_file_path = file_path.replace('.wav', '.flac')
                subprocess.run(['flac', file_path])
                os.remove(file_path)

                transcript_file_path = flac_file_path.replace('.flac', '.txt')
                with open(transcript_file_path, 'w') as transcript_file:
                    json_file_path = file_path.replace('.wav', '.json').replace('/data/', '/data_label/')
                    try:
                        with open(json_file_path) as json_file:
                            transcript_data = json.load(json_file)
                            transcript = transcript_data['transcript']
                            transcript_file.write(transcript)
                    except FileNotFoundError:
                        print(f'JSON file not found for {file_path}')

            elif file_name.endswith('.mp4'):
                os.remove(file_path)

        for dir_name in dirs:
            new_dir_name = korean_to_roman(dir_name)
            os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))

    os.remove(tar_file)

def main():
    dataset_key = 538
    file_key_pairs = [
        (55080, 55112),  # VL1.tar and VS1.tar
        (55081, 55113),  # VL10.tar and VS10.tar
        (55082, 55114),  # VL11.tar and VS11.tar
        (55083, 55115),  # VL12.tar and VS12.tar
        (55084, 55116),  # VL13.tar and VS13.tar
        (55085, 55117),  # VL14.tar and VS14.tar
        (55086, 55118),  # VL15.tar and VS15.tar
        (55087, 55119),  # VL16.tar and VS16.tar
        (55088, 55120),  # VL17.tar and VS17.tar
        (55089, 55121),  # VL18.tar and VS18.tar
        (55090, 55122),  # VL19.tar and VS19.tar
        (55091, 55123),  # VL2.tar and VS2.tar
        (55092, 55124),  # VL20.tar and VS20.tar
        (55093, 55125),  # VL21.tar and VS21.tar
        (55094, 55126),  # VL22.tar and VS22.tar
        (55095, 55127),  # VL23.tar and VS23.tar
        (55096, 55128),  # VL24.tar and VS24.tar
        (55097, 55129),  # VL25.tar and VS25.tar
        (55098, 55130),  # VL26.tar and VS26.tar
        (55099, 55131),  # VL27.tar and VS27.tar
        (55100, 55132),  # VL28.tar and VS28.tar
        (55101, 55133),  # VL29.tar and VS29.tar
        (55102, 55134),  # VL3.tar and VS3.tar
        (55103, 55135),  # VL30.tar and VS30.tar
        (55104, 55136),  # VL31.tar and VS31.tar
        (55105, 55137),  # VL32.tar and VS32.tar
        (55106, 55138),  # VL4.tar and VS4.tar
        (55107, 55139),  # VL5.tar and VS5.tar
        (55108, 55140),  # VL6.tar and VS6.tar
        (55109, 55141),  # VL7.tar and VS7.tar
        (55110, 55142),  # VL8.tar and VS8.tar
        (55111, 55143)  # VL9.tar and VS9.tar
    ]

    download_dir = 'downloaded_data'
    output_dir = 'processed_data'

    os.makedirs(download_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    download_and_process_tar_files(dataset_key, file_key_pairs, download_dir, output_dir)

if __name__ == '__main__':
    main()
