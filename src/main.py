import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

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
    generate_page(
        os.path.join(dir_path_blog, "glorfindel/index.md"),
        template_path,
        os.path.join(dir_path_public, "blog/glorfindel/index.html"),
    )
    generate_page(
        os.path.join(dir_path_blog, "majesty/index.md"),
        template_path,
        os.path.join(dir_path_public, "blog/majesty/index.html"),
    )
    generate_page(
        os.path.join(dir_path_blog, "tom/index.md"),
        template_path,
        os.path.join(dir_path_public, "blog/tom/index.html"),
    )
    generate_page(
        os.path.join(dir_path_contact, "index.md"),
        template_path,
        os.path.join(dir_path_public, "contact/index.html"),
    )
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()
