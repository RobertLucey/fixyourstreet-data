from unittest import TestCase

from fixyourstreet_data.models.category import Category


class CategoryTest(TestCase):

    def test_serialize(self):
        self.assertEqual(
            Category(
                **{'id': 3, 'title': 'Street Lighting'}
            ).serialize(),
            {'category': {'id': 3, 'title': 'Street Lighting', 'label': 'street_lighting'}}
        )
