from PIL import Image
import config as cf
import pyscreeze
import pickle
import os

frames = os.listdir(cf.dir_name)
cursor = Image.open(cf.cursor_path)

locations = []
for frame in frames:
    img = Image.open(f"{cf.dir_name}/{frame}")
    location = pyscreeze.locate(cursor, img, confidence=cf.confidence)
    locations.append(location)
    if location:
        print(f"Located cursor in {frame}, x = {location[0]}, y = {location[1]}")
    else:
        print(f"No cursor found in {frame}, is this an error?")
    
print("Pickling locations of a cursor...")
with open("locations.p", "wb") as f:
    pickle.dump(locations, f)

print("Done! Run 'display_frames.pyw' to continue.")
