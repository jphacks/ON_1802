import unittest
import read

class TestRead(unittest.TestCase):
    """test class of read.py
    """

    def test_read(self):
        """test method for json_to_data
        """
        user_id_1 = 'sample_data'
        expected1 = [{'user_id': 1, 'task_name': '洗濯物をたたむ', 'task_info': '洗濯物が溜まってきたのでそろそろ畳まないといけない', 'time_limit': {'year': 2018, 'month': 10, 'date': 18}}, {'user_id': 1, 'task_name': '洗濯物をたたむ', 'task_info': '洗濯物が溜まってきたのでそろそろ畳まないといけない', 'time_limit': {'year': 2018, 'month': 10, 'date': 18}}, {'user_id': 1, 'task_name': '洗濯物をたたむ', 'task_info': '洗濯物が溜まってきたのでそろそろ畳まないといけない', 'time_limit': {'year': 2018, 'month': 10, 'date': 18}}]
        user_id_2 = '2'
        expected2 = False
        
        self.assertEqual(expected1, read.json_to_data(user_id_1))
        self.assertEqual(expected2, read.json_to_data(user_id_2))

if __name__ == "__main__":
    unittest.main()
