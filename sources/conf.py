import sys
import os
from datetime import UTC, datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "."))

author = "Mickaël Schoentgen"
project = "Knowledge Base &ndash; Tiger-222"
this_year = datetime.now(tz=UTC).year
copyright = f"2006-{this_year}, {author}"
url = "https://www.tiger-222.fr"

extensions = [
    'myst_parser', 
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_tabs.tabs",
    "sphinx_togglebutton",
]
html_theme = "shibuya"
exclude_patterns = ['_build', "venv"]
html_static_path = ["_static"]
templates_path = ["_templates"]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

html_title = project
html_theme = "shibuya"
html_baseurl = f"{url}/"
sitemap_url_scheme = "{link}"
html_show_sourcelink = True
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "accent_color": "purple",
    "logo_target": "/",
    "light_logo": "_static/favicon.ico",
    "dark_logo": "_static/favicon.ico",
    "globaltoc_expand_depth": 2,

    "og_image_url": f"{url}/icon.png",
    "twitter_creator": "__tiger222__",
    "twitter_site": "__tiger222__",

    "twitter_url": "https://twitter.com/__tiger222__",
    "github_url": "https://github.com/BoboTiG",

    "globaltoc_expand_depth": 2,
    "nav_links": [
        {
            "title": "Blog",
            "url": url
        },
        {
            "title": "Liens",
            "url": f"{url}/links"
        },
    ]
}
html_context = {
    "source_type": "github",
    "source_user": "BoboTiG",
    "source_repo": "kb",
}