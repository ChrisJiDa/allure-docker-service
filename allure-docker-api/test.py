import json
from datetime import datetime

def get_file_as_string(path_file):
    file = None
    content = None
    try:
        file = open(path_file, "r")
        content = file.read()
    finally:
        if file is not None:
            file.close()
    return content

with open('C:/baidu/behaviors.json') as f:
    json_content = json.load(f)

y = int(str(json_content['children'][0]['children'][0]['children'][0]['time']['start'])[0:10])
start_time = datetime.fromtimestamp(y)
print(start_time)
print(y)