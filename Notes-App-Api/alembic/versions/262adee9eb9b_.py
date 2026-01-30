"""empty message

Revision ID: 262adee9eb9b
Revises: c79deeae9b5b
Create Date: 2026-01-29 13:44:56.312583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '262adee9eb9b'
down_revision: Union[str, Sequence[str], None] = 'c79deeae9b5b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table("notes") as batch_op:
        batch_op.add_column(
            sa.Column("user_id", sa.Integer(), nullable=False)
        )
        batch_op.create_foreign_key(
            "fk_notes_user_id",
            "users",
            ["user_id"],
            ["id"]
        )
def downgrade():
    with op.batch_alter_table("notes") as batch_op:
        batch_op.drop_constraint(
            "fk_notes_user_id",
            type_="foreignkey"
        )
        batch_op.drop_column("user_id")
