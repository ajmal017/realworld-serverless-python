"""Create profile-article relationship

Revision ID: ce5457ef45d6
Revises: 6cd1ecc66c36
Create Date: 2018-05-12 04:59:18.521528

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision = 'ce5457ef45d6'
down_revision = '6cd1ecc66c36'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'profile-article-association',
        sa.Column(
            'profile-id',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_profile.user-id')
        ),
        sa.Column(
            'article-id',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_article.uuid')
        )
    )


def downgrade():
    op.drop_table('profile-article-association')
