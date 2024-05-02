

class StudentResource(Resource):
    def get(self, student_id: int):
        if student_id == 1:
            return {'id': student_id, 'name': 'jack', 'gender': 'male'}
        else:
            return {'id': f'Student not found for id:{student_id}'}, 404

    def put(self, student_id: int):
        return {'id': student_id, 'name': 'jane', 'gender': 'female'}

    api.add_resource(StudentResource, '/student/<int:student_id>')
