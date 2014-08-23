"""empty message

Revision ID: 1929550bddee
Revises: 3065d17fde08
Create Date: 2014-08-23 20:56:29.839154

"""

# revision identifiers, used by Alembic.
revision = '1929550bddee'
down_revision = '3065d17fde08'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['fb_id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user')
    ### end Alembic commands ###