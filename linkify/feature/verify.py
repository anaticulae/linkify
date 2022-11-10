# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configo
import utila

import linkify.link
import linkify.serialize

# Limit request to secure server to overload
HTTP_REQUEST_PARALLEL_MAX = configo.HV_INT_PLUS(default=16)


def work(links: str, offline: bool = False) -> str:
    parsed = parse_links(links, offline=offline)
    dumped = linkify.serialize.dump_links(parsed)
    return dumped


def parse_links(path, offline: bool = False):
    loaded = linkify.serialize.load_links(path)
    with utila.GeorgFork(
            process=False,
            returncode=False,
            worker=HTTP_REQUEST_PARALLEL_MAX,
    ) as fork:
        for link in loaded:
            fork.fork(
                method=linkify.link.verify,
                url=link,
                allgreen=offline,
            )
    result = list(zip(
        loaded,
        fork.result,
    ))
    return result
