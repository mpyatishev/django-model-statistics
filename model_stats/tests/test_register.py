# -*- coding: utf-8 -*-


import mock

from django.test import TestCase

from ..register import register
from .models import Model


class RegisterTest(TestCase):
    @mock.patch('model_stats.register.Register')
    def test_register_model_with_fields(self, m_register):
        register.register(Model, fields=['views'])

        m_register._init_signals.assert_called_once_with()
        self.assertIn(Model, register._models)
