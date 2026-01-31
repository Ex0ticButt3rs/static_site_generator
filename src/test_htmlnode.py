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

if __name__ == "__main__":
    unittest.main()