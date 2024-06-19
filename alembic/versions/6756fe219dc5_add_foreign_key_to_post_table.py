"""add foreign key to post table

Revision ID: 6756fe219dc5
Revises: ebb7a039cc55
Create Date: 2024-06-19 10:23:31.369157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6756fe219dc5'
down_revision: Union[str, None] = 'ebb7a039cc55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_user_fk',source_table = "posts", referent_table='users', local_cols=['owner_id'], remote_cols=['id'],
                          ondelete = "CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_user_fk', table_name="posts")
    op.drop_column('posts','owner_id')
    pass
