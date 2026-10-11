#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import utilo

import ligare

WORKPLAN = [
    utilo.create_step(
        'verify',
        inputs=[
            utilo.ResultFile(producer='links', name='todo'),
            utilo.Bool('offline')
        ],
        output=('verified',),
    )
]


def main():
    utilo.featurepack(
        workplan=WORKPLAN,
        root=ligare.ROOT,
        featurepackage='ligare.feature',
        config=utilo.FeaturePackConfig(
            description='',
            multiprocessed=True,
            name=ligare.PROCESS,
            version=ligare.__version__,
        ),
    )
