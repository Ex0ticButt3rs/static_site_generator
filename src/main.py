from textnode import TextNode, TextType
import os
import shutil
import re
from splitblocks import markdown_to_html_node
from parentnode import ParentNode

def main():
    source = "static"
    destination = "public"
    if os.path.exists(destination):    
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_static(source, destination)
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"
    generate_page(from_path, template_path, dest_path)

def extract_title(markdown):
    substrings_list = markdown.split("\n")
    for line in substrings_list:
        if re.match(r"^#\s+.+", line):
            text = line.lstrip("#").strip()
            return text
    raise Exception("no h1 header line exists")

def copy_static(source, destination):
    if not os.path.exists(source):
        raise Exception("static folder is missing or misnamed")
    if not os.path.exists(destination):
        raise Exception("provided destination isn't an existing path")
    
    for i in os.listdir(source):
        entry_path = os.path.join(source, i)
        if os.path.isfile(entry_path):
            shutil.copy(entry_path, destination)
        else:
            dest_directory = os.path.join(destination, i)
            os.mkdir(dest_directory)
            copy_static(entry_path, dest_directory)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, mode='r') as opened_markdown_object:
        markdown_read_string = opened_markdown_object.read()
        markdown_parent_node = markdown_to_html_node(markdown_read_string)
        markdown_to_html_result = markdown_parent_node.to_html()
        page_title = extract_title(markdown_read_string)
    with open(template_path, mode='r') as opened_template_object:
        template_read_string = opened_template_object.read()
        updated_template_string = template_read_string.replace("{{ Title }}", page_title).replace("{{ Content }}", markdown_to_html_result)
        dir_name = os.path.dirname(dest_path)
        if dest_path and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(dest_path, mode='w') as opened_destination_object:
            opened_destination_object.write(updated_template_string)

if __name__ == "__main__":
    main()