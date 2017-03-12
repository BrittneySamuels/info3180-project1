"""empty message

Revision ID: 0594699df53c
Revises: 
Create Date: 2017-03-11 20:01:05.781038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0594699df53c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.String(length=8), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('biography', sa.String(length=255), nullable=True),
    sa.Column('gender', sa.String(length=7), nullable=True),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###
