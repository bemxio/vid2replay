### Settings for a "cursor tracing" visualization. ###

input_video = "input.mp4"   # name of a video to process
dir_name = "TEMP"   # directory name in which the frames will be extracted
cursor_path = "cursor.png"   # path to a cursor png to locate in frames

fps = 60   # fps of a video
start = 0   # start point (in seconds) of a video, set to 0 if not specified
end = 60   # end point (in seconds) of a video, set to 0 if not specified

video_resolution = (1920, 1080) # resolution of a input video
pygame_resolution = (960, 540) # resolution of a visualization in pygame
confidence = 0.4 # confidence in searchng for a cursor
