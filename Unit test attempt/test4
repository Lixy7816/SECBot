#execute 中部分函数测试

#coding=utf-8　
import json
import unittest
from execute import max_length
import random
import torch
x = torch.Tensor(2,3)


class max_length_test(unittest.TestCase):
    def test_max_length(self):

        test_str = max_length(x)
        # 如果接受到的内容为空，则给出相应的回复
        self.assertEqual(test_str, 3)
unittest.main()
