import unittest
from markdown import markdown


class AutoDirectionTestCase(unittest.TestCase):
    def test_ok(self):
        text = "Text"
        html = markdown(text, extensions=['autodirection'])
        self.assertEqual(
            html,
            '<p dir="auto">Text</p>'
        )


if __name__ == '__main__':
    unittest.main()
