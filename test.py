import unittest
from functions import *


class MyTestCase(unittest.TestCase):
    def test_person_taking_care_of_elders(self):
        self.assertEqual(all_people_being_taken_care(), [{'Name': 'Bhagwati', 'Taken Care By': 'anchal'},
                                                         {'Name': 'Pushpa', 'Taken Care By': 'anchal'},
                                                         {'Name': 'Mohan', 'Taken Care By': 'anchal'}], "Correct")

    def test_young_taking_care(self):
        names = ['anchal', 'mayank', 'pankaj', 'manish']
        outputs = [['Bhagwati', 'Pushpa', 'Mohan'], [], [], []]
        for name, output in zip(names, outputs):
            self.assertEqual(young_person_taking_care_of(name), output, "Correct")


if __name__ == '__main__':
    unittest.main()
