import os
import unittest
import json
import sys
from api import Image
import config
from image_comparison_app import ImageAPI

class ImageComparisonTestCase(unittest.TestCase):
    def setUp(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': config.Bearer               
        }
        self.api = ImageAPI()
        self.app = self.api.create_app()
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        pass
 
    def test_identical_image_local(self):
        res = self.client().get('/image-comparison?imageA=image/black.jpg&imageB=image/black.jpg', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['percentage'], "100.00%")

    def test_identical_image_url(self):
        res = self.client().get('/image-comparison?imageA=https://consequenceofsound.net/wp-content/uploads/2019/05/pikachu-e1557247424342.jpg?quality=80&imageB=https://consequenceofsound.net/wp-content/uploads/2019/05/pikachu-e1557247424342.jpg?quality=80', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['percentage'], "100.00%")

    def test_different_image_local(self):
        res = self.client().get('/image-comparison?imageA=image/original_golden_bridge.jpg&imageB=image/old_photo.jpg', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['percentage'])

    def test_different_image_url(self):
        res = self.client().get('/image-comparison?imageA=https://consequenceofsound.net/wp-content/uploads/2019/05/pikachu-e1557247424342.jpg?quality=80&imageB=https://d.newsweek.com/en/full/822411/pikachu-640x360-pokemon-anime.jpg?w=1600&h=1200&q=88&f=3ed1c0d6e3890cbc58be90f05908a8f5', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['percentage'])

    def test_compare_local_url(self):
        res = self.client().get('/image-comparison?imageA=image/original_golden_bridge.jpg&imageB=https://consequenceofsound.net/wp-content/uploads/2019/05/pikachu-e1557247424342.jpg?quality=80', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['percentage'])

    def test_not_found(self):
        res = self.client().get('/image-comparison?imageA=null&imageB=null', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_invalid_auth(self):
        res = self.client().get('/image-comparison?imageA=image/black.jpg&imageB=image/black.jpg')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['code'], 'authorization_header_missing')
        self.assertEqual(data['message']['description'], 'Authorization header is expected.')

    def test_broken_url(self):
        res = self.client().get('/image-comparison?imageA=https://consequenceofsound.net/wp-content/uploads/2019/05/pikachu-e1557247424342.jp&imageB=https://consequenceofsound.net/wp-content/uploads/2019/05/pikachu-e1557247424342.jp', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()