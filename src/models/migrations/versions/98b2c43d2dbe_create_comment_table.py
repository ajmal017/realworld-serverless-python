"""Create comment table

Revision ID: 98b2c43d2dbe
Revises: f5ef6affc65c
Create Date: 2018-05-12 04:47:36.778387

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision = '98b2c43d2dbe'
down_revision = 'f5ef6affc65c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'conduit_api_comment',
        sa.Column(
            'id',
            sa.Integer,
            autoincrement=True,
            primary_key=True,
            nullable=False,
            unique=True
        ),
        sa.Column(
            'body',
            sa.String(100),
            nullable=False
        ),
        sa.Column(
            'author-id',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_profile.user-id'),
            nullable=False
        ),
        sa.Column(
            'article-id',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_article.uuid'),
            nullable=False
        )
    )


def downgrade():
    op.drop_table('conduit_api_comment')
