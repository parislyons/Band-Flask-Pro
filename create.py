from application import db
from application.models import Albums, Songs, Listings

db.drop_all()
db.create_all()

# adds example albums to db
grooty = Albums(album_name='Grooty', release_year=2008) 
frooty = Albums(album_name='Frooty', release_year=2009) 
best = Albums(album_name='Best of Frooty and Grooty', release_year=2009) 
db.session.add(grooty)
db.session.add(frooty)
db.session.add(best)
db.session.commit()

# adds example songs to db
song1 = Songs(song_name='Song 1', song_length = '2:34')
song2 = Songs(song_name='Song 2', song_length = '4:44')
song3 = Songs(song_name='Song 3', song_length = '3:15')
db.session.add(song1)
db.session.add(song2)
db.session.add(song3)
db.session.commit()

# creates links between the albums and songs on Listings table
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
