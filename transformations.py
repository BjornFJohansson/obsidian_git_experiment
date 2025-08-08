#!/usr/bin/env python3
import re

# PAGE LINK CONVERSION
# [[file name|link text]] --> [[link text|file-name]]
def switch_fn_linktext(m):
    # Groups are now: 1: '[[', 2: pagename, 3: linktext, 4: ']]'
    linktext = m.group(3)
    pagename = m.group(2).replace(" ", "-")
    sub = f"{m.group(1)}{linktext}|{pagename}{m.group(4)}"
    return sub

def transform_page_links(text):
    # This regex now specifically looks for links that are NOT image links (![[...]])
    # and not header links ([[#...]]) by checking the first characters.
    return re.sub(r"(?<!!)(\[\[)([^#\[\]][^\[\]]*?)\|([^\[\]|]+?)(\]\])", switch_fn_linktext, text)

# HEADER LINK CONVERSION
# [[#Some header in the page|some text]] --> [some text](#some-header-in-the-page)
def links_to_header(m):
    linktext = m.group(2)
    pagename = m.group(1).replace(" ", "-").lower()
    sub = f"[{linktext}]({pagename})"
    return sub

def transform_header_links(text):
    return re.sub(r"\[\[(#[^#|\[\]]+?)\|([^\[\]|]+?)\]\]", links_to_header, text)

# IMAGE LINK CONVERSION
# ![[some image.png]] --> [[some image.png]]
def remove_exclamation_mark(m):
    sub = " " + m.group(2)
    return sub

def transform_image_links(text):
    return re.sub(r"(!)(\[\[.+\]\])", remove_exclamation_mark, text)

def run_all_transformations(text):
    text = transform_page_links(text)
    text = transform_header_links(text)
    text = transform_image_links(text)
    return text
