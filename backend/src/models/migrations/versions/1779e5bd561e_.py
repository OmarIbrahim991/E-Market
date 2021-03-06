"""empty message

Revision ID: 1779e5bd561e
Revises: 
Create Date: 2020-08-26 22:22:00.251600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1779e5bd561e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=False, server_default="customer"),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=False, server_default="false"),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
