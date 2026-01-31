from textnode import TextNode, TextType
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def extract_markdown_images(text):
    image_match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_match

def extract_markdown_links(text):
    url_match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return url_match

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes