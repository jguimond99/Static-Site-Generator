import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode



class TestHTMLNode(unittest.TestCase):
	def test_key_value_pair(self):
		node = HTMLNode(props={"href": "https://www.boot.dev"}, value="test")
		actual = node.props_to_html()
		self.assertEqual(actual, ' href="https://www.boot.dev"')

	def test_props_none(self):
		node = HTMLNode()
		actual = node.props_to_html()
		self.assertEqual(actual, "")

	def test_props_empty_dict(self):
		node = HTMLNode(props={})
		actual = node.props_to_html()
		self.assertEqual(actual, "")


	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
		self.assertEqual(
			node.to_html(),
			'<a href="https://www.boot.dev">Click me!</a>',
		)

	def test_leaf_to_html_no_tag(self):
		node = LeafNode(None, "Hello, world!")
		self.assertEqual(node.to_html(), "Hello, world!")

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_many_children(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None,"Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		self.assertEqual(
			node.to_html(),
			"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
		)

	def test_headings(self):
		node = ParentNode(
			"h2",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		self.assertEqual(
			node.to_html(),
			"<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
		)
