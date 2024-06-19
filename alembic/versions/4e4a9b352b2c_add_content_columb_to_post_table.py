"""add content columb to post table

Revision ID: 4e4a9b352b2c
Revises: 4a22847ac35c
Create Date: 2024-06-19 09:55:48.831125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e4a9b352b2c'
down_revision: Union[str, None] = '4a22847ac35c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
