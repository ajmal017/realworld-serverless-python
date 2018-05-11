"""Create profile table

Revision ID: 586ff0a55152
Revises: 060c71f40c75
Create Date: 2018-05-12 03:39:41.737116

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision = '586ff0a55152'
down_revision = '060c71f40c75'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'conduit_api_profile',
        sa.Column(
            'user-id',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_user.uuid'),
            nullable=False,
        )
    )


def downgrade():
    op.drop_table('conduit_api_profile')
