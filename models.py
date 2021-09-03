from flask_sqlalchemy import SQLAlchemy


database_path = 'postgresql://hwabivydkzlskf:0ac8a4cbb275bf218592e40b22dae4d2693618d74b63e93fc9761e461b6f61d6@ec2-44-198-80-194.compute-1.amazonaws.com:5432/db2g12mkfigind'


db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()



class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String)
    shows = db.relationship('Show', backref="venue", lazy='joined')
    genres = db.Column(db.ARRAY(db.String()),nullable=False)

    
    def __repr__(self):
      return f'<Venue {self.id} {self.name}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate ✓

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)
    city = db.Column(db.String(120),nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120),nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String)
    genres = db.Column(db.ARRAY(db.String()),nullable=False)
    shows = db.relationship('Show', backref="artist", lazy="joined")

    def __repr__(self):
      return f'<Artist {self.id} {self.name}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate ✓

class Show(db.Model):
  __tablename__ = 'show'
  
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'),nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'),nullable=False)
  start_time = db.Column(db.DateTime, nullable=False)
  
  def __repr__(self):
    return f'<Show {self.venue_id} {self.artist_id}>'
