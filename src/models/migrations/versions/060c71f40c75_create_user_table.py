"""Create user table

Revision ID: 060c71f40c75
Revises: 
Create Date: 2018-04-27 05:10:59.366909

"""
import uuid

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy_utils import UUIDType, URLType, PasswordType, EmailType

revision = '060c71f40c75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'conduit_api_user',
        sa.Column(
            'uuid',
            UUIDType(binary=False),
            primary_key=True,
            nullable=False,
            unique=True,
            default=uuid.uuid4()
        ),
        sa.Column(
            'email',
            EmailType,
            nullable=False,
            unique=True,
        ),
        sa.Column(
            'username',
            sa.String(20),
            nullable=False
        ),
        sa.Column(
            'password',
            PasswordType(
                schemes=[
                    'pbkdf2_sha512',
                ],
            ),
            nullable=False
        ),
        sa. Column(
            'bio',
            sa.String(100),
            nullable=True
        ),
        sa.Column(
            'image',
            URLType,
            nullable=True
        ),
    )


def downgrade():
    op.drop_table('conduit_api_user')
