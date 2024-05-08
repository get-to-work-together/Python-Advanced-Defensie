import unittest


from ..src.models.activity import Activity


class TestActivity(unittest.TestCase):

    def test_instantiation(self):
        activity = Activity('Onderhoud', 'onderhoud', date_due = '2024-05-21')
        self.assertIsInstance(activity, Activity)

    def test_default_status(self):
        activity = Activity('Onderhoud', 'onderhoud', date_due = '2024-05-21')
        expected = 'open'
        actual = activity._status
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()
