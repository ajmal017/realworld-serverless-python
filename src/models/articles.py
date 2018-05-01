import uuid
import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlalchemy.orm import relationship
from models.associations import profiles_articles_relationship_table
from models.database import Base, Session


class ArticleManager(object):
    """
    Manager class for model Article
    """

    def __init__(self):
        self.session = Session()

    pass


class Article(Base, sau.Timestamp):
    """
    Article model class
    """
    __tablename__ = 'conduit_api_article'

    # base fields
    uuid = sa.Column(
        'uuid',
        sau.UUIDType(binary=False),
        primary_key=True,
        nullable=False,
        unique=True,
        default=uuid.uuid4
    )
    title = sa.Column(
        'title',
        sa.String(100),
        nullable=False
    )
    slug = sa.Column(
        'slug',
        sa.String(100),
        nullable=False
    )
    description = sa.Column(
        'description',
        sa.String(300),
        nullable=False
    )
    body = sa.Column(
        'body',
        sa.Text,
        nullable=False
    )

    author_id = sa.Column(
        'author-id',
        sau.UUIDType,
        sa.ForeignKey('conduit_api_profile.user_id'),
        nullable=False,
        primary_key=False,
        unique=True
    )

    # relationship fields
    author = relationship('Profile', back_populates='conduit_api_profile')
    favorited_user = relationship(
        'Profile',
        secondary=profiles_articles_relationship_table,
        back_populates='conduit_api_articles'
    )

    __manager__ = ArticleManager()

    def __repr__(self):
        pass

    def __str__(self):
        return 'Conduit API Article Model'

    def serialize(self):
        pass
