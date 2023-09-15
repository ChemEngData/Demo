import unittest

def add(a,b):
    return a+b


print(add(1,2))

class TestMyAddFunc(unittest.TestCase):
    def test_add(self):
        answer = add(10, 20)
        self.assertEqual(answer, 30)


if __name__ == '__main__':
    unittest.main()