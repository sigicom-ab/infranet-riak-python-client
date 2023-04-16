#!/usr/bin/env python

from setuptools import setup
from commands import setup_timeseries, build_messages

setup(
    cmdclass={
        "build_messages": build_messages,
        "setup_timeseries": setup_timeseries,
    }
)
