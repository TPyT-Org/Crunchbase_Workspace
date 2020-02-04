
import os
from types import SimpleNamespace


def stage():
    if 'PYTHON_ENV' in os.environ:
        return os.environ['PYTHON_ENV']
    else:
        return 'test'


def build_settings():
    return SimpleNamespace(**{
        'database': 'test.sqlite',
        'stage': 'test',
    })


settings = build_settings()
