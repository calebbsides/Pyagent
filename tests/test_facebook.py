import pytest
from pyagent.tools.facebook_tool import create_fb_post

def test_create_fb_post_returns_expected_string():
    content = "Hello, Facebook!"
    result = create_fb_post(content)
    assert result == f"Posted to Facebook: {content}"

def test_create_fb_post_prints_output(capfd):
    content = "Test post"
    create_fb_post(content)
    out, _ = capfd.readouterr()
    assert f"Creating Facebook post with content: {content}" in out
