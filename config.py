import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres://hwabivydkzlskf:0ac8a4cbb275bf218592e40b22dae4d2693618d74b63e93fc9761e461b6f61d6@ec2-44-198-80-194.compute-1.amazonaws.com:5432/db2g12mkfigind'
