# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila


def load_links(path: str) -> list:
    loaded = utila.from_raw_or_path(path)
    splitted = [item for item in loaded.splitlines() if item]
    return splitted


def dump_links(links) -> str:
    result = [f'{status} {link}' for link, status in links]
    raw = utila.NEWLINE.join(result) + utila.NEWLINE
    return raw
