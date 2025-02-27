import sys
from datetime import UTC, datetime
from pathlib import Path

from pygments.lexers.web import PhpLexer
from sphinx.highlighting import lexers

lexers["php"] = PhpLexer(startinline=True, linenos=1)

sys.path.insert(0, f"{Path(__file__).parent}.")

author = "Mickaël Schoentgen"
project = "Base de connaissances du luma"
this_year = datetime.now(tz=UTC).year
copyright = f"2006-{this_year}, {author}"  # noqa:A001
url = "https://www.tiger-222.fr"
language = "fr"

extensions = [
    "myst_parser",
    "sphinx_contributors",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    # "sphinx_design",
    # "sphinx_tabs.tabs",
    "sphinx_togglebutton",
]
myst_enable_extensions = [
    "attrs_inline",
    "deflist",
    "replacements",
    "tasklist",
]
suppress_warnings = ["myst.xref_missing"]
todo_include_todos = True
html_theme = "shibuya"
html_css_files = ["custom.css"]
html_static_path = ["_static"]
templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
togglebutton_hint = "Cliquer pour afficher"
togglebutton_hint_hide = "Cliquer pour cacher"

html_title = project
html_theme = "shibuya"
html_favicon = "_static/favicon.svg"
html_logo = "_static/logo.svg"
html_theme_options = {
    "accent_color": "iris",
    "twitter_creator": "__tiger222__",
    "twitter_site": "__tiger222__",
    "twitter_url": "https://twitter.com/__tiger222__",
    "github_url": "https://github.com/BoboTiG",
    "globaltoc_expand_depth": 2,
    "nav_links": [
        {"title": "Blog", "url": url},
        {"title": "Liens", "url": f"{url}/links"},
    ],
}
html_context = {
    "source_type": "github",
    "source_user": "BoboTiG",
    "source_repo": "luma",
    "source_docs_path": "/sources/",
    "source_version": "main",
}
