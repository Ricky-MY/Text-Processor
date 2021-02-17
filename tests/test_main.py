import unittest
import sys

sys.path.append('c:/Users/User/Documents/Programming/Python/Projects/Text-Processor/')
from textprocessor import TextProcessor

class TestMain(unittest.TestCase):
    path = 'tests/dummy.txt'
    def test_render_lines(self):
        with TextProcessor(self.path) as ctx:
            result = [*ctx.render_lines()]
        
        self.assertEqual(result, ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', '', 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', '', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', '', 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '', 'https://Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.com', '', 'https://Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.mp4', '', 'https://Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.jpg', '', 'https://Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.outcastextension'])

    def test__affirm(self):
        with TextProcessor(self.path) as ctx:
            ctx.render_lines()
            result = ctx._affirm()

        self.assertEqual(result, True)

    def test__empty_db(self):
        with TextProcessor(self.path) as ctx:
            ctx.render_lines()
            ctx.get_links('https://')
            ctx._empty_db()
            result = ctx.links

        self.assertEquals(result, [])

    def test_get_links(self):
        with TextProcessor(self.path) as ctx:
            ctx.render_lines()
            result = ctx.get_links('https://')

        self.assertEqual(result, ["https://Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.com"])

    def test_get_images(self):
        with TextProcessor(self.path) as ctx:
            ctx.render_lines()
            result = ctx.get_images('https://')

        self.assertEqual(result, ["https://Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.jpg"])

    def test_get_videos(self):
        with TextProcessor(self.path) as ctx:
            ctx.render_lines()
            result = ctx.get_videos('https://')

        self.assertEqual(result, ["https://Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.mp4"])

    def test_get_outcasts(self):
        with TextProcessor(self.path) as ctx:
            ctx.render_lines()
            result = ctx.get_outcasts('https://')

        self.assertEqual(result, ["https://Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.outcastextension"])

    def test_find_word(self):
        with TextProcessor(self.path) as ctx:
            ctx.render_lines()
            result = ctx.find_word('dolore')

        self.assertEqual(result, [[87, 255], 2])

if __name__ == '__main__':
    unittest.main()