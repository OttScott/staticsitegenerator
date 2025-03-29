import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

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