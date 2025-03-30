import unittest

from htmlnode import HTMLNode,ParentNode,LeafNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHtmlNode(unittest.TestCase):
    def test_constructor(self):
        node = HTMLNode("div", "Hello World", ["child1", "child2"], {"class": "test"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, ["child1", "child2"])
        self.assertEqual(node.props, {"class": "test"})
    def test_constructor_empty(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html(self):
        node = HTMLNode("div", None, None, {"class": "test", "id": "test-id"})
        self.assertEqual(node.props_to_html(), ' class="test" id="test-id"')
    def test_props_to_html_empty(self):
        node = HTMLNode("div")
        self.assertEqual(node.props_to_html(), "")

class TestHtmlLeafNode(unittest.TestCase):
    def test_constructor(self):
        node = LeafNode(None, "Hello World", {"class": "test"})
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "test"})
    def test_constructor_empty(self):
        node = LeafNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html(self):
        node = LeafNode("p", "Hello World", {"class": "test"})
        self.assertEqual(node.to_html(), '<p class="test">Hello World</p>')
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello World", {"class": "test"})
        self.assertEqual(node.to_html(), "Hello World")
    def test_to_html_no_value(self):
        node = LeafNode("p", None, {"class": "test"})
        with self.assertRaises(ValueError):
            node.to_html()
    def test_to_html_no_props(self):
        node = LeafNode("p", "Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")

class testParentNode(unittest.TestCase):
    def test_constructor(self):
        node = ParentNode("div", None, ["child1", "child2"], {"class": "test"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, ["child1", "child2"])
        self.assertEqual(node.props, {"class": "test"})
    def test_constructor_empty(self):
        node = ParentNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html(self):
        child1 = LeafNode("p", "Hello World")
        child2 = LeafNode("span", "Test")
        node = ParentNode("div", None, [child1, child2], {"class": "test"})
        self.assertEqual(node.to_html(), '<div class="test"><p>Hello World</p><span>Test</span></div>')
    def test_to_html_no_tag(self):
        child1 = LeafNode("p", "Hello World")
        child2 = LeafNode("span", "Test")
        node = ParentNode(None, None, [child1, child2], {"class": "test"})
        with self.assertRaises(ValueError):
            node.to_html()
    def test_to_html_no_children(self):
        node = ParentNode("div", None, None, {"class": "test"})
        with self.assertRaises(ValueError):
            node.to_html()
    def test_to_html_no_props(self):
        child1 = LeafNode("p", "Hello World")
        child2 = LeafNode("span", "Test")
        node = ParentNode("div", None, [child1, child2])
        self.assertEqual(node.to_html(), '<div><p>Hello World</p><span>Test</span></div>')
    def test_nested_to_html(self):
        child1 = LeafNode("h1", "Title")
        child2 = LeafNode("p", "This is a paragraph.")
        section = ParentNode("section", children=[child1, child2])
        root = ParentNode("div", children=[section], props={"class": "outer"})
        expected = (
            '<div class="outer">'
            '<section>'
            '<h1>Title</h1>'
            '<p>This is a paragraph.</p>'
            '</section>'
            '</div>'
        )
        self.assertEqual(root.to_html(), expected)

class testTextNodeTypetoHtmlNodeType(unittest.TestCase):
    def test_normal_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold_text(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
