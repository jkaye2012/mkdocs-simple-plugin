""" md
## Python Version

You can put _markdown_ in triple-quoted strings in Python.

You can even combine it with mkdocstrings to automatically generate your source documentation!

::: module.main
    handler: python
    rendering:
        show_root_heading: true
        show_source: false
        heading_level: 3
"""


def main():
    """
    This is a test function.  It takes no paramers.

    It says "Hello, world!"
    """
    print("Hello, world!")
    return 0