from moviepy.editor import TextClip, concatenate_videoclips

clip1 = TextClip("FFmpeg is working!", fontsize=70, color='white', size=(640, 480)).set_duration(3)
clip1.write_videofile("test_output.mp4", fps=24)
