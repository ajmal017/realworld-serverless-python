"""Create profile-profile relationship

Revision ID: 6cd1ecc66c36
Revises: 738a04ab8395
Create Date: 2018-05-12 04:55:21.538463

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision = '6cd1ecc66c36'
down_revision = '738a04ab8395'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'profile-profile-association',
        sa.Column(
            'first-person-profile',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_profile.user-id')
        ),
        sa.Column(
            'second-person-profile',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_profile.user-id')
        )
    )


def downgrade():
    op.drop_table('profile-profile-association')
