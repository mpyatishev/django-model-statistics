# -*- coding: utf-8 -*-

import sys

from django.conf import settings

from model_stats.tests import settings as test_settings


if not settings.configured:
    settings.configure(**test_settings.__dict__)


from django_nose import NoseTestSuiteRunner


def runtests(*args):
    failures = NoseTestSuiteRunner(verbosity=2, interactive=True).run_tests(args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
