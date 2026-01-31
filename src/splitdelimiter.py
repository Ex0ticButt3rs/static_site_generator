from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list_of_nodes = []
    for nodes_object in old_nodes:
        if nodes_object.text_type != TextType.TEXT:
            new_list_of_nodes.append(nodes_object)
            continue
        elif delimiter not in nodes_object.text:
            new_list_of_nodes.append(nodes_object)
            continue        
        else:
            split_list_of_words = nodes_object.text.split(delimiter)
            if len(split_list_of_words) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for i in range(len(split_list_of_words)):
                part = split_list_of_words[i]
                if part == "":
                    continue
                if i % 2 == 0:
                    new_list_of_nodes.append(TextNode(split_list_of_words[i], TextType.TEXT))
                else:
                    new_list_of_nodes.append(TextNode(split_list_of_words[i], text_type))
    return new_list_of_nodes