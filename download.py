import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

aihub_id = os.environ.get('AIHUB_ID')
aihub_pw = os.environ.get('AIHUB_PW')

dataset_key = 538

file_keys = [
    55112, 55113, 55114, 55115, 55116, 55117, 55118, 551129
]


for file_key in file_keys:
    command = ["./aihubshell", "-mode", "d", "-datasetkey", str(dataset_key), "-filekey", str(file_key)]
    subprocess.run(command)
