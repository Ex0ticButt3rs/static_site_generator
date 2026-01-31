import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "omg, a url", {"href": "www.google.com"})
        node2 = LeafNode("b", "omg, a url", {"href": "www.google.com"})
        #self.assertEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()