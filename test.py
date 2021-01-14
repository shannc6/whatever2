import os
import unittest
import json
import sys
from api import Image


class ImageComparisonTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    # def setUp(self):
    #     """Define test variables and initialize app."""
    #     self.app = create_app()
    #     self.client = self.app.test_client
    #     self.database_name = "trivia_test"
    #     # self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
    #     self.database_path = 'postgresql:///trivia_test'
    #     setup_db(self.app, self.database_path)

    #     # binds the app to the current context
    #     with self.app.app_context():
    #         self.db = SQLAlchemy()
    #         self.db.init_app(self.app)
    #         # create all tables
    #         self.db.create_all()
    # def __init__(self):
    #     self.image = Image()

    def setUp(self):
        self.image = Image()
        self.app = self.image.create_app()
        self.client = self.app.test_client

    # def tearDown(self):
    #     """Executed after reach test"""
    #     pass
 
    def test_identical_image_local(self):
        # print("test cliet" + self.app.test_client)
        res = self.client().get('/image-comparison?imageA=image/black.jpg&imageB=image/black.jpg')
        data = json.loads(res.data)

        print(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['percentage'], "100%")

    # def test_identical_image_url(self):
    #     res = self.client().get('/questions?page=100000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['error'], 404)
    #     self.assertEqual(data['message'],'not found')

    # def test_different_image_local(self):
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['total_category'])

    # def test_different_image_url(self):
    #     res = self.client().get('/categories/100000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['error'], 404)
    #     self.assertEqual(data['message'],'not found')

    # def test_compare_local_url(self):
    #     res = self.client().get('/categories/100000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['error'], 404)
    #     self.assertEqual(data['message'],'not found')

    # def test_not_found(self):
    #     # self mock test
    #     question = Question(question='q', answer='a', category=1, difficulty=1)
    #     question.insert()
    #     question_id = question.id
    #     # print(question_id, file=sys.stderr)
    #     res = self.client().delete(f'/questions/{question_id}')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], question_id)

    # def test_invalid_auth(self):
        question_id = 10000000

        res = self.client().delete(f'/questions/{question_id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'unprocessable entity')









    # def test_create_question(self):
    #     new_q = {
    #         'question': 'q',
    #         'answer': 'a',
    #         'category': 1,
    #         'difficulty': 1
    #     }
    #     res = self.client().post('/questions', json=new_q)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['created'])
    #     self.assertTrue(data['total_questions'])

    # def test_create_empty_question(self):
    #     new_q = {
    #         'question': '',
    #         'answer': '',
    #         'category': 1,
    #         'difficulty': 1
    #     }
    #     res = self.client().post('/questions', json=new_q)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['error'], 422)
    #     self.assertEqual(data['message'], 'unprocessable entity')

    # def test_search_question(self):
    #     new_search = {
    #         'searchTerm': 'title'
    #     }
    #     res = self.client().post('/questions/search', json=new_search)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['total_questions'])

    # def test_empty_search_term(self):
    #     new_search = {
    #         'searchTerm': ''
    #     }
    #     res = self.client().post('/questions/search', json=new_search)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['error'], 422)
    #     self.assertEqual(data['message'], 'unprocessable entity')

    # def test_get_question_by_category(self):
    #     res = self.client().get('categories/1/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['category'],1)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['total_questions'])

    # def test_get_question_by_category_not_found(self):
    #     res = self.client().get('/categories/100000/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['error'], 404)
    #     self.assertEqual(data['message'],'not found')

    # def test_play_quiz(self):
    #     new_quiz = {
    #         'previous_questions': [],
    #         'quiz_category': {
    #             'type': 'Sports',
    #             'id': 6
    #         }
    #     }
    #     res = self.client().post('/quizzes', json=new_quiz)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_empty_play_quiz(self):
    #     res = self.client().post('/quizzes', json={})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['error'], 404)
    #     self.assertEqual(data['message'], 'not found')
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()