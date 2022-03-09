from application import app, db
from application.models import Albums, Songs, Listings
from application.forms import AddAlbum, AddSong, AddSongToAlbum, DeleteAlbum, EditSong
from flask import render_template, request, redirect, url_for

# route for home page listing, querying db tables
@app.route('/')
def index():
    albums = Albums.query.order_by(Albums.release_year).all()
    songs = Songs.query.all()
    listings = Listings.query.all()
    return render_template('index.html', albums = albums, songs = songs, listings = listings)

# route for adding album, album variable passes form data to submission as new entry
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

# route for adding song, song variable passes form data to submission as new entry
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

# route for linking many to many tables, for loops populate SelectFields and if statement creates db entry linking album and song id
@app.route('/addsongtoalbum', methods=['GET', 'POST'])
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
                album_id = form.album_id.data
            )
            db.session.add(listing)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('addsongtoalbum.html', form=form)

# route for deleting album, if statement takes id from SelectField and deletes entry from db
@app.route('/deletealbum', methods=['GET', 'POST', 'DELETE'])
def deletealbum():
    form = DeleteAlbum()

    albums = Albums.query.all()

    for album in albums:
        form.album_id.choices.append(
            (album.id, f"{album.album_name}")
        )

    if request.method == 'POST':
        if form.validate_on_submit():
            album = Albums.query.get(form.album_id.data)
            db.session.delete(album)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('delete.html', form=form)

# route for editing song, if statement takes song id and uses form data to overwrite on commit
@app.route('/editsong', methods=['GET', 'POST', 'PUT'])
def edit():
    form = EditSong()

    songs = Songs.query.all()

    for song in songs:
        form.song_id.choices.append(
            (song.id, f"{song.song_name} - {song.song_length}")
        )

    if request.method == 'POST':
        if form.validate_on_submit():
            song = Songs.query.get(form.song_id.data)
            song.song_name = form.new_song_name.data
            song.song_length = form.new_song_length.data
            db.session.commit()
            return redirect(url_for('index')) 

    return render_template('edit.html', form=form)

