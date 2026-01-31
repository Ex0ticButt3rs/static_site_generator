from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        if self.props == None or self.props == {}:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            i = self.props_to_html()
            return f"<{self.tag} {i}>{self.value}</{self.tag}>"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"