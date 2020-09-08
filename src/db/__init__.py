from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pathlib import Path

from .models import Base
from .models import User, Bill

current_dir = Path(__file__).resolve().parent

engine = create_engine(f'sqlite:///{current_dir}/rasa.sqlite', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)