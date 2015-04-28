# -*- coding: utf-8 -*-


import mock

from django.test import TestCase

from ..register import register
from .models import Model


class RegisterTest(TestCase):
    def test_register_model_with_fields(self):
        register.add(Model, fields=['views'])

        self.assertIn(Model, register._models)
