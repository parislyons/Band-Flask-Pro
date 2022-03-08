from app import db, Albums, Songs, Listings

db.drop_all()
db.create_all()

grooty = Albums(album_name='Grooty', release_year=2008) # Extra: this section populates the table with an example entry
frooty = Albums(album_name='Frooty', release_year=2009) # Extra: this section populates the table with an example entry
best = Albums(album_name='Best of Frooty and Grooty', release_year=2009) # Extra: this section populates the table with an example entry
db.session.add(grooty)
db.session.add(frooty)
db.session.commit()

song1 = Songs(song_name='Song 1', song_length = '2:34')
song2 = Songs(song_name='Song 2', song_length = '4:44')
song3 = Songs(song_name='Song 3', song_length = '3:15')
db.session.add(song1)
db.session.add(song2)
db.session.add(song3)
db.session.commit()

lsong1 = Listings(song_id=1, album_id=1)
lsong2 = Listings(song_id=2, album_id=1)
lsong3 = Listings(song_id=3, album_id=2)
lsong4 = Listings(song_id=1, album_id=3)
lsong5 = Listings(song_id=3, album_id=3)
db.session.add(lsong1)
db.session.add(lsong2)
db.session.add(lsong3)
db.session.add(lsong4)
db.session.add(lsong5)
db.session.commit()
