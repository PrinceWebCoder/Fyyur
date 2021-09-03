"""empty message

Revision ID: f13ba75a1041
Revises: f36f2ae784b3
Create Date: 2021-06-30 22:51:53.334447

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f13ba75a1041'
down_revision = 'f36f2ae784b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artist')
    op.drop_table('venue')
    op.drop_table('show')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='show_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='show_venue_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='show_pkey')
    )
    op.create_table('venue',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('seeking_description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('genres', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='venue_pkey')
    )
    op.create_table('artist',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('seeking_venue', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('seeking_description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('genres', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='artist_pkey')
    )
    # ### end Alembic commands ###
