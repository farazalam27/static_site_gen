from htmlnode import HtmlNode
class ParentNode(HtmlNode):
    def __init__(self, children, tag=None, props=None):
        if not isinstance(children, list):
            raise TypeError("children must be a list")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag given")
        if not self.children:
            raise ValueError("No children given")

        props = f" {self.props_to_html()}" if self.props else ""
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props}>{children_html}</{self.tag}>"
