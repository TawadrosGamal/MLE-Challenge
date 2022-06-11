from unittest import TestCase, main
import requests

class TestAudio(TestCase):
    API_URl="http://127.0.0.1:7000/"
    Audio_json={'Path':'E:/ML/FreeLance/intalio/mle-challenge/tests/static/test_audio.mp3','outPath':r'tests/results'}
    
    def test_1(self):
        response=requests.get(TestAudio.API_URl)
        statusCode=response.status_code
        self.assertEqual(statusCode, 200)
    
    def test_process_audio(self):

        response=requests.post(TestAudio.API_URl+"audio",json=TestAudio.Audio_json)
        print(response.status_code)

        self.assertDictEqual(response.json(),{'ChunkPaths': ['tests/results/0_chunck.mp3', 'tests/results/1_chunck.mp3', 'tests/results/2_chunck.mp3', 'tests/results/3_chunck.mp3', 'tests/results/4_chunck.mp3', 'tests/results/5_chunck.mp3', 'tests/results/6_chunck.mp3', 'tests/results/7_chunck.mp3', 'tests/results/8_chunck.mp3', 'tests/results/9_chunck.mp3', 'tests/results/10_chunck.mp3', 'tests/results/11_chunck.mp3', 'tests/results/12_chunck.mp3', 'tests/results/13_chunck.mp3', 'tests/results/14_chunck.mp3', 'tests/results/15_chunck.mp3', 'tests/results/16_chunck.mp3', 'tests/results/17_chunck.mp3'], 'numberOfChunks': 18})
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    main()
