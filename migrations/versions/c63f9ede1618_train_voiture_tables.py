"""Train, Voiture tables

Revision ID: c63f9ede1618
Revises: ead0c67d8a05
Create Date: 2019-11-22 14:34:23.248233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c63f9ede1618'
down_revision = 'ead0c67d8a05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('train',
    sa.Column('numTrain', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('numTrain')
    )
    op.create_table('voiture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numVoiture', sa.Integer(), nullable=True),
    sa.Column('nbPlacesDispos', sa.Integer(), nullable=True),
    sa.Column('numTrain', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['numTrain'], ['train.numTrain'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voiture')
    op.drop_table('train')
    # ### end Alembic commands ###
