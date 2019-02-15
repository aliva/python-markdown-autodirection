import unittest
from markdown import markdown

list_expected = '''<ul dir="auto">
<li>first item</li>
<li>second item</li>
</ul>'''


class AutoDirectionTestCase(unittest.TestCase):
    def test_ok(self):
        text = "Text"
        html = markdown(text, extensions=['autodirection'])
        self.assertEqual(
            html,
            '<p dir="auto">Text</p>'
        )

    def test_list(self):
        text = '- first item\n- second item'
        html = markdown(text, extensions=['autodirection'])
        self.assertEqual(html, list_expected)


    def test_header(self):
        text = "# header"
        html = markdown(text, extensions=['autodirection'])
        self.assertEqual(html, '<h1 dir="auto">header</h1>')
if __name__ == '__main__':
    unittest.main()
