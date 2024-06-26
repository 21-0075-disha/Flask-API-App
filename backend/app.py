from flask import Flask, request, jsonify
from google.cloud import speech
import ffmpeg
import os
import psycopg2
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure Google Cloud Speech-to-Text
speech_client = speech.SpeechClient()

# Define the connection parameters
dbname = "mydatabase"
user = "myuser"
password = "mypassword"
host = "localhost"
port = "5432"  # default PostgreSQL port

# Configure PostgreSQL connection
conn = psycopg2.connect("dbname=yourdbname user=youruser password=yourpassword host=yourhost")
cur = conn.cursor()

@app.route('/upload-video', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)

    # Save the video file locally
    file.save(filename)

    # Extract audio from video
    audio_filename = filename.rsplit('.', 1)[0] + '.wav'
    ffmpeg.input(filename).output(audio_filename).run()

    # Transcribe audio
    with open(audio_filename, 'rb') as audio_file:
        audio_content = audio_file.read()

    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US',
    )

    response = speech_client.recognize(config=config, audio=audio)

    transcription = ' '.join([result.alternatives[0].transcript for result in response.results])

    # Store video metadata in PostgreSQL
    cur.execute("INSERT INTO videos (filename, transcription) VALUES (%s, %s)", (filename, transcription))
    conn.commit()

    # Clean up local files
    os.remove(filename)
    os.remove(audio_filename)

    return jsonify({'filename': filename, 'transcription': transcription})

if __name__ == '__main__':
    app.run(debug=True)
