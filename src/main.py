import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
dir_path_blog = os.path.join(dir_path_content, "blog")
dir_path_contact = os.path.join(dir_path_content, "contact")
template_path = "./template.html"
basepath = sys.argv[1] if len(sys.argv) > 1 else "/"


def main():

    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs)


main()
