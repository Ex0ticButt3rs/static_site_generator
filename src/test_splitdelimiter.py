import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from splitdelimiter import split_nodes_delimiter


class TestSplitDelimiter(unittest.TestCase):
    def test_no_delimiter_text_unchanged(self):
        node = TextNode("plain text only", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "plain text only")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_simple_bold_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_multiple_bold_segments(self):
        node = TextNode("a **b** c **d** e", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        texts = [n.text for n in result]
        types = [n.text_type for n in result]
        self.assertEqual(texts, ["a ", "b", " c ", "d", " e"])
        self.assertEqual(
            types,
            [
                TextType.TEXT,
                TextType.BOLD,
                TextType.TEXT,
                TextType.BOLD,
                TextType.TEXT,
            ],
        )

    def test_code_delimiter(self):
        node = TextNode("some `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual([n.text for n in result], ["some ", "code", " here"])
        self.assertEqual(
            [n.text_type for n in result],
            [TextType.TEXT, TextType.CODE, TextType.TEXT],
        )

    def test_italic_delimiter(self):
        node = TextNode("this is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual([n.text for n in result], ["this is ", "italic", " text"])
        self.assertEqual(
            [n.text_type for n in result],
            [TextType.TEXT, TextType.ITALIC, TextType.TEXT],
        )

    def test_non_text_node_unchanged(self):
        node = TextNode("already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], node)

    def test_unmatched_delimiter_raises(self):
        node = TextNode("broken **bold text", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()