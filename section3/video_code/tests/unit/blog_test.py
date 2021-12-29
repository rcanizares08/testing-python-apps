from unittest import TestCase
from section3.video_code.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test author', b.author)
        self.assertEqual(0, len(b.posts))
        self.assertListEqual([], b.posts)

    def test_json_no_posts(self):
        b = Blog('Test', 'Test author')

        self.assertDictEqual(b.json(), {
            'title': b.title,
            'author': b.author,
            'posts': [],
        })

    def test_repr(self):
        b = Blog('Test', 'Test author')
        b2 = Blog('Test2', 'Test author2')
        print(b.__repr__())

        self.assertEqual(b.__repr__(), 'Test by Test author (0 post)')
        self.assertEqual(b2.__repr__(), 'Test2 by Test author2 (0 post)')

    def test_repr_multiple_post(self):
        b = Blog('Test', 'Test author')
        b.posts = ['Hello']
        b2 = Blog('Test2', 'Test author2')
        b2.posts = ['Hello', 'another']
        self.assertEqual(b.__repr__(), 'Test by Test author (1 post)')
        self.assertEqual(b2.__repr__(), 'Test2 by Test author2 (2 posts)')
