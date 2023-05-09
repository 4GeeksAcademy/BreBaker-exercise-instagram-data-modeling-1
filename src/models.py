import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, DateTime, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    date_of_birth = Column(DateTime)
    profile_picture = Column(String)
    bio = Column(String)
    followers = Column(Integer)
    following = Column(Integer)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    caption = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")
    hashtags = relationship("Hashtag", secondary="post_hashtag")
    comments = relationship("Comment", back_populates="post")
    likes = relationship("Like", back_populates="post")

class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Post", back_populates="comments")

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Post", back_populates="likes")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

# image = Image.open('diagram.png')
# image.show()