import uuid
from sqlalchemy import Column, String
from sqlalchemy_utils import EmailType, PasswordType, URLType, UUIDType

from models.database import Base, Session


class UserManager(object):
    def __init__(self):
        self.session = Session()

    def create_user(self, username, email, password, **kwargs):
        if not username:
            raise ValueError('Field {username} cannot be null')
        if not email:
            raise ValueError('Field {email} cannot be null')
        if not password:
            raise ValueError('Field {password} cannot be null')

        new_user = User(
            username=username,
            email=email,
            password=password,
            bio=kwargs['bio'] if 'bio' in kwargs else None,
            image=kwargs['image'] if 'image' in kwargs else None
        )

        self.session.add(new_user)
        self.session.commit()
        return new_user.serialize()

    def find_one_user(self, email, password):
        if not email or not password:
            raise ValueError('Both email and password must be provided')

        user = self.session.query(User).filter(
            User.email == email
        ).one()
        assert user.password == password
        return user.serialize()


class User(Base):
    __tablename__ = 'conduit_api_user'

    uuid = Column(
        'uuid',
        UUIDType(
            binary=False
        ),
        primary_key=True,
        nullable=False,
        unique=True,
        default=uuid.uuid4()
    )
    email = Column(
        'email',
        EmailType,
        nullable=False,
        unique=True,
    )
    username = Column(
        'username',
        String(20),
        nullable=False
    )
    password = Column(
        'password',
        PasswordType(
            schemes=[
                'pbkdf2_sha512',
            ],
        ),
        nullable=False
    )
    bio = Column(
        'bio',
        String(100),
        nullable=True
    )
    image = Column(
        'image',
        URLType,
        nullable=True
    )

    __manager__ = UserManager()

    def __repr__(self):
        return '<User email: {}, username: {} >'.format(self.email, self.username)

    def __str__(self):
        return 'Conduit API User Model'

    def serialize(self):
        return {
            'email': self.email,
            'username': self.username,
            'bio': self.bio,
            'image': self.image
        }
