"""table Billet

Revision ID: 9c23501f8e79
Revises: fc6985c7a5db
Create Date: 2019-11-24 11:22:03.031205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c23501f8e79'
down_revision = 'fc6985c7a5db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('billet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prix', sa.Integer(), nullable=True),
    sa.Column('idVoyage', sa.Integer(), nullable=True),
    sa.Column('idPlace', sa.Integer(), nullable=True),
    sa.Column('idClient', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idClient'], ['client.id'], ),
    sa.ForeignKeyConstraint(['idPlace'], ['place.id'], ),
    sa.ForeignKeyConstraint(['idVoyage'], ['voyage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('billet')
    # ### end Alembic commands ###
