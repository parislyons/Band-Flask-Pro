from application import app, db
from application.models import Albums, Songs, Listings
from application.forms import AddAlbum, AddSong, AddSongToAlbum
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addalbum', methods=['GET', 'POST', 'PUT'])
def addalbum():
    form = AddAlbum()

    if request.method == 'POST':
        if form.validate_on_submit():
            album = Albums(
                album_name = form.album_name.data,
                release_year = form.release_year.data
            )
            db.session.add(album)
            db.session.commit()
            return redirect(url_for('addsong'))

    return render_template('addalbum.html', form=form)

@app.route('/addsong', methods=['GET', 'POST', 'PUT'])
def addsong():
    form = AddSong()

    if request.method == 'POST':
        if form.validate_on_submit():
            song = Songs(
                song_name = form.song_name.data,
                song_length = form.song_length.data
            )
            db.session.add(song)
            db.session.commit()
            return redirect(url_for('addsongtoalbum'))

    return render_template('addsong.html', form=form)

@app.route('/addsongtoalbum', methods=['GET', 'POST', 'PUT'])
def addsongtoalbum():
    form = AddSongToAlbum()

    albums = Albums.query.all()
    songs = Songs.query.all()

    for album in albums:
        form.album_id.choices.append(
            (album.id, f"{album.album_name}")
        )

    for song in songs:
        form.song_id.choices.append(
            (song.id, f"{song.song_name}")
        )

    if request.method == 'POST':
        if form.validate_on_submit():
            listing = Listings(
                song_id = form.song_id.data,
                album = form.album_id.data
            )
            db.session.add(listing)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('addsongtoalbum.html', form=form)

@app.route('/edit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def edit():
    return render_template('edit.html')

