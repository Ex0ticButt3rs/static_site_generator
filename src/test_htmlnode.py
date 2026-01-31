import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

        node3 = HTMLNode("a")
        node4 = HTMLNode("a")
        self.assertEqual(node3, node4)

        node5 = HTMLNode("a", {"href": "https://www.google.com"}).props_to_html()
        node6 = HTMLNode("p", {"p": "This is a test paragraph"}).props_to_html()
        self.assertNotEqual(node5.props_to_html(), node6.props_to_html())

if __name__ == "__main__":
    unittest.main()