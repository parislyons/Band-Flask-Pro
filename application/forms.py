from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from application.models import Songs, Albums, Listings

class AddAlbum(FlaskForm):
    album_name = StringField('Album Name', validators=[DataRequired(), Length(min=2,max=30)])
    release_year = IntegerField('Release Year', validators=[DataRequired()])
    submit = SubmitField('Add Album')

class AddSong(FlaskForm):
    song_name = StringField('Song Name', validators=[DataRequired(), Length(min=2,max=30)])
    song_length = StringField('Song Length', validators=[DataRequired(), Length(min=4,max=5)])
    submit = SubmitField('Add Song')

class AddSongToAlbum(FlaskForm):
    song_id = SelectField('Pick Song', choices=[])
    album_id = SelectField('Pick Album', choices=[])
    submit = SubmitField('Add Song to Album')

class DeleteAlbum(FlaskForm):
    album_id = SelectField('Pick Album', choices=[])
    submit = SubmitField('Delete Album')

class EditSong(FlaskForm):
    song_id = SelectField('Pick Song', choices=[])
    new_song_name = StringField('Song Name', validators=[DataRequired(), Length(min=2,max=30)]) 
    new_song_length = StringField('Song Length', validators=[DataRequired(), Length(min=4,max=5)])
    submit = SubmitField('Edit Song')