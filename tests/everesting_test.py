import unittest

from everesting import calculate


class MyTestCase(unittest.TestCase):
    def test_calculate(self):
        n1 = {
            'data': {
                'name': "X1",
                'elevation': 10,
                'length': 50,
            },
        }
        n2 = {
            'data': {
                'name': "Z1",
                'elevation': 30,
                'length': 100,
            },
            'next': n1,
        }
        n1['next'] = n2

        res = calculate(n1)
        self.assertEqual(res['A'], 20)
        self.assertEqual(res['B'], 885)
        self.assertEqual(res['Cl'], 150)
        self.assertEqual(res['Ck'], 50)
        self.assertEqual(res['Dn'], "X1")
        self.assertEqual(res['Dk'], 24)

    def test_case1(self):
        n5 = {
            'data': {
                'name': "y2",
                'elevation': 55,
                'length': 234,
            },
        }
        n4 = {
            'data': {
                'name': "y1",
                'elevation': 10,
                'length': 175,
            },
            'next': n5
        }
        n3 = {
            'data': {
                'name': "x3",
                'elevation': 60,
                'length': 200,
            },
            'next': n4
        }
        n2 = {
            'data': {
                'name': "x2",
                'elevation': 30,
                'length': 122,
            },
            'next': n3,
        }
        n1 = {
            'data': {
                'name': "x1",
                'elevation': 20,
                'length': 150,
            },
            'next': n2,
        }
        n5['next'] = n1

        res = calculate(n1)
        self.assertEqual(res['A'], 85)
        self.assertEqual(res['B'], 209)
        self.assertEqual(res['Cl'], 881)
        self.assertEqual(res['Ck'], 447)
        self.assertEqual(res['Dn'], "y1")
        self.assertEqual(res['Dk'], 15)


if __name__ == '__main__':
    unittest.main()
