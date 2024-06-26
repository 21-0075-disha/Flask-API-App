from .database import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    transcription = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(255))

def save_video_metadata(filename, transcription, tags):
    video = Video(filename=filename, transcription=transcription, tags=tags)
    db.session.add(video)
    db.session.commit()
