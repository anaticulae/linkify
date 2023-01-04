# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import linkify.path
import tests
import tests.test_validate


def test_cli(mp):
    tests.run('--help', mp=mp)


def test_offline_flag(td, mp):
    utila.file_create(
        'links__todo.yaml',
        tests.test_validate.LINK_LIST,
    )
    tests.run('--offline', mp=mp)

    loaded = utila.file_read(linkify.path.verified(td.tmpdir))
    assert loaded == tests.test_validate.EXPECTED
