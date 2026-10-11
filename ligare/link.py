# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import http

import configos
import urllib3
import utilo

HTTP_TIMEOUT = configos.HV_SECOND(default=5)


def verify(url, allgreen: bool = False) -> bool:
    """Check connection for given `url`.

    Args:
        url(str): url to check
        allgreen(bool): if True, all valid urls are treated as connectable
    Returns:
        True if connection is possible
        False if server is not reachable
        None if given `url` is not valid

    Not a valid url:

    >>> verify('not@@?@vlaid', False) is None
    True
    """
    # disable urllib logging
    urllib3.logging.disable()
    try:
        # validate url
        connection = urllib3.connection_from_url(
            url,
            timeout=HTTP_TIMEOUT,
        )
    except ValueError:
        # not a valid url
        return None
    if allgreen:
        return True
    try:
        requested = connection.request('GET', '/')
    except Exception as error:  # pylint:disable=broad-except
        utilo.error(error)
        return False
    return requested.status == http.HTTPStatus.OK
