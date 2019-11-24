"""table Place

Revision ID: fc6985c7a5db
Revises: bf9d6347702d
Create Date: 2019-11-23 17:28:05.686543

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fc6985c7a5db'
down_revision = 'bf9d6347702d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('place',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numPlace', sa.Integer(), nullable=True),
    sa.Column('idVoiture', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idVoiture'], ['voiture.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('voiture', 'nbPlaces')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('voiture', sa.Column('nbPlaces', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_table('place')
    # ### end Alembic commands ###
