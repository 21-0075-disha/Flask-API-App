import whisper
from moviepy.editor import VideoFileClip

def extract_and_transcribe(video_filename):
    video_path = '/content/' + video_filename
    # Load the video
    video = VideoFileClip(video_path)
    # Extract audio
    audio = video.audio
    # Save to a path
    audio_path = '/content/audio/audio.mp3'
    audio.write_audiofile(audio_path)
    print(f'Audio file saved at {audio_path}')

    # Load required Whisper model
    model = whisper.load_model("base")

    # Transcribe audio file
    result = model.transcribe(audio_path)

    transcript = result['text']
    return transcript
