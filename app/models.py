from . import db

class UserProfile(db.Model):
    id = db.Column(db.String(8), primary_key=True, unique=True)
    date = db.Column(db.Date())
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    age = db.Column(db.Integer())
    biography = db.Column(db.String(225))
    gender = db.Column(db.String(7))
    image = db.Column(db.String(50))


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)