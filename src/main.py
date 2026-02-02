from textnode import TextNode, TextType
import os
import shutil

def main():
    source = "static"
    destination = "public"
    
    if os.path.exists(destination):    
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_static(source, destination)    

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

if __name__ == "__main__":
    main()