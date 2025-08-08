#!/usr/bin/env python3
import pytest
from transformations import (
    transform_page_links,
    transform_header_links,
    transform_image_links,
    run_all_transformations
)

# --- Test Data ---

OBSIDIAN_PAGE_LINK = 'This is a test [[Page Name|with some link text]].'
GITHUB_PAGE_LINK = 'This is a test [[with some link text|Page-Name]].'

OBSIDIAN_HEADER_LINK = 'Link to a [[#Some Header|custom display text]].'
GITHUB_HEADER_LINK = 'Link to a [custom display text](#some-header).'

OBSIDIAN_IMAGE_LINK = 'Here is an image ![[my-image.png]].'
GITHUB_IMAGE_LINK = 'Here is an image  [[my-image.png]].'

# --- Tests for Individual Transformations ---

def test_page_link_transformation():
    """Tests the page link transformation."""
    assert transform_page_links(OBSIDIAN_PAGE_LINK) == GITHUB_PAGE_LINK

def test_header_link_transformation():
    """Tests the header link transformation."""
    assert transform_header_links(OBSIDIAN_HEADER_LINK) == GITHUB_HEADER_LINK

def test_image_link_transformation():
    """Tests the image link transformation."""
    assert transform_image_links(OBSIDIAN_IMAGE_LINK) == GITHUB_IMAGE_LINK

# --- Test for Combined Transformations ---

def test_all_transformations():
    """Tests running all transformations together."""
    obsidian_text = f"{OBSIDIAN_PAGE_LINK}\n{OBSIDIAN_HEADER_LINK}\n{OBSIDIAN_IMAGE_LINK}"
    github_text = f"{GITHUB_PAGE_LINK}\n{GITHUB_HEADER_LINK}\n{GITHUB_IMAGE_LINK}"
    assert run_all_transformations(obsidian_text) == github_text

# --- Edge Case Tests ---

def test_no_links():
    """Tests text with no links, should not be changed."""
    text = "This is a simple text with no links."
    assert run_all_transformations(text) == text

def test_empty_string():
    """Tests an empty string, should remain empty."""
    assert run_all_transformations("") == ""
