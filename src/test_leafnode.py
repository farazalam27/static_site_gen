import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode('What are you doing?', 'a', {"href": "https://www.google.com"})
        node2 = LeafNode('What are you doing?', 'a', {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)  # add assertion here

    def test_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None, 'a', {"href": "https://www.google.com"})
            node.to_html()

    def test_to_html(self):
        node = LeafNode('Click Me!', 'a', {"href": "https://www.google.com"})
        html = node.to_html()
        self.assertEqual(html, "<a href=https://www.google.com>Click Me!</a>")


if __name__ == '__main__':
    unittest.main()
