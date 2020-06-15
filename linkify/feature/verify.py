# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import linkify.link


def work(links: str, offline: bool = False) -> str:
    parsed = parse_links(links, offline=offline)
    raw = utila.NEWLINE.join(parsed)
    return raw


def parse_links(path, offline: bool = False):
    loaded = utila.from_raw_or_path(path)
    splitted = [item for item in loaded.splitlines() if item]

    result = []
    for item in splitted:
        verified = linkify.link.verify(item, allgreen=offline)
        result.append(f'{verified} {item}')
    return result
