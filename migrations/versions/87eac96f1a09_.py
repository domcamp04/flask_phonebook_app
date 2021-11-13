"""empty message

Revision ID: 87eac96f1a09
Revises: 47bd328088bb
Create Date: 2021-11-12 20:34:11.947917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87eac96f1a09'
down_revision = '47bd328088bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phonebook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=False),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('phone', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('occupation', sa.String(length=150), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('phone_book_entry')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phone_book_entry',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), nullable=False),
    sa.Column('phone_number', sa.VARCHAR(length=50), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone_number')
    )
    op.drop_table('phonebook')
    # ### end Alembic commands ###