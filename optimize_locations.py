import config as cf
import pickle
import os

with open("locations.p", "rb") as f:
    locations = pickle.load(f)

prev = None
for index, location in enumerate(locations):
    if not prev:
        prev = location
        continue
    if not location:
        locations[index] = prev
        continue
    
    if (location[0] - prev[0]) >= cf.max_limit or (location[1] - prev[1]) >= cf.max_limit:
        locations[index] = prev
        
    prev = location

with open("locations.p", "wb") as f:
    pickle.dump(locations, f)
