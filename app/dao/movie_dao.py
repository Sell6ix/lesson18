from app.dao.models.movie import Movie

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid) -> Movie:
        return self.session.query(Movie).get(uid)

    def get_all(self, director_id: int = None, genre_id : int = None, year: int = None) -> list[Movie]:
        data = self.session.query(Movie)

        if director_id is not None:
            data = data.filter(models.Movie.director_id == director_id)

        if genre_id is not None:
            data = data.filter(models.Movie.genre_id == genre_id)

        if year is not None:
            data = data.filter(models.Movie.year == year)

        return data.all()

    def create(self, data) -> Movie:
        model = Movie(**data)
        self.session.add(model)
        self.session.commit()
        return model

    def update(self, model: Movie) -> None:
        self.session.add(model)
        self.session.commit()

    def delete(self, uid: int) -> None:
        model = self.get_one(uid)
        self.session.delete(model)
        self.session.commit()
