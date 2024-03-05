"""added currency table

Revision ID: b185f62c3173
Revises: d6c512318f80
Create Date: 2024-03-05 16:28:11.399549

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b185f62c3173'
down_revision: Union[str, None] = 'd6c512318f80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted', sa.Boolean(), server_default='f', nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('code', sa.String(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('account', sa.Column('timestamp', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('account', sa.Column('deleted', sa.Boolean(), server_default='f', nullable=True))
    op.add_column('account', sa.Column('balance', sa.DECIMAL(), nullable=True))
    op.add_column('account', sa.Column('currency_id', sa.Integer(), nullable=True))
    op.create_foreign_key("FK_currency_account", 'account', 'currency', ['currency_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("FK_currency_account", 'account', type_='foreignkey')
    op.drop_column('account', 'currency_id')
    op.drop_column('account', 'balance')
    op.drop_column('account', 'deleted')
    op.drop_column('account', 'timestamp')
    op.drop_table('currency')
    # ### end Alembic commands ###
