from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Albums, Songs, Listings

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        album = Albums(album_name="Lipgloss",  release_year=2000)
        db.session.add(album)
        song = Songs(song_name="Cherry", song_length="2:30")
        db.session.add(song)
        listing = Listings(album_id=1,  song_id=1)
        db.session.add(listing)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)
    
    def test_add_album_get(self):
        response = self.client.get(url_for('addalbum'))
        self.assert200(response)

    def test_add_song_get(self):
        response = self.client.get(url_for('addsong'))
        self.assert200(response)

    def test_add_song_to_album_get(self):
        response = self.client.get(url_for('addsongtoalbum'))
        self.assert200(response)

    def test_delete_album_get(self):
        response = self.client.get(url_for('deletealbum'))
        self.assert200(response)

    def test_edit_song_get(self):
        response = self.client.get(url_for('edit'))
        self.assert200(response)

class TestRead(TestBase):

    def test_read_home_tasks(self):
        response = self.client.get(url_for('index'))
        self.assertIn(b"Lipgloss", response.data)


class TestAdd(TestBase):

    def test_add_album_task(self):
        response = self.client.post(
            url_for('addalbum'),
            data={"album_name": "Fresh", "release_year": 2000},
            follow_redirects=True
        )
        new_album = Albums.query.get(2)
        self.assertEquals(new_album.album_name, "Fresh")

    def test_add_song_task(self):
        response = self.client.post(
            url_for('addsong'),
            data={"song_name": "Test Song", "song_length": "2:59"},
            follow_redirects=True
        )
        new_song = Songs.query.get(2)
        self.assertEquals(new_song.song_name, "Test Song")
        self.assertIn(b"Test Song", response.data)
    
    def test_add_song_to_album_task(self):
        song = Songs(song_name="Lime", song_length="4:30")
        db.session.add(song)
        db.session.commit()
        response = self.client.post(
            url_for('addsongtoalbum'),
            data={"song_id": 2, "album_id": 1},
            follow_redirects=True
        )
        self.assertIn(b"Lime", response.data)
    
class TestUpdate(TestBase):

    def test_edit_song_task(self):
        response = self.client.post(
            url_for('edit'),
            data={"song_id": "1", "new_song_name": "Edit Song", "new_song_length": "3:01"},
            follow_redirects=True
        )
        self.assertIn(b"Edit Song", response.data)

class TestDelete(TestBase):

    def test_delete_album_task(self):
        response = self.client.post(
            url_for('deletealbum'),
            data={"album_id": 1},
            follow_redirects=True
        )
        self.assertNotIn(b"Lipgloss", response.data)
