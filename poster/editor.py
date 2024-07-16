import random
import os
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from subtitle_generator import make_subtitles, generate_subtitles_file


def editor():
    video_files = os.listdir('video')

    selected_video = random.choice(video_files)


    tts_clip = AudioFileClip('tts_audio.mp3')

    audio_duration = tts_clip.duration

    video_clip_full = VideoFileClip('video/' + selected_video).resize((1080, 1920))
    video_clip_full = video_clip_full.without_audio()

    aspect_ratio_target = 9 / 16
    aspect_ratio_video = video_clip_full.w / video_clip_full.h

    if aspect_ratio_video > aspect_ratio_target:
        new_height = 1920
        new_width = int(video_clip_full.w * (1920 / video_clip_full.h))
    else:
        new_width = 1080
        new_height = int(video_clip_full.h * (1080 / video_clip_full.w))

    resized_clip = video_clip_full.resize((new_width, new_height))

    final_clip = resized_clip.crop(width=1080, height=1920, x_center=resized_clip.w / 2, y_center=resized_clip.h / 2)

    max_start_time = max(0, video_clip_full.duration - audio_duration)
    start_time = random.uniform(0, max_start_time)

    video_clip = final_clip.subclip(start_time, start_time + audio_duration)

    audio_clip = CompositeAudioClip([tts_clip])

    language, segments = make_subtitles()
    subtitles = generate_subtitles_file(language, segments)

    video_clip = video_clip.set_audio(audio_clip)
    generator = lambda txt: TextClip(txt, font="arial", fontsize=50, color="white", method='caption', size=video_clip.size)

    sub_clip = SubtitlesClip('brainrot.en.srt', generator)

    final_video_clip = CompositeVideoClip((video_clip, sub_clip), size=video_clip.size)
    final_video_clip.write_videofile('final_clip_with_subtitles.mp4')

    print('complete.')
