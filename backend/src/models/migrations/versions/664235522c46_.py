"""empty message

Revision ID: 664235522c46
Revises: ed2f81414346
Create Date: 2020-08-29 00:04:01.355835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '664235522c46'
down_revision = 'ed2f81414346'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
