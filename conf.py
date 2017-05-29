from __future__ import unicode_literals

import time

SITE_URL = "https://ransonr.github.io/"
BLOG_AUTHOR = "Ryan Ranson"
BLOG_TITLE = "ransonr.github.io"
BLOG_EMAIL = "ryan.ranson@gmail.com"
BLOG_DESCRIPTION = "Ryan Ranson's GitHub Page"

# POSTS and PAGES contains (wildcard, destination, template) tuples.
# The difference between POSTS and PAGES is that POSTS are added
# to feeds, indexes, tag lists and archives and are considered part
# of a blog, while PAGES are just independent HTML pages.
POSTS = (
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
    ("posts/*.ipynb", "posts", "post.tmpl"),
)
PAGES = (
    ("pages/*.md", "", "story.tmpl"),
    ("pages/*.txt", "", "story.tmpl"),
    ("pages/*.html", "", "story.tmpl"),
    ("pages/*.ipynb", "", "story.tmpl"),
)

COMPILERS = {
    "rest": (".rst", ".txt"),
    "markdown": (".md", ".markdown"),
    "wiki": (".wiki",),
    "ipynb": (".ipynb",),
    "html": (".html", ".htm"),
}

TIMEZONE = "America/Chicago"

# Create posts in single-file format by default
ONE_FILE_POSTS = True

DEFAULT_LANG = "en"
TRANSLATIONS = {DEFAULT_LANG: ""}
TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"

# To avoid a conflict because blogs try to generate /index.html
# See: https://getnikola.com/creating-a-site-not-a-blog-with-nikola.html
INDEX_PATH = "blog"

# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
COPY_SOURCES = False

# If a link ends in /index.html,  drop the index.html part.
STRIP_INDEXES = True

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
PRETTY_URLS = True

# If you hate "Filenames with Capital Letters and Spaces.md", you should set this to true.
UNSLUGIFY_TITLES = True

DATE_FORMAT = "%B %-d, %Y"

# Links for the sidebar / navigation bar
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/about/', 'About'),
        ('/blog/', 'Posts'),
        ('/projects/', 'Projects'),
    ),
}

THEME = 'custom'

# Primary color of your theme. This will be used to customize your theme and
# auto-generate related colors in POSTS_SECTION_COLORS. Must be a HEX value.
THEME_COLOR = '#81a1ca'

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored. Leave empty to disable.
# Can be any of:
# algol, algol_nu, autumn, borland, bw, colorful, default, emacs, friendly,
# fruity, igor, lovelace, manni, monokai, murphy, native, paraiso-dark,
# paraiso-light, pastie, perldoc, rrt, tango, trac, vim, vs, xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# Check with list(pygments.styles.get_all_styles()) in an interpreter.
# CODE_COLOR_SCHEME = 'default'

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# )

# github_deploy configuration
# For more details, read the manual:
# https://getnikola.com/handbook.html#deploying-to-github
# You will need to configure the deployment branch on GitHub.
GITHUB_SOURCE_BRANCH = 'src'
GITHUB_DEPLOY_BRANCH = 'master'
GITHUB_REMOTE_NAME = 'origin'
GITHUB_COMMIT_SOURCE = True

# Show teasers (instead of full posts) in indexes
INDEX_TEASERS = True

# 'Read more...' for the index page (if INDEX_TEASERS is True)
INDEX_READER_MORE_LINK = '<p class="more"><a href="{link}">{read_more}...</a></p>'

# Writes tag cloud data in form of tag_cloud_data.json.
# Warning: this option will change its default value to False in v8!
WRITE_TAG_CLOUD = False

# If you do not want to display a tag publicly, you can mark it as hidden.
# The tag will not be displayed on the tag list page, the tag cloud and posts.
# Tag pages will still be generated.
HIDDEN_TAGS = ["mathjax"]

IMAGE_FOLDERS = {"images": "images"}
# IMAGE_THUMBNAIL_SIZE = 400
# IMAGE_THUMBNAIL_FORMAT = '{name}.thumbnail{ext}'

COMMENT_SYSTEM = ""

# A small copyright notice for the page footer (in HTML).
CONTENT_FOOTER = "Contents &copy; {date} <a href='mailto:{email}'>{author}</a> - Powered by <a href='https://getnikola.com' rel='nofollow'>Nikola</a> {license}"

# Things that will be passed to CONTENT_FOOTER.format()
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format()
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": ""
        }
    )
}

# If you want support for the $.$ syntax (which may conflict with running
# text!), just use this config:
MATHJAX_CONFIG = """
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
        processEscapes: true
    },
    displayAlign: 'center', // Change this to 'left' if you want left-aligned equations.
    "HTML-CSS": {
        styles: {'.MathJax_Display': {"margin": 0}}
    }
});
</script>
"""

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# The default is ['fenced_code', 'codehilite']
MARKDOWN_EXTENSIONS = [
    'markdown.extensions.fenced_code',
    'markdown.extensions.codehilite',
    'markdown.extensions.extra',
]

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
GENERATE_RSS = False

# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# BODY_END = """
# <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.5/styles/default.min.css">
# <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.5/highlight.min.js"></script>
# <script>hljs.initHighlightingOnLoad();</script>
# """

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# Enabling hyphenation has been shown to break math support in some cases,
# use with caution.
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example. (defaults to 1.)
DEMOTE_HEADERS = 1

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {'GITHUB_URL': 'https://github.com/ransonr/'}

# Add functions here and they will be called with template GLOBAL_CONTEXT
# as parameter when the template is about to be rendered
GLOBAL_CONTEXT_FILLER = []
