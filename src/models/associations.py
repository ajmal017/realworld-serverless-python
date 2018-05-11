"""
defines many-to-many relationship tables
"""
import sqlalchemy as sa
import sqlalchemy_utils as sau
from models.database import Base

profiles_relationship_table = sa.Table(
    'profile-profile-association',
    Base.metadata,
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

profiles_articles_relationship_table = sa.Table(
    'profile-article-association',
    Base.metadata,
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

articles_comments_relationship_table = sa.Table(
    'article-comment-association',
    Base.metadata,
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

articles_tags_relationship_table = sa.Table(
    'article-tag-association',
    Base.metadata,
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
