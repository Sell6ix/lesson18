# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Тут возвращаются модели.
# А вьюшка уже их переводит куда надо. В json или иной объект

# Пример
from app.service_container import MovieDAO
from app.dao.models.movie import Movie


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def create(self, data) -> Movie:
        return self.dao.create(data)

    def get_one(self, uid: int) -> Movie:
        return self.dao.get_one(uid)

    def get_all(self, director_id:int=None, genre_id:int=None, year:int=None) -> list[Movie]:
        return self.dao.get_all(director_id=director_id, genre_id=genre_id, year=year)

    def update(self, data):
        '''
        data - json
        '''
        uid = data.get('id')
        model = Movie(**data)
        self.dao.update(model)

    def particular_update(self, data):
        uid = data.get('id')
        model = self.get_one(uid)

        if 'name' in data:
            model.name = data.get('name')

        if 'description' in data:
            model.description = data.get('description')

        if 'trailer' in data:
            model.trailer = data.get('trailer')

        if 'year' in data:
            model.year = data.get('year')

        if 'raiting' in data:
            model.raiting = data.get('raiting')

        if 'genre_id' in data:
            model.genre_id = data.get('genre_id')

        if 'director_id' in data:
            model.director_id = data.get('director_id')

        self.dao.update(model)

    def delete(self, uid: int):
        uid = data.get('id')
        self.dao.delete(uid)