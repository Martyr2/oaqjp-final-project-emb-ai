import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_glad(self):
        self.assertEqual(emotion_detector('I am glad this happened')['dominate_emotion'], 'joy')

    def test_mad(self):
        self.assertEqual(emotion_detector('I am really mad about this')['dominate_emotion'], 'anger')

    def test_disgusted(self):
        self.assertEqual(emotion_detector('I feel disgusted just hearing about this')['dominate_emotion'], 'disgust')

    def test_sad(self):
        self.assertEqual(emotion_detector('I am so sad about this')['dominate_emotion'], 'sadness')

    def test_afraid(self):
        self.assertEqual(emotion_detector('I am really afraid that this will happen')['dominate_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()