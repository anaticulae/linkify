#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import utila

import linkify

WORKPLAN = [
    utila.create_step(
        'verify',
        inputs=[
            utila.ResultFile(producer='detector', name='bibliography_links'),
        ],
        output=('verified',),
    )
]


def main():
    utila.featurepack(
        workplan=WORKPLAN,
        root=linkify.ROOT,
        featurepackage='linkify.feature',
        config=utila.FeaturePackConfig(
            description='',
            multiprocessed=True,
            name=linkify.PROCESS,
            pages=True,
            version=linkify.__version__,
        ),
    )
