#!/usr/bin/python
# -*- coding: utf-8 -*-

from confapp import conf

from AnyQt           import uic
from AnyQt.QtWidgets import QPushButton, QSizePolicy
from AnyQt.QtGui     import QIcon

from pyforms_gui.controls.control_base import ControlBase


class ControlButton(ControlBase):
    def __init__(self, *args, **kwargs):
        """
        ...

        :param str icon: Button icon
        :param bool checkable: Flag to set the button checkable.
        
        """
        self._checkable = kwargs.get('checkable', False)
        super(ControlButton, self).__init__(*args, **kwargs)

        default = kwargs.get('default', None)
        if default: self.value = default

        icon = kwargs.get('icon', None)
        if icon: self.icon = icon

    def init_form(self):
        self._form = QPushButton()
        self._form.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self._form.setCheckable(self._checkable)
        self.label = self._label
        self._form.setToolTip(self.help)
        super().init_form()

    def click(self):
        """
        Trigger a click event
        """
        self._form.click()

    def load_form(self, data, path=None):
        pass

    def save_form(self, data, path=None):
        pass

    ##########################################################################

    @property
    def label(self):
        return ControlBase.label.fget(self)

    @label.setter
    def label(self, value):
        ControlBase.label.fset(self, value)
        self._form.setText(self._label)

    @property
    def icon(self):
        """
        Sets and gets the icon of the button.
        """
        return self._form.icon()

    @icon.setter
    def icon(self, value):
        if isinstance(value, (str, bytes)):
            self._form.setIcon(QIcon(value))
        else:
            self._form.setIcon(value)

    ##########################################################################

    @property
    def value(self):
        """
        Sets and gets the value of the Button. The value should be a function
        """
        return None

    @value.setter
    def value(self, value):
        try:
            self._form.clicked.disconnect()  # ignore previous signals if any
        except TypeError as err:
            # http://stackoverflow.com/questions/21586643/pyqt-widget-connect-and-disconnect
            pass
        self._form.clicked[bool].connect(value)

    @property
    def checked(self):
        """
        Sets and gets the button checked state
        """
        return self._form.isChecked()

    @checked.setter
    def checked(self, value):
        self._form.setChecked(value)
