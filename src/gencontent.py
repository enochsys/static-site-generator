import os

from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, dest_root):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        content = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    title = extract_title(content)
    html = markdown_to_html_node(content).to_html()

    rel_to_root = os.path.relpath(dest_root, os.path.dirname(dest_path))
    if rel_to_root == ".":
        basepath = ""
    else:
        basepath = rel_to_root + "/"

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No title found in markdown")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                dest_path = os.path.join(
                    dest_dir_path, os.path.relpath(from_path, dir_path_content)
                )
                dest_path = dest_path.replace(".md", ".html")
                generate_page(from_path, template_path, dest_path, dest_dir_path)
