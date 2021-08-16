import unittest
import main
import module1
import module2
import module3
import module4


class TestMain(unittest.TestCase):
    
    def test_function1(self):
        results = module1.function(main.subset)
        self.assertEqual(results, [[], []])
        
    def test_function2(self):
        results = module2.function(main.subset)
        self.assertEqual(results, [[], []])
        
    def test_function3(self):
        results = module3.function(main.subset)
        self.assertEqual(results, [[], []])
        
    def test_function4(self):
        results = module4.function(main.subset)
        self.assertEqual(results, {})


if __name__ == '__main__':
    unittest.main()