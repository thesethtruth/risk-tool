"""Initial migration

Revision ID: bc075d64e7f6
Revises: 
Create Date: 2024-11-13 17:35:05.815664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'bc075d64e7f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('measures', sa.Column('owner', sa.String(length=255), nullable=True))
    op.add_column('measures', sa.Column('deadline', sa.Date(), nullable=True))
    op.add_column('measures', sa.Column('status', sa.String(length=255), nullable=True))
    op.drop_column('measures', 'description')
    op.add_column('risks', sa.Column('cause', sa.String(length=255), nullable=True))
    op.add_column('risks', sa.Column('consequence', sa.String(length=255), nullable=True))
    op.add_column('risks', sa.Column('phase', sa.String(length=255), nullable=True))
    op.add_column('risks', sa.Column('theme', sa.String(length=255), nullable=True))
    op.add_column('risks', sa.Column('allocation', sa.String(length=255), nullable=True))
    op.add_column('risks', sa.Column('responsible', sa.String(length=255), nullable=True))
    op.add_column('risks', sa.Column('status', sa.String(length=255), nullable=True))
    op.add_column('rubrics', sa.Column('name', sa.String(length=255), nullable=True))
    op.add_column('rubrics', sa.Column('description', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_rubrics_name'), 'rubrics', ['name'], unique=False)
    op.add_column('scorings', sa.Column('likelihood', sa.Integer(), nullable=True))
    op.add_column('scorings', sa.Column('geld', sa.Integer(), nullable=True))
    op.add_column('scorings', sa.Column('tijd', sa.Integer(), nullable=True))
    op.add_column('scorings', sa.Column('kwaliteit', sa.Integer(), nullable=True))
    op.add_column('scorings', sa.Column('omgeving', sa.Integer(), nullable=True))
    op.add_column('scorings', sa.Column('veiligheid', sa.Integer(), nullable=True))
    op.add_column('scorings', sa.Column('imago', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('scorings', 'imago')
    op.drop_column('scorings', 'veiligheid')
    op.drop_column('scorings', 'omgeving')
    op.drop_column('scorings', 'kwaliteit')
    op.drop_column('scorings', 'tijd')
    op.drop_column('scorings', 'geld')
    op.drop_column('scorings', 'likelihood')
    op.drop_index(op.f('ix_rubrics_name'), table_name='rubrics')
    op.drop_column('rubrics', 'description')
    op.drop_column('rubrics', 'name')
    op.drop_column('risks', 'status')
    op.drop_column('risks', 'responsible')
    op.drop_column('risks', 'allocation')
    op.drop_column('risks', 'theme')
    op.drop_column('risks', 'phase')
    op.drop_column('risks', 'consequence')
    op.drop_column('risks', 'cause')
    op.add_column('measures', sa.Column('description', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('measures', 'status')
    op.drop_column('measures', 'deadline')
    op.drop_column('measures', 'owner')
    # ### end Alembic commands ###
