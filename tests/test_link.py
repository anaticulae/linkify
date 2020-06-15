# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import http

import pytest
import urllib3
import urllib3.request

import linkify.link


@pytest.mark.parametrize('url, green, expected', [
    ('http://www.google.de', False, False),
    ('http://www.checkitweg.de', True, True),
])
def test_verify_link(url, green, expected):
    result = linkify.link.verify(url=url, allgreen=green)
    assert result == expected


def test_verify_mocked(monkeypatch):
    with monkeypatch.context() as context:
        context.setattr(
            urllib3.request.RequestMethods,
            'request',
            lambda _, __, ___: urllib3.HTTPResponse(status=http.HTTPStatus.OK),
        )
        result = linkify.link.verify(url='http://www.amazon.com')
    assert result
