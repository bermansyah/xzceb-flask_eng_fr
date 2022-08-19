import unittest

from translator import englishToFrench, frenchToEnglish

class MyUnitTest(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertNotEqual(englishToFrench(''), 'Bonjour')        
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        self.assertNotEqual(frenchToEnglish(''), 'Hello')        
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()