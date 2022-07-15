import jinja2

env = jinja2.Environment(
    loader=jinja2.PackageLoader("main", "static"),
    autoescape=jinja2.select_autoescape()
)

template = env.get_template("index.jinja")

print(template.render(footer="footer text", body="body text", header="header text"))
