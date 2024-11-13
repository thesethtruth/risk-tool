"""Initial migration

Revision ID: 86555293a85f
Revises: 17bf65762987
Create Date: 2024-11-13 18:09:58.618279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '86555293a85f'
down_revision: Union[str, None] = '17bf65762987'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('measures_ibfk_1', 'measures', type_='foreignkey')
    op.drop_column('measures', 'risk_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('measures', sa.Column('risk_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('measures_ibfk_1', 'measures', 'risks', ['risk_id'], ['id'])
    # ### end Alembic commands ###