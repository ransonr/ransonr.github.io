# [Ryan Ranson's GitHub Page](https://ransonr.github.io)

---

Static site built with [Nikola](https://getnikola.com). This uses a custom theme and attempts to strip out as much as possible from `conf.py`. The `src` branch contains the source code used to build the site and the `master` branch only contains what is deployed.

To build the site::

    nikola build

To see it::

    nikola serve -b

To deploy to GitHub Pages::

    nikola github_deploy

To check all available commands::

    nikola help
