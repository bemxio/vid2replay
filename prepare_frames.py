import config as cf
import os

os.mkdir(cf.dir_name)
print("Extracting frames from a video...")
os.system(f"ffmpeg -i {cf.input_video} {cf.dir_name}/frame%04d.png -hide_banner")

print("Sorting all frames...")
frames = os.listdir(cf.dir_name)
if cf.start or cf.end:
    n1, n2 = cf.start * cf.fps, cf.end * cf.fps
    framesf = frames[n1:n2]
    for frame in frames:
        if frame not in framesf:
            print(f"Deleting frame {frame}...")
            os.remove(f"{cf.dir_name}/{frame}")

print("Done! Run 'analyze_frames.py' to continue.")




