"""Add index on visit purpose

Revision ID: e1fa93fd61eb
Revises: 1d49ba9b4131
Create Date: 2025-01-13 11:47:17.677261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1fa93fd61eb'
down_revision: Union[str, None] = '1d49ba9b4131'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_index("idx_visit_purpose", "visit", ["purpose"])


def downgrade() -> None:
    op.drop_index("idx_visit_purpose", table_name="visit")
