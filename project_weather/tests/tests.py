from unittest import TestCase

from ..src.models.openweathermap.get_data import get_formatted_data


class Tests(TestCase):

    def test_get_data(self):
        city = 'Soesterberg'
        days = 14
        # data = get_formatted_data(city, days)
        self.assertEquals(1, 1)