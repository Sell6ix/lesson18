from .database import db
from .dao.models.genre import Genre
from .dao.models.director import Director
from .dao.models.movie import Movie

def prepeare_data():
    genres = [
        Genre(id=1, name="drama"),
        Genre(id=2, name="comedy")
    ]

    directors = [
        Director(id=1, name="Name 1"),
        Director(id=2, name="Name 2"),
        Director(id=3, name="Name 3")
    ]

    movies = [
        Movie(
            id=1,
            name="Movie name 1",
            description="Movie description 1",
            trailer="Movie trailer 1",
            year=2000,
            raiting="R",
            genre_id=1,
            director_id=1
        ),
         Movie(
            id=2,
            name="Movie name 2",
            description="Movie description 2",
            trailer="Movie trailer 2",
            year=2001,
            raiting="R",
            genre_id=2,
            director_id=1
        ),
         Movie(
            id=3,
            name="Movie name 3",
            description="Movie description 3",
            trailer="Movie trailer 3",
            year=2000,
            raiting="R",
            genre_id=1,
            director_id=2
        ),
         Movie(
            id=4,
            name="Movie name 4",
            description="Movie description 4",
            trailer="Movie trailer 4",
            year=2000,
            raiting="R",
            genre_id=2,
            director_id=2
        ),
         Movie(
            id=5,
            name="Movie name 5",
            description="Movie description 5",
            trailer="Movie trailer 5",
            year=2002,
            raiting="R",
            genre_id=1,
            director_id=3
        ),
         Movie(
            id=6,
            name="Movie name 6",
            description="Movie description 6",
            trailer="Movie trailer 6",
            year=2002,
            raiting="R",
            genre_id=2,
            director_id=3
         )
    ]

    db.session.add_all(directors)
    db.session.add_all(genres)
    db.session.add_all(movies)
    db.session.commit()