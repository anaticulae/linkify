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


def work(links: str) -> str:
    parsed = parse_links(links)
    raw = utila.NEWLINE.join(parsed)
    return raw


def parse_links(path):
    loaded = utila.from_raw_or_path(path)
    splitted = [item for item in loaded.splitlines() if item]

    result = []
    for item in splitted:
        verified = linkify.link.verify(item)
        result.append(f'{verified} {item}')
    return result
