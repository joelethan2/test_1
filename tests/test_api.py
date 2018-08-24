import json
import unittest
from app.Routes import app
from app.Question import Question
#tests for the api end points

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING']=True
        self.client = self.app.test_client

        self.test_qn={
                    'qn':'what',
                    'user':'j',
                    }
        self.test_ans={
                    'qn_id': 8,
                    'answer': 'Yes!',
                    'user': '   jo',
                    }

    def test_add_a_question(self):
        resp=self.client().post('/v1/questions',data=(self.test_qn))
        self.assertEqual(resp.status_code, 201)
        self.assertIn('what', str(resp.data))
        self.assertIn('j', str(resp.data))

    
    def test_answer_a_queation(self):
        resp=self.client().post('/v1/questions/1/answers', data=self.test_ans)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Yes!',str(resp.data))
        self.assertIn('   jo',str(resp.data))
    
    
    def test_get_all_questions(self):
        post_resp=self.client().post('/v1/questions',data=(self.test_qn))
        self.assertEqual(post_resp.status_code, 201)
        get_resp=self.client().get('/v1/questions')
        self.assertEqual(get_resp.status_code, 200)
        self.assertIn('what', str(get_resp.data))


if __name__=="__main__":
    unittest.main()