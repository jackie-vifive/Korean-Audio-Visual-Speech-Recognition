import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

aihub_id = os.environ.get('AIHUB_ID')
aihub_pw = os.environ.get('AIHUB_PW')

dataset_key = 538

file_keys = [
    # 54866,54867,54868,54869,54870,548671,54872,54873,54874,54875,54876,54877,54878
    # 54879,54880,54881,54882,54883,54884,54885
    # 54906, 54907, 54908, 54909, 54910, 54911, 54912, 54913
    54914, 54915, 54916, 54917, 54918, 54919, 54920, 54921
]



for file_key in file_keys:
    print(file_key)
    command = ["./aihubshell", "-mode", "d", "-datasetkey", str(dataset_key), "-filekey", str(file_key)]
    subprocess.run(command)
