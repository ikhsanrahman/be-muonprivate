"""empty message

Revision ID: 584a47abe698
Revises: b6094872c96b
Create Date: 2019-07-19 18:06:21.607615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '584a47abe698'
down_revision = 'b6094872c96b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tutors', sa.Column('gender', sa.String(length=100), nullable=True))
    op.add_column('tutors', sa.Column('phone_number', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tutors', 'phone_number')
    op.drop_column('tutors', 'gender')
    # ### end Alembic commands ###
