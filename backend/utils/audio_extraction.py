import ffmpeg

def extract_audio(video_filename):
    audio_filename = video_filename.rsplit('.', 1)[0] + '.wav'
    ffmpeg.input(video_filename).output(audio_filename).run()
    return audio_filename
