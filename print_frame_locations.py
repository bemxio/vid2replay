import config as cf
import pickle
import os

with open("locations.p", "rb") as f:
    locations = pickle.load(f)

for frame, location in zip(os.listdir(cf.dir_name), locations):
    if not location:
        details = f"{frame}: No location found"
    else:
        details = f"{frame}: x = {location[0]}, y = {location[1]}"
    print(details)
