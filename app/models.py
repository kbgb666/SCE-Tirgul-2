from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), index=True, unique=False)
    last_name = db.Column(db.String(120), index=True, unique=False)
    user_id = db.Column(db.Integer,unique= True )
    can_vote = db.Column(db.Boolean,unique=False )

    def __init__(self, first_name, last_name, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.can_vote = True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.first_name


class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    picture = db.Column(db.String(120), index=True, unique=False)
    voting_amount = db.Column(db.Integer, unique=False)

    def __init__(self, name, picture):
        self.name = name
        self.picture = picture
        self.voting_amount = 0

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<Party %r>' % self.name
