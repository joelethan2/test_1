import unittest
import json
from app import create_app

class APITestCase(unittest.TestCase):

    def setUp(self):
        """Initialise the app and test variables"""
        self.app = create_app(config_name="testing")
        self.client=self.app.test_client


    def test_post_answer(self):
        post_resp = self.client().post('/questionz', data=json.dumps({
            'qn_id':12,'qn':'what','aurthor':'j','answer':[{},{}]
        }),content_type='application/json', )
        data=json.loads(post_resp.get_data(as_text=True))
        assert post_resp.status_code==200
        assert data['qn_id'] == 12
    
    def test_post_an_answer(self):
        post_resp = self.client().post('/questionz/122/answers', data=json.dumps({
            'ans_id': 8,'answer': 'Yes!','aurthor': 'jo','votedown':5,'voteup': 7
            }),content_type='application/json', )
        data=json.loads(post_resp.get_data(as_text=True))
        assert post_resp.status_code == 200
        assert data['ans_id']==8



    

if __name__=="__main__":
    unittest.main()