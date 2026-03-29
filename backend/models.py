from database import Base , engine 
from sqlalchemy import  Column , Integer , String , ForeignKey , relationship

#Db Models
class User(Base):
  __tablename__ = "users"

  id = Column(Integer , primary_key=True , index=True)
  name = Column(String(100) , nullable=False) 
  email = Column(String(200) , nullable=False , unique=True)
  password = Column(String(200) , nullable=False) 
  favorites = relationship("Favorites", back_populates="user") 


class Favorites(Base):
  __tablename__ = "favorites"
  id = Column(Integer, primary_key=True , index=True)

  id_anime = Column(Integer , ForeignKey("Anime_Movie.id"))
  id_user = Column(Integer, ForeignKey("users.id"))
  name = Column(String(100) , nullable=False)
  type = Column(String(100) , nullable=False)
  users = relationship("Favorites", back_populates="users") 

class AnimeMovie(Base):
  __tablename__ = "Anime_Movie"
  id = Column(Integer , primary_key=True)
  title = Column(String(300) , nullable=False)
  type = Column(String(100))
  genre = Column(String(100))
  rating = Column(String(200))


class userPrefrence(Base) :
  __tablename__ = "userPrefrence"
  id = Column(Integer , primary_key=True)
  id_user = Column(Integer , ForeignKey("users.id") )
  preferedGenre = Column(String(200))
  preferedType = Column (String(200))
  users = relationship("Favorites", back_populates="useres")

Base.metadata.create_all(engine)