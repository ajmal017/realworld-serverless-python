"""Create article-tag relationship

Revision ID: b3711b2a949c
Revises: 187ee66c9910
Create Date: 2018-05-12 05:16:44.580529

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision = 'b3711b2a949c'
down_revision = '187ee66c9910'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'article-tag-association',
        sa.Column(
            'article-id',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_article.uuid')
        ),
        sa.Column(
            'tag-id',
            sa.Integer,
            sa.ForeignKey('conduit_api_tag.id')
        )
    )


def downgrade():
    op.drop_table('article-tag-association')
