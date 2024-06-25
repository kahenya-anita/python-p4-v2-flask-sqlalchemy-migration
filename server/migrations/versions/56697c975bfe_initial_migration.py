"""Initial migration

Revision ID: 56697c975bfe
Revises: 
Create Date: 2024-06-25 02:14:20.082875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56697c975bfe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###