from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///:memory:", echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Identity Map in action
user1 = User(name="Alice")
session.add(user1)
session.flush() # Flushes SQL, but stays in transaction

user_fetched = session.query(User).filter_by(name="Alice").first()
print("Same object in memory?", user1 is user_fetched) # Output: True