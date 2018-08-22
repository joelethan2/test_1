import unittest
from flask import json
from app import create_app

class APITestCase(unittest.TestCase):

    def setUp(self):
        """Initialise the app and test variables"""
        self.app = create_app(config_name="testing")
        self.client=self.app.test_client

        self.test_qn={
                    'qn_id':12,
                    'qn':'what',
                    'aurthor':'j',
                    'answer':[{},{}]
                    }
        self.test_ans={
                    'ans_id': 8,
                    'answer': 'Yes!',
                    'aurthor': '   jo',
                    'votedown':5,'voteup': 7
                    }


    def test_questeion_has_id(self):
        post_resp = self.client().post('/questionz', 
                    data=json.dumps(self.test_qn),content_type='application/json')
        data=json.loads(post_resp.get_data(as_text=True))
        self.assertEqual(post_resp.status_code, 200)
        self.assertEqual(data['qn_id'], 12)


    def test_question_has_content(self):
        post_resp = self.client().post('/questionz', 
                    data=json.dumps(self.test_qn),content_type='application/json')
        data=json.loads(post_resp.get_data(as_text=True))
        self.assertEqual(post_resp.status_code, 200)
        self.assertNotEqual(data['qn'].strip(), '')
    
    def test_question_has_aurthor(self):
        post_resp = self.client().post('/questionz', 
                    data=json.dumps(self.test_qn),content_type='application/json')
        data=json.loads(post_resp.get_data(as_text=True))
        self.assertEqual(post_resp.status_code, 200)
        self.assertNotEqual(data['aurthor'].strip(), '')
    

    def test_answer_has_id(self):
        post_resp = self.client().post('/questionz/122/answers', data=json.dumps(self.test_ans),content_type='application/json')
        data=json.loads(post_resp.get_data(as_text=True))
        assert post_resp.status_code == 200
        assert data['ans_id']==8


    def test_answer_has_content(self):
        post_resp = self.client().post('/questionz/122/answers', data=json.dumps(self.test_ans),content_type='application/json')
        data=json.loads(post_resp.get_data(as_text=True))
        self.assertEqual(post_resp.status_code, 200)
        self.assertNotEqual(data['answer'].strip(), '')


    def test_answer_has_aurthor(self):
        post_resp = self.client().post('/questionz/122/answers', data=json.dumps(self.test_ans),content_type='application/json')
        data=json.loads(post_resp.get_data(as_text=True))
        self.assertEqual(post_resp.status_code, 200)
        self.assertNotEqual(data['aurthor'].strip(), '')

    def test_get_a_question(self):
        post_resp = self.client().post('/questionz/122/answers', data=json.dumps(self.test_ans),content_type='application/json')
        data=json.loads(post_resp.get_data(as_text=True))
        self.assertEqual(post_resp.status_code, 200)
        get_resp = self.client().get('questionz/12')
        self.assertEqual(get_resp.status_code, 200)


        


if __name__=="__main__":
    unittest.main()