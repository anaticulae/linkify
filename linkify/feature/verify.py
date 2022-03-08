# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import linkify.link
import linkify.serialize


def work(links: str, offline: bool = False) -> str:
    parsed = parse_links(links, offline=offline)
    dumped = linkify.serialize.dump_links(parsed)
    return dumped


def parse_links(path, offline: bool = False):
    loaded = linkify.serialize.load_links(path)
    result = []
    for link in loaded:
        verified = linkify.link.verify(link, allgreen=offline)
        result.append((link, verified))
    return result
