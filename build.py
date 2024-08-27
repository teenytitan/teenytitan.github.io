from jinja2 import Template
import shutil

pages = [
    {"name": "index", "label": "Home"},
    {"name": "solutions", "label": "What We Offer"},
    {"name": "portfolio", "label": "Portfolio"},
    {"name": "manifesto", "label": "Why Us?"},
    {"name": "contact", "label": "Contact Us"},
]


with open("layout.html") as f:
    layout = f.read()
template = Template(layout)


for page in pages:
    # build nav
    nav_src = ""
    for p in pages:
        css_class = "active" if p["name"] == page["name"] else "inactive"
        nav_src += f"""<li><a class="{css_class}" href="{p["name"]}.html">{p["label"]}</a></li>\n"""

    try:
        with open(f"fragments/{page['name']}.html") as f:
            content = f.read()
        result = template.render(content=content, nav_src=nav_src)

        with open(f"docs/{page['name']}.html", "w") as f:
            f.write(result)
    except:
        print(f"failed to load and render {page}.html")
        continue

shutil.copytree("css", "docs/css/", dirs_exist_ok=True)
