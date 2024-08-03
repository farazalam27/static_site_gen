import unittest
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node1 = HtmlNode('p', 'hello' )
        node2 = HtmlNode('p', 'hello')
        self.assertEqual(node1, node2)  # add assertion here

    def test_print(self):
        node1 = HtmlNode('h1', 'hello', ['hello', 'world'], {'href': 'benchod'})
        self.assertEqual(str(node1), "HtmlNode(h1, hello, ['hello', 'world'], {'href': 'benchod'})")

    def test_props_to_html(self):
        node1 = HtmlNode('h1', 'hello', ['hello', 'world'], {'href': 'benchod'})
        self.assertEqual(node1.props_to_html(), "href=benchod")

if __name__ == '__main__':
    unittest.main()
