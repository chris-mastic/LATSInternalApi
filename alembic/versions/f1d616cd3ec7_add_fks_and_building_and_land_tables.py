"""add fks and building and land tables

Revision ID: f1d616cd3ec7
Revises: 41e64207b15a
Create Date: 2024-05-14 15:53:42.113151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'f1d616cd3ec7'
down_revision: Union[str, None] = '41e64207b15a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('noa_ltc_change_order_building',
    sa.Column('ltc_sub_class_old', sa.String(length=10), nullable=True),
    sa.Column('ltc_sub_class_new', sa.String(length=10), nullable=True),
    sa.Column('quantity_old', sa.Integer(), nullable=True),
    sa.Column('quantity_new', sa.Integer(), nullable=True),
    sa.Column('units_old', sa.String(length=1), nullable=True),
    sa.Column('units_new', sa.String(length=1), nullable=True),
    sa.Column('other_exempt_old', sa.Integer(), nullable=True),
    sa.Column('other_exempt_new', sa.Integer(), nullable=True),
    sa.Column('value_old_total', sa.Integer(), nullable=True),
    sa.Column('value_new_total', sa.Integer(), nullable=True),
    sa.Column('value_old_hs', sa.Integer(), nullable=True),
    sa.Column('value_new_hs', sa.Integer(), nullable=True),
    sa.Column('value_old_tp', sa.Integer(), nullable=True),
    sa.Column('value_new_tp', sa.Integer(), nullable=True),
    sa.Column('noaltc_change_order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['noaltc_change_order_id'], ['noa_ltc_change_order.id'], ),
    sa.PrimaryKeyConstraint('noaltc_change_order_id')
    )
    op.create_table('noa_ltc_change_order_land',
    sa.Column('ltc_sub_class_old', sa.String(length=10), nullable=True),
    sa.Column('ltc_sub_class_new', sa.String(length=10), nullable=True),
    sa.Column('quantity_old', sa.Integer(), nullable=True),
    sa.Column('quantity_new', sa.Integer(), nullable=True),
    sa.Column('units_old', sa.String(length=1), nullable=True),
    sa.Column('units_new', sa.String(length=1), nullable=True),
    sa.Column('other_exempt_old', sa.Integer(), nullable=True),
    sa.Column('other_exempt_new', sa.Integer(), nullable=True),
    sa.Column('value_old_total', sa.Integer(), nullable=True),
    sa.Column('value_new_total', sa.Integer(), nullable=True),
    sa.Column('value_old_hs', sa.Integer(), nullable=True),
    sa.Column('value_new_hs', sa.Integer(), nullable=True),
    sa.Column('value_old_tp', sa.Integer(), nullable=True),
    sa.Column('value_new_tp', sa.Integer(), nullable=True),
    sa.Column('noaltc_change_order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['noaltc_change_order_id'], ['noa_ltc_change_order.id'], ),
    sa.PrimaryKeyConstraint('noaltc_change_order_id')
    )
    op.drop_table('noa_parid_change_orders')
    op.add_column('noa_ltc_change_order', sa.Column('parcel_address', sa.String(length=50), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('restoration_tax_exepmt', sa.String(length=1), nullable=True))
    op.drop_column('noa_ltc_change_order', 'id_com')
    op.drop_column('noa_ltc_change_order', 'restoration_tax_expmt')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('noa_ltc_change_order', sa.Column('restoration_tax_expmt', mysql.VARCHAR(length=1), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('id_com', mysql.VARCHAR(length=25), nullable=True))
    op.drop_column('noa_ltc_change_order', 'restoration_tax_exepmt')
    op.drop_column('noa_ltc_change_order', 'parcel_address')
    op.create_table('noa_parid_change_orders',
    sa.Column('parid', mysql.TEXT(), nullable=True),
    sa.Column('jur', mysql.TEXT(), nullable=True),
    sa.Column('val01', mysql.TEXT(), nullable=True),
    sa.Column('val02', mysql.TEXT(), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('noa_ltc_change_order_land')
    op.drop_table('noa_ltc_change_order_building')
    # ### end Alembic commands ###