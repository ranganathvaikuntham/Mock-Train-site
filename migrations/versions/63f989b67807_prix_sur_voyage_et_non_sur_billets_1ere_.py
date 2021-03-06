"""Prix sur voyage et non sur billets, 1ere et 2nde classes

Revision ID: 63f989b67807
Revises: c1b88a431134
Create Date: 2019-11-26 18:15:23.196931

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '63f989b67807'
down_revision = 'c1b88a431134'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('billet', 'prix')
    op.add_column('voiture', sa.Column('classe1', sa.Boolean(), nullable=True))
    op.add_column('voyage', sa.Column('prixClasse1', sa.Float(), nullable=True))
    op.add_column('voyage', sa.Column('prixClasse2', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('voyage', 'prixClasse2')
    op.drop_column('voyage', 'prixClasse1')
    op.drop_column('voiture', 'classe1')
    op.add_column('billet', sa.Column('prix', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
