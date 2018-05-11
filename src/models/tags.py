import sqlalchemy as sa
from sqlalchemy.orm import relationship
from models.associations import articles_tags_relationship_table
from models.database import Base, Session


class TagManager(object):
    """
    Manager class for model Tag
    """
    def __init__(self):
        self.session = Session()

    pass


class Tag(Base):
    """
    Tag model class
    """
    __tablename__ = 'conduit_api_tag'

    # base fields
    id = sa.Column(
        'id',
        sa.Integer,
        autoincrement=True,
        primary_key=True,
        unique=True,
        nullable=False
    )
    body = sa.Column(
        'body',
        sa.String(20),
        nullable=False
    )

    # relationship fields
    articles = relationship(
        'Article',
        secondary=articles_tags_relationship_table,
        back_populates='conduit_api_articles'
    )

    __manager__ = TagManager()

    def __repr__(self):
        pass

    def __str__(self):
        return 'Conduit API Tag model'

    def serialize(self):
        pass
