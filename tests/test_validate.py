# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import linkify.feature.verify
import tests

LINK_LIST = """\
http://www.google.de
A&&&2ASD
not@@?@vlaid
www.helm.de
"""

EXPECTED = """\
True http://www.google.de
True A&&&2ASD
None not@@?@vlaid
True www.helm.de
"""


def test_validate_links(mp):
    with tests.patch_urllib(mp):
        dumped = linkify.feature.verify.work(LINK_LIST)
    assert dumped == EXPECTED
