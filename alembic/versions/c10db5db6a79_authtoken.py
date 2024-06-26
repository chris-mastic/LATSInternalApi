"""authtoken

Revision ID: c10db5db6a79
Revises: f95b3a0779a9
Create Date: 2024-04-26 14:36:53.387955

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c10db5db6a79'
down_revision: Union[str, None] = 'f95b3a0779a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('noa_ltc_change_order', sa.Column('auth_token', sa.String(length=32), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('noa_ltc_change_order', 'auth_token')
    # ### end Alembic commands ###
