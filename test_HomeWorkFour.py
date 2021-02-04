import unittest
import HomeWorkFour

class TestHomeWorkFour(unittest.TestCase):
    def test_Average(self):
        list0 = [1,2,3,4,5,6,7,8,9]
        list1 = []
        list2 = [-2,-1,0,1,2]
        self.assertEqual(HomeWorkFour.average(list0), 5)
        self.assertEqual(HomeWorkFour.average(list1), 0)
        self.assertEqual(HomeWorkFour.average(list2), 0)

    def test_Volume(self):
        self.assertEqual(HomeWorkFour.volume(5), 125)
        self.assertEqual(HomeWorkFour.volume(-100), 0)
        self.assertEqual(HomeWorkFour.volume(4.5), 91.125)

    def test_Name(self):
        self.assertEqual(HomeWorkFour.fullname('Phillip', 'Renaud'), 'Phillip Renaud')
        self.assertEqual(HomeWorkFour.fullname('Santa', 'Claus'), 'Santa Claus')
        self.assertEqual(HomeWorkFour.fullname('Bella', 'Delphine'), 'Bella Delphine')

if __name__ == '__main__':
    unittest.main()