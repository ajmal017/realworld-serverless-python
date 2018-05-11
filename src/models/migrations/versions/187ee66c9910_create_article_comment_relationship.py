"""Create article-comment relationship

Revision ID: 187ee66c9910
Revises: ce5457ef45d6
Create Date: 2018-05-12 05:11:52.940730

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision = '187ee66c9910'
down_revision = 'ce5457ef45d6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'article-comment-association',
        sa.Column(
            'article-id',
            sau.UUIDType(binary=False),
            sa.ForeignKey('conduit_api_article.uuid'),
        ),
        sa.Column(
            'comment-id',
            sa.Integer,
            sa.ForeignKey('conduit_api_comment.id')
        )
    )


def downgrade():
    op.drop_table('article-comment-association')
