"""
defines many-to-many relationship tables
"""
import sqlalchemy as sa
from models.database import Base

profiles_relationship_table = None
profiles_articles_relationship_table = None
articles_comments_relationship_table = None
articles_tags_relationship_table = None
