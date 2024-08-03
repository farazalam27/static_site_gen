from htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag:
            props = f" {self.props_to_html()}" if self.props else ""
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
        else:
            return self.value






