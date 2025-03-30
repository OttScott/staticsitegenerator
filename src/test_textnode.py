import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_Text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.text, "This is a text node")

    def test_Bold(self):
        node = TextNode("This is a Bold node", TextType.BOLD)
        self.assertEqual(node.text, "This is a Bold node")
        self.assertEqual(node.text_type, TextType.BOLD)
    def test_Italic(self):
        node = TextNode("This is an Italic node", TextType.ITALIC)
        self.assertEqual(node.text, "This is an Italic node")
        self.assertEqual(node.text_type, TextType.ITALIC)
    def test_Code(self):
        node = TextNode("This is a Code node", TextType.CODE)
        self.assertEqual(node.text, "This is a Code node")
        self.assertEqual(node.text_type, TextType.CODE)
    def test_Link(self):
        node = TextNode("This is a Link node", TextType.LINK)
        self.assertEqual(node.text, "This is a Link node")
        self.assertEqual(node.text_type, TextType.LINK)
    def test_Image(self):
        node = TextNode("This is an Image node", TextType.IMAGE)
        self.assertEqual(node.text, "This is an Image node")
        self.assertEqual(node.text_type, TextType.IMAGE)

    def test_URL(self):
        node = TextNode("This is a URL node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node.url, "https://www.boot.dev")
    def test_URL_neq(self):
        node = TextNode("This is a URL node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a URL node", TextType.LINK, "https://www.boot.dev2")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a Bold node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a Bold node, BOLD, None)")
    def test_repr_with_url(self):
        node = TextNode("This is a URL node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(repr(node), "TextNode(This is a URL node, LINK, https://www.boot.dev)")

if __name__ == "__main__":
    unittest.main()