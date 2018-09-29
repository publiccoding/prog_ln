import unittest

from modules.addition import addValues
from mathsOperaton import mathsOperation


class unitTest(unittest.TestCase):
    def testCalculation(self):
        self.assertEqual(mathsOperation(1, [4,5]).calcOperation(), 9)


if __name__ == '__main__':
    unittest.main()