import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlalchemy.orm import relationship
from models.database import Base, Session
from models.associations import \
    profiles_articles_relationship_table, profiles_relationship_table


class ProfileManager(object):
    """
    Manager class for model Profile
    """
    def __init__(self):
        self.session = Session()

    pass


class Profile(Base, sau.Timestamp):
    """
    Profile model class
    """
    __tablename__ = 'conduit_api_profile'

    # base fields
    user_id = sa.Column(
        'user-id',
        sau.UUIDType(binary=False),
        sa.ForeignKey('conduit_api_user.uuid'),
        nullable=False,
        primary_key=True,
        unique=True
    )

    # relationship fields
    user = relationship('User', back_populates='conduit_api_user')
    followers = relationship(
        'Profile',
        secondary=profiles_relationship_table,
        back_populates='conduit_api_profiles'
    )
    favorite_articles = relationship(
        'Article',
        secondary=profiles_articles_relationship_table,
        back_populates='conduit_api_articles'
    )
    written_articles = relationship('Article', back_populates='conduit_api_articles')

    __manager__ = ProfileManager()

    def __repr__(self):
        pass

    def __str__(self):
        return 'Conduit API Profile Model'

    def serialize(self):
        """
        returns JSON-serialized format of Model
        """
        pass
