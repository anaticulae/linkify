# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configos
import utilo

import ligare.link
import ligare.serialize

# Limit request to secure server to overload
HTTP_REQUEST_PARALLEL_MAX = configos.HV_INT_PLUS(default=16)


def work(links: str, offline: bool = False) -> str:
    parsed = parse_links(links, offline=offline)
    dumped = ligare.serialize.dump_links(parsed)
    return dumped


def parse_links(path, offline: bool = False):
    loaded = ligare.serialize.load_links(path)
    with utilo.GeorgFork(
            process=False,
            returncode=False,
            worker=HTTP_REQUEST_PARALLEL_MAX,
    ) as fork:
        for link in loaded:
            fork.fork(
                method=ligare.link.verify,
                url=link,
                allgreen=offline,
            )
    result = list(zip(
        loaded,
        fork.result,
    ))
    return result
