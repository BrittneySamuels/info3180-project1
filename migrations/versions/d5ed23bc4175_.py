"""empty message

Revision ID: d5ed23bc4175
Revises: 66b0e90b7f2d
Create Date: 2017-03-11 21:37:49.999804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ed23bc4175'
down_revision = '66b0e90b7f2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('date', sa.Date(), nullable=True))
    op.add_column('user_profile', sa.Column('image', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'image')
    op.drop_column('user_profile', 'date')
    # ### end Alembic commands ###
