#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import contextlib
import functools
import http

import urllib3
import utila
import utilatest

import linkify.cli

# pylint:disable=C0103
run = functools.partial(
    utilatest.run_command,
    main=linkify.cli.main,
    process=linkify.PROCESS,
    success=True,
)
fail = functools.partial(
    utilatest.run_command,
    main=linkify.cli.main,
    process=linkify.PROCESS,
    success=False,
)


@contextlib.contextmanager
def patch_urllib(monkeypatch):
    with monkeypatch.context() as context:
        context.setattr(
            urllib3.request.RequestMethods,
            'request',
            lambda _, __, ___: urllib3.HTTPResponse(status=http.HTTPStatus.OK),
        )
        yield
