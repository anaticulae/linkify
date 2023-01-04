#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import contextlib
import http

import urllib3
import utilatest

import linkify

run, fail = utilatest.create_cli_runner(linkify)


@contextlib.contextmanager
def patch_urllib(mp):
    with mp.context() as context:
        context.setattr(
            urllib3.request.RequestMethods,
            'request',
            lambda _, __, ___: urllib3.HTTPResponse(status=http.HTTPStatus.OK),
        )
        yield
