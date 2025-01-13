"""Add column on ship

Revision ID: 1d49ba9b4131
Revises: 
Create Date: 2025-01-13 11:45:32.408217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d49ba9b4131'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("ship", sa.Column("crew", sa.Integer(), nullable=False, server_default="0"))


def downgrade() -> None:
    op.drop_column("ship", "crew")
