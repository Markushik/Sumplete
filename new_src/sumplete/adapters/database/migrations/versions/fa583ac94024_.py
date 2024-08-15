"""empty message

Revision ID: fa583ac94024
Revises: 
Create Date: 2024-08-15 12:09:58.442709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'fa583ac94024'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puzzles',
    sa.Column('puzzle_id', sa.Integer(), nullable=False),
    sa.Column('size', sa.SmallInteger(), nullable=False),
    sa.Column('score', sa.SmallInteger(), nullable=False),
    sa.Column('complexity', sa.String(length=10), nullable=False),
    sa.Column('sample', postgresql.ARRAY(sa.SmallInteger(), dimensions=1, zero_indexes=True), nullable=False),
    sa.Column('original', postgresql.ARRAY(sa.SmallInteger(), dimensions=1, zero_indexes=True), nullable=False),
    sa.Column('zeroed', postgresql.ARRAY(sa.SmallInteger(), dimensions=1, zero_indexes=True), nullable=False),
    sa.Column('modified', postgresql.ARRAY(sa.SmallInteger(), dimensions=1, zero_indexes=True), nullable=False),
    sa.Column('vertical', postgresql.ARRAY(sa.SmallInteger(), dimensions=1, zero_indexes=True), nullable=False),
    sa.Column('horizontal', postgresql.ARRAY(sa.SmallInteger(), dimensions=1, zero_indexes=True), nullable=False),
    sa.PrimaryKeyConstraint('puzzle_id', name=op.f('pk_puzzles'))
    )
    op.create_table('users',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('user_name', sa.String(length=32), nullable=True),
    sa.Column('locale', sa.String(length=2), nullable=False),
    sa.Column('anncmt', sa.String(length=5), nullable=False),
    sa.Column('style', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('user_id', name=op.f('pk_users'))
    )
    op.create_table('profile',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('scores', sa.Integer(), nullable=False),
    sa.Column('solved_3x3', sa.Integer(), nullable=False),
    sa.Column('solved_4x4', sa.Integer(), nullable=False),
    sa.Column('solved_5x5', sa.Integer(), nullable=False),
    sa.Column('solved_6x6', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name=op.f('fk_profile_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', name=op.f('pk_profile'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    op.drop_table('users')
    op.drop_table('puzzles')
    # ### end Alembic commands ###