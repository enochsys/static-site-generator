import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_blog = os.path.join(dir_path_content, "blog")
dir_path_contact = os.path.join(dir_path_content, "contact")
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()
