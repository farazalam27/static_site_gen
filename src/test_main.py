import unittest
from textnode import TextNode
from leafnode import LeafNode
from main import text_node_to_html_node


class Test_Main(unittest.TestCase):
    def test_text_type_text(self):
        # Create the text node
        text_node = TextNode(text_type="text", text="normal text", url="")

        # Convert it using the function
        result_node = text_node_to_html_node(text_node)

        # Assert the type of the result
        self.assertIsInstance(result_node, LeafNode)

        # Assert the values of the result
        self.assertEqual(result_node.tag, None)
        self.assertEqual(result_node.value, "normal text")

    def test_text_type_bold(self):
        # Create the text node
        text_node = TextNode(text_type="bold", text="bold text", url="")

        # Convert it using the function
        result_node = text_node_to_html_node(text_node)

        # Assert the type of the result
        self.assertIsInstance(result_node, LeafNode)

        # Assert the values of the result
        self.assertEqual(result_node.tag, 'b')
        self.assertEqual(result_node.value, "bold text")

    def test_text_type_italic(self):
        # Create the text node
        text_node = TextNode(text_type="italic", text="italic text", url="")

        # Convert it using the function
        result_node = text_node_to_html_node(text_node)

        # Assert the type of the result
        self.assertIsInstance(result_node, LeafNode)

        # Assert the values of the result
        self.assertEqual(result_node.tag, 'i')
        self.assertEqual(result_node.value, "italic text")

    def test_text_type_code(self):
        # Create the text node
        text_node = TextNode(text_type="code", text="coding...", url="")

        # Convert it using the function
        result_node = text_node_to_html_node(text_node)

        # Assert the type of the result
        self.assertIsInstance(result_node, LeafNode)

        # Assert the values of the result
        self.assertEqual(result_node.tag, 'code')
        self.assertEqual(result_node.value, "coding...")

    def test_text_type_link(self):
        # Create the text node
        text_node = TextNode(text_type="link", text="click me", url="https://bootdev.com/")

        # Convert it using the function
        result_node = text_node_to_html_node(text_node)

        # Assert the type of the result
        self.assertIsInstance(result_node, LeafNode)

        # Assert the values of the result
        self.assertEqual(result_node.tag, 'a')
        self.assertEqual(result_node.value, "click me")
        self.assertEqual(result_node.props_to_html(), "href=https://bootdev.com/")

    def test_text_type_img(self):
        # Create the text node
        text_node = TextNode(text_type="image", text="click me", url="https://bootdev.com/")

        # Convert it using the function
        result_node = text_node_to_html_node(text_node)

        # Assert the type of the result
        self.assertIsInstance(result_node, LeafNode)

        # Assert the values of the result
        self.assertEqual(result_node.tag, 'img')
        self.assertEqual(result_node.value, "")
        self.assertEqual(result_node.props_to_html(), "src=https://bootdev.com/ alt=click me")

    def test_text_type_unknown(self):
        with self.assertRaises(ValueError):
            text_node = TextNode(text_type="unknown", text="normal text", url="fewaioji")
            result_node = text_node_to_html_node(text_node)

if __name__ == '__main__':
    unittest.main()
