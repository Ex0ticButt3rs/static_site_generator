from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.tag in ["img", "link", "input", "meta", "source"]:
            if self.props is None or self.props == {}:
                return f"<{self.tag}>"
            else:
                i = self.props_to_html()
                return f"<{self.tag} {i}>"
        else:
            if self.value is None or self.value == "":
                print("BAD LEAF:", self.tag, repr(self.value), self.props)
                raise ValueError("value is none or empty string")
            if self.tag is None:
                return f"{self.value}"
            if self.props is None or self.props == {}:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                i = self.props_to_html()
                return f"<{self.tag} {i}>{self.value}</{self.tag}>"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"