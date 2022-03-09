from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Albums, Songs, Listings

class TestBase(TestCase):
    def createapp(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='SQLITE:///data.db',
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setup(self):
        db.create_all()
        db.session.add(Albums)
        db.session.add(Songs)
        db.session.add(Listings)
        db.session.commit()

    def teardown(self):
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
        response = self.client.get(url_for('editsong'))
        self.assert200(response)

class TestRead(TestBase):

    def test_read_home_tasks(self):
        response = self.client.get(url_for('index'))
        self.assertIn(b"Run unit tests", response.data)


class TestAdd(TestBase):

    def test_add_album_task(self):
        response = self.client.post(
            url_for('addalbum'),
            data={"album_name": "Test"},
            data={"release_date": "2000"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)

    def test_add_song_task(self):
        response = self.client.post(
            url_for('addsong'),
            data={"song_name": "Test Song"},
            data={"song_length": "2:59"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
    
    def test_add_song_to_album_task(self):
        response = self.client.post(
            url_for('addsongtoalbum'),
            data={"song_id": "1"},
            data={"album_id": "1"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
    
class TestUpdate(TestBase):

    def test_edit_song_task(self):
        response = self.client.post(
            url_for('editsong'),
            data={"song_id": "1"},
            data={"new_song_name": "Edit Song"},
            data={"new_song_length": "3:01"},
            follow_redirects=True
        )
        self.assertIn(b"Testing update functionality", response.data)

class TestDelete(TestBase):

    def test_delete_album_task(self):
        response = self.client.get(
            url_for('deletealbum'),
            data={"album_id": "1"},
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data)
