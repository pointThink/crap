import sys
import os
import datetime
from PIL import Image
import shutil

folder = sys.argv[1]
folder_contents = os.listdir(folder)

years = {}

for file in folder_contents:
    if file.startswith(".") or os.path.isdir(f"{folder}/{file}"):
        continue

    creation_time = os.path.getmtime(f"{folder}/{file}")
    creation_date = datetime.datetime.fromtimestamp(creation_time).year
    
    if not creation_date in years.keys():
        years[creation_date] = []

    years[creation_date].append(f"{folder}/{file}")

for key in years:
    if not os.path.isdir(f"{folder}/{key}"):
        os.mkdir(f"{folder}/{key}")

    print(f"{key}: {len(years[key])} images")

    for file in years[key]:
        # print(f"{file}")
        shutil.move(f"{file}", f"{folder}/{key}/{os.path.basename(file)}")
