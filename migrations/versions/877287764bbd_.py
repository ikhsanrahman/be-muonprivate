"""empty message

Revision ID: 877287764bbd
Revises: a830d4e37073
Create Date: 2019-07-21 11:08:32.255330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '877287764bbd'
down_revision = 'a830d4e37073'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('is_working', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'is_working')
    # ### end Alembic commands ###
