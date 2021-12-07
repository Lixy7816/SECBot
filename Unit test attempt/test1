#the first test


#coding=utf-8　
#test文件在execute所在文件夹下

import unittest
from execute import preprocess_sentence

class preprocess_sentenceTest(unittest.TestCase):

 def test_preprocess_sentence1(self):

    preprocess_sentence_str = preprocess_sentence('Joker')
    self.assertEqual(preprocess_sentence_str,'start Joker end')
    
 def test_preprocess_sentence2(self):

    preprocess_sentence_str = preprocess_sentence('liming')
    self.assertEqual(preprocess_sentence_str,'start liming end')

unittest.main()
