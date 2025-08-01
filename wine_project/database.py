from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from wine_project.settings import Settings

engine = create_engine(Settings().DATABASE_URL)

#doesn't make sense to test the session so removing from test coverage
def get_session(): # pragma: no cover
    with Session(engine) as session:
        yield session
