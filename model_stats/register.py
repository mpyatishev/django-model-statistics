# -*- coding: utf-8 -*-


class Register(object):
    def register(self, model, fields=None):
        self._init_signals()

    def _init_signals(self):
        pass

register = Register()
