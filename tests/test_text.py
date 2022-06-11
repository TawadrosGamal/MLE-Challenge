from unittest import TestCase, main

import requests
class TestText(TestCase):
    API_URl="http://127.0.0.1:7000/"
    text_json={'text':None,'language':'EN'}
    Ar_text_json={'Path':'E:/ML/FreeLance/intalio/mle-challenge/tests/static/test_text.txt','language':'AR'}
       
    def test_1(self):
        response=requests.get(TestText.API_URl)
        statusCode=response.status_code
        self.assertEqual(statusCode, 200)
    
    def test_process_text_eng(self):
        with open('tests/static/test_text.txt','r',encoding='utf-8') as file:
            text=file.read()
        TestText.text_json['text']=text
        response=requests.post(TestText.API_URl+"text",json=TestText.text_json)
        print(response.status_code)
        self.assertDictEqual(response.json(),{'predictions': [['Barack', 'PERSON'], ['Obama', 'PERSON'], ['United', 'LOCATION'], ['States', 'LOCATION'], ['2008', 'DATE'], ['2012', 'DATE'], ['Kenya', 'LOCATION'], ['Kansas', 'LOCATION'], ['Obama', 'PERSON'], ['Hawaii', 'LOCATION'], ['Columbia', 'ORGANIZATION'], ['University', 'ORGANIZATION'], ['Harvard', 'ORGANIZATION'], ['Law', 'ORGANIZATION'], ['School', 'ORGANIZATION'], ['Harvard', 'ORGANIZATION'], ['Law', 'ORGANIZATION'], ['Review', 'ORGANIZATION'], ['Illinois', 'ORGANIZATION'], ['State', 'ORGANIZATION'], ['Senate', 'ORGANIZATION'], ['U.S.', 'LOCATION'], ['Illinois', 'LOCATION'], ['2004', 'DATE'], ['Michelle', 'PERSON'], ['Obama', 'PERSON'], ['Malia', 'PERSON'], ['Sasha', 'PERSON']], 'wordsNumber': 28})

    def test_process_text_non(self):
        with open('tests/static/test_text.txt','r',encoding='utf-8') as file:
            text=file.read()
        TestText.text_json['text']=text
        TestText.text_json['language']='Fr'
        
        response=requests.post(TestText.API_URl+"text",json=TestText.text_json)
        print(response.status_code)
        self.assertDictEqual(response.json(),{'WrongLang': "Please Choose Between AR or EN"})


if __name__ == "__main__":
    main()
