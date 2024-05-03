from flask_restful import Resource
from resources import api

from services.book_service import BookService

class BookResource(Resource):
    def get(self, book_id: int):
        book_model = BookService().get_book_by_id(book_id)

        if book_model:
            return book_model.serialize()
        else:
            return {'error': f'Book with id {book_id} not found.'}, 404

    # def put(self, book_id: int):
    #     return == 1:
    #         return {'id': student_id, 'name': 'jack', 'gender': 'male'},200
    #     else:
    #         return {'id': f'Student not found for id:{student_id}'}, 404



api.add_resource(BookResource, '/books/<int:book_id>')
