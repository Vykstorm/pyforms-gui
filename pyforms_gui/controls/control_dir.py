#!/usr/bin/python
# -*- coding: utf-8 -*-

from confapp import conf

from pyforms_gui.controls.control_text import ControlText

import pyforms_gui.utils.tools as tools


from AnyQt           import uic
from AnyQt.QtWidgets import QFileDialog


class ControlDir(ControlText):

    def init_form(self):
        control_path = tools.getFileInSameDirectory(__file__, "fileInput.ui")
        self._form = uic.loadUi(control_path)
        self._form.label.setText(self._label)
        self._form.lineEdit.setText(self._value)
        super().init_form()

    def click(self):
        value = str(QFileDialog.getExistingDirectory(self._form, 'Choose a directory', self.value))
        if value: self.value = value

    @property
    def parent(self): return ControlText.parent.fget(self, value)

    @parent.setter
    def parent(self, value):
        ControlText.parent.fset(self, value)
        self._form.pushButton.clicked.connect(self.click)
