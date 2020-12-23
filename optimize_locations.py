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
    
    if (location[0] - prev[0]) >= 50:
        locations[index] = prev
    if (location[1] - prev[1]) >= 50:
        locations[index] = prev
        
    prev = location

with open("locations.p", "wb") as f:
    pickle.dump(locations, f)
