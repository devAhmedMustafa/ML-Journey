import unittest
from StarAI.Workflow.Analysis import *


class Analysis(unittest.TestCase):
    def mqe(self):
        self.assertEqual(mean_square_error([1, 1, 1, 1], [1, 1, 1, 1]), 0)
        self.assertEqual(mean_square_error([2, 2], [1, 1]), 1/2)


if __name__ == '__main__':
    unittest.main()
