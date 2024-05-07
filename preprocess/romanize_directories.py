import os
from hangul_romanize import Transliter
from hangul_romanize.rule import academic

def romanize_korean(text):
    transliter = Transliter(academic)
    romanized = transliter.translit(text)
    return romanized.replace(' ', '_')

def romanize_directories(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in dirs:
            try:
                original_path = os.path.join(root, name)
                romanized_name = '_'.join(romanize_korean(part) for part in name.split())
                new_path = os.path.join(root, romanized_name)
                os.rename(original_path, new_path)
                print(f"Renamed '{original_path}' to '{new_path}'")
            except Exception as e:
                print(f"Failed to rename {original_path}: {e}")

start_dir = '/home/jupyter/Korean-Audio-Visual-Speech-Recognition/data'
romanize_directories(start_dir)