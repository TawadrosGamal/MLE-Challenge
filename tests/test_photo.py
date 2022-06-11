from unittest import TestCase, main

import requests

class TestPhoto(TestCase):
    API_URl="http://127.0.0.1:7000/"
    photo_json={'Path':'E:/ML/FreeLance/intalio/mle-challenge/tests/static/test_image.png','outPath':r'tests/results','IsPDF':False}
    pdf_json={'Path':'E:/ML/FreeLance/intalio/mle-challenge/tests/static/test_pdf.pdf','outPath':r'tests/results','IsPDF':True}
    
    def test_1(self):
        response=requests.get(TestPhoto.API_URl)
        statusCode=response.status_code
        self.assertEqual(statusCode, 200)
        
    def test_process_photo(self):

        response=requests.post(TestPhoto.API_URl+"photo",json=TestPhoto.photo_json)
        print(response.status_code)
        print(response.json())
        self.assertDictEqual(response.json(),{'Face': [1], 'Path': ['tests/results/imageWithFaces.jpeg'], 'Position': [[[180, 68, 237, 237]]]})
        self.assertEqual(response.status_code, 200)
    def test_process_pdf(self):

        response=requests.post(TestPhoto.API_URl+"photo",json=TestPhoto.pdf_json)
        print(response.status_code)
    
        self.assertDictEqual(response.json(),{'Face': [1,1], 'Path': ['tests/results/0imageWithFaces.jpeg','tests/results/1imageWithFaces.jpeg'], 'Position': [[[129, 86, 253, 253]], [[181, 68, 236, 236]]]})
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    main()
