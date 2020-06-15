# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import linkify.path
import tests
import tests.test_validate


def test_cli(monkeypatch):
    tests.run('--help', monkeypatch=monkeypatch)


def test_offline_flag(testdir, monkeypatch):
    utila.file_create(
        'detector__bibliography_links.yaml',
        tests.test_validate.LINK_LIST,
    )
    tests.run('--offline', monkeypatch=monkeypatch)

    loaded = utila.file_read(linkify.path.verified(testdir.tmpdir))
    assert loaded == tests.test_validate.EXPECTED
