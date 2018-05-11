"""Create article table

Revision ID: f5ef6affc65c
Revises: 586ff0a55152
Create Date: 2018-05-12 04:42:27.751231

"""
import uuid

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision = 'f5ef6affc65c'
down_revision = '586ff0a55152'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'conduit_api_article',
        sa.Column(
            'uuid',
            sau.UUIDType(binary=False),
            primary_key=True,
            nullable=False,
            unique=True,
            default=uuid.uuid4
        ),
        sa.Column(
            'title',
            sa.String(100),
            nullable=False
        ),
        sa.Column(
            'slug',
            sa.String(100),
            nullable=False
        ),
        sa.Column(
            'description',
            sa.String(300),
            nullable=False
        ),
        sa.Column(
            'body',
            sa.Text,
            nullable=False
        ),
        sa.Column(
            'author-id',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_profile.user-id'),
            nullable=False,
            primary_key=False,
            unique=True
        ),
    )


def downgrade():
    op.drop_table('conduit_api_article')
