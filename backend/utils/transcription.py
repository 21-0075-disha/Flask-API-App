from google.cloud import speech

def transcribe_audio(audio_filename):
    client = speech.SpeechClient()

    with open(audio_filename, 'rb') as audio_file:
        audio_content = audio_file.read()

    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US',
    )

    response = client.recognize(config=config, audio=audio)
    transcription = ' '.join([result.alternatives[0].transcript for result in response.results])
    
    return transcription
