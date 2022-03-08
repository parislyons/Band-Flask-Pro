from application import db

class Albums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.String(30), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    listings = db.relationship('Listings', backref='album')

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(30), nullable=False)
    song_length = db.Column(db.String(5), nullable=False)
    listings = db.relationship('Listings', backref='song')

class Listings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column('songs_id', db.Integer, db.ForeignKey('songs.id'))
    album_id = db.Column('album_id', db.Integer, db.ForeignKey('albums.id'))
