import pandas as pd 
import json
# from io import StringIO

# df = pd.read_json(StringIO("Video_Games.json"), lines=True)
# print(pd)

with open('/Users/franM/projects/sparkdev_AI/AI-Fall-2020/Video_Games.json') as f:  #change to file directory for the json file
    chunks = pd.read_json(f, lines=True, chunksize=100)
    for c in chunks:
        print(c)