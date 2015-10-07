# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from datetime import datetime

import dateutil

from mixbox import entities

import cybox.bindings.cybox_common as common_binding

DATE_PRECISION_VALUES = ("year", "month", "day")
TIME_PRECISION_VALUES = ("hour", "minute", "second")
DATETIME_PRECISION_VALUES = DATE_PRECISION_VALUES + TIME_PRECISION_VALUES

def parse_value(value):
    if not value:
        return None
    elif isinstance(value, datetime):
        return value
    return dateutil.parser.parse(value)


def serialize_value(value):
    if not value:
        return None
    return value.isoformat()


class DateTimeWithPrecision(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.DateTimeWithPrecisionType
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self, value=None, precision='second'):
        super(DateTimeWithPrecision, self).__init__()
        self.value = value
        self.precision = precision

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = parse_value(value)

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        if value not in DATETIME_PRECISION_VALUES:
            raise ValueError("value must be one of [%s]" % ", ".join(x for x in DATETIME_PRECISION_VALUES))

        self._precision = value

    def to_obj(self, ns_info=None):
        obj = super(DateTimeWithPrecision, self).to_dict()
        obj.valueOf_ = serialize_value(self.value)
        obj.precision = self._precision
        return obj

    @classmethod
    def from_obj(cls, obj):
        if not obj:
            return None

        return_obj = cls()
        return_obj.value = obj.valueOf_
        return_obj.precision = obj.precision
        return return_obj

    def to_dict(self):
        value = serialize_value(self.value)
        if self.precision == 'second':
            return value

        dict_ = super(DateTimeWithPrecision, self).to_dict()
        dict_['precision'] = self.precision
        dict_['value'] = value
        return dict_

    @classmethod
    def from_dict(cls, dict_):
        if not dict_:
            return None

        return_obj = cls()

        if not isinstance(dict_, dict):
            return_obj.value = dict_
        else:
            return_obj.precision = dict_.get('precision')
            return_obj.value = dict_.get('value')

        return return_obj


class DateWithPrecision(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.DateWithPrecisionType
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self, value=None, precision='day'):
        super(DateWithPrecision, self).__init__()
        self.value = value
        self.precision = precision

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = parse_value(value)
        if isinstance(self._value, datetime):
            self._value = self._value.date()

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        if value not in DATE_PRECISION_VALUES:
            raise ValueError("value must be one of [%s]" % ", ".join(x for x in DATE_PRECISION_VALUES))

        self._precision = value

    def to_obj(self, ns_info=None):
        obj = super(DateWithPrecision, self).to_obj(ns_info)
        obj.valueOf_ = serialize_value(self.value)
        obj.precision = self._precision
        return obj

    @classmethod
    def from_obj(cls, obj):
        if not obj:
            return None

        return_obj = cls()
        return_obj.value = obj.valueOf_
        return_obj.precision = obj.precision
        return return_obj

    def to_dict(self):
        value = serialize_value(self.value)
        if self.precision == 'day':
            return value

        dict_ = super(DateWithPrecision, self).to_dict()
        dict_['precision'] = self.precision
        dict_['value'] = value
        return dict_

    @classmethod
    def from_dict(cls, dict_):
        if not dict_:
            return None

        return_obj = cls()

        if not isinstance(dict_, dict):
            return_obj.value = dict_
        else:
            return_obj.precision = dict_.get('precision')
            return_obj.value = dict_.get('value')
        return return_obj    
