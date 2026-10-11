#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import contextlib
import http

import urllib3
import utilotest

import ligare

run, fail = utilotest.create_cli_runner(ligare)


@contextlib.contextmanager
def patch_urllib(mp):

    def mock_request(self, method, url, **kwargs):  # pylint: disable=unused-argument
        return urllib3.HTTPResponse(
            status=http.HTTPStatus.OK,
            body=b"OK",
        )

    mp.setattr(
        urllib3.HTTPConnectionPool,
        "request",
        mock_request,
    )
    yield
