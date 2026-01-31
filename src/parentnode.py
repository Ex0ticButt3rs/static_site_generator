from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag is none")
        if self.children == None:
            raise ValueError("children are none")
        if self.children == []:
            raise ValueError("children are empty list")
        children_string = ""
        for child_object in self.children:
            children_string += child_object.to_html()      
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"

    def __eq__(self, other):
        return self.tag == other.tag and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"