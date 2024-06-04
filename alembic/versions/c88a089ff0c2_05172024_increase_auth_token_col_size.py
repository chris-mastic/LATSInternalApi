"""05172024_increase_auth_token_col_size

Revision ID: c88a089ff0c2
Revises: 91b507cf0a8e
Create Date: 2024-05-17 13:18:44.720151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'c88a089ff0c2'
down_revision: Union[str, None] = '91b507cf0a8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('noa_ltc_change_order', 'auth_token',
               existing_type=mysql.VARCHAR(length=32),
               type_=sa.String(length=256),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('noa_ltc_change_order', 'auth_token',
               existing_type=sa.String(length=256),
               type_=mysql.VARCHAR(length=32),
               existing_nullable=True)
    # ### end Alembic commands ###