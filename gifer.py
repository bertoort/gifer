import sys
from moviepy.editor import *

if __name__ == '__main__':
    try:
        video = sys.argv[1]
    except IndexError:
        video = "video.mov"
    try:
        gif = sys.argv[2]
    except IndexError:
        gif = "clip.gif"

    clip = VideoFileClip(video)
    clip = clip.resize(width=800)
    clip.write_gif(gif, fps=3)
