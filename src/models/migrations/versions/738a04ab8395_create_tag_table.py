"""Create tag table

Revision ID: 738a04ab8395
Revises: 98b2c43d2dbe
Create Date: 2018-05-12 04:51:35.079263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '738a04ab8395'
down_revision = '98b2c43d2dbe'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'conduit_api_tag',
        sa.Column(
            'id',
            sa.Integer,
            autoincrement=True,
            primary_key=True,
            unique=True,
            nullable=False
        ),
        sa.Column(
            'body',
            sa.String(20),
            nullable=False
        )
    )


def downgrade():
    op.drop_table('conduit_api_tag')
