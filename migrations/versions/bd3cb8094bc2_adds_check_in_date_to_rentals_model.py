"""adds check-in-date to rentals model

Revision ID: bd3cb8094bc2
Revises: ed61ce7ae811
Create Date: 2021-05-21 15:14:13.220226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd3cb8094bc2'
down_revision = 'ed61ce7ae811'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rentals', sa.Column('check_in_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rentals', 'check_in_date')
    # ### end Alembic commands ###
