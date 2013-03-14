#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Tue Nov 06 14:03:17 2012 by generateDS.py version 2.7c.
#

import sys
import getopt
import re as re_

import cybox_common_types_1_0
import network_route_entry_object_1_1

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    if Verbose_import_:
        print('Error: LXML version 2.3+ required for parsing files')

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'utf-8'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class NetworkRouteEntriesType(GeneratedsSuper):
    """The NetworkRouteEntriesType type is intended to characterize the set
    of network route segments for this route."""
    subclass = None
    superclass = None
    def __init__(self, Network_Route_Entry=None):
        if Network_Route_Entry is None:
            self.Network_Route_Entry = []
        else:
            self.Network_Route_Entry = Network_Route_Entry
    def factory(*args_, **kwargs_):
        if NetworkRouteEntriesType.subclass:
            return NetworkRouteEntriesType.subclass(*args_, **kwargs_)
        else:
            return NetworkRouteEntriesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Network_Route_Entry(self): return self.Network_Route_Entry
    def set_Network_Route_Entry(self, Network_Route_Entry): self.Network_Route_Entry = Network_Route_Entry
    def add_Network_Route_Entry(self, value): self.Network_Route_Entry.append(value)
    def insert_Network_Route_Entry(self, index, value): self.Network_Route_Entry[index] = value
    def export(self, outfile, level, namespace_='NetworkRouteObj:', name_='NetworkRouteEntriesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='NetworkRouteEntriesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='NetworkRouteObj:', name_='NetworkRouteEntriesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='NetworkRouteObj:', name_='NetworkRouteEntriesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Network_Route_Entry_ in self.Network_Route_Entry:
            Network_Route_Entry_.export(outfile, level, 'NetworkRouteObj:', name_='Network_Route_Entry', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Network_Route_Entry
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='NetworkRouteEntriesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Network_Route_Entry=[\n')
        level += 1
        for Network_Route_Entry_ in self.Network_Route_Entry:
            showIndent(outfile, level)
            outfile.write('model_.network_route_entry_object_1_1.NetworkRouteEntryObjectType(\n')
            Network_Route_Entry_.exportLiteral(outfile, level, name_='network_route_entry_object_1_1.NetworkRouteEntryObjectType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Network_Route_Entry':
            obj_ = network_route_entry_object_1_1.NetworkRouteEntryObjectType.factory()
            obj_.build(child_)
            self.Network_Route_Entry.append(obj_)
# end class NetworkRouteEntriesType

class NetRouteObjectType(cybox_common_types_1_0.DefinedObjectType):
    """The NetRouteObjectType type is intended to characterize a specific
    network route.The is_ipv6 attribute specifies whether or not the
    route uses IPv6 addresses.The is_autoconfigure_address specifies
    if the IP address is autoconfigured.The is_immortal attribute
    specifies if the route is immortal.The is_loopback attribute
    specifies if the route is a loopback route (the gateway is on
    the local host).The is_publish attribute specifies if the route
    is published."""
    subclass = None
    superclass = cybox_common_types_1_0.DefinedObjectType
    def __init__(self, object_reference=None, is_publish=None, is_autoconfigure_address=None, is_loopback=None, is_immortal=None, is_ipv6=None, Description=None, Network_Route_Entries=None, Preferred_Lifetime=None, Valid_Lifetime=None, Route_Age=None):
        super(NetRouteObjectType, self).__init__(object_reference, )
        self.is_publish = _cast(bool, is_publish)
        self.is_autoconfigure_address = _cast(bool, is_autoconfigure_address)
        self.is_loopback = _cast(bool, is_loopback)
        self.is_immortal = _cast(bool, is_immortal)
        self.is_ipv6 = _cast(bool, is_ipv6)
        self.Description = Description
        self.Network_Route_Entries = Network_Route_Entries
        self.Preferred_Lifetime = Preferred_Lifetime
        self.Valid_Lifetime = Valid_Lifetime
        self.Route_Age = Route_Age
    def factory(*args_, **kwargs_):
        if NetRouteObjectType.subclass:
            return NetRouteObjectType.subclass(*args_, **kwargs_)
        else:
            return NetRouteObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Network_Route_Entries(self): return self.Network_Route_Entries
    def set_Network_Route_Entries(self, Network_Route_Entries): self.Network_Route_Entries = Network_Route_Entries
    def get_Preferred_Lifetime(self): return self.Preferred_Lifetime
    def set_Preferred_Lifetime(self, Preferred_Lifetime): self.Preferred_Lifetime = Preferred_Lifetime
    def validate_DurationObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.DurationObjectAttributeType, a restriction on None.
        pass
    def get_Valid_Lifetime(self): return self.Valid_Lifetime
    def set_Valid_Lifetime(self, Valid_Lifetime): self.Valid_Lifetime = Valid_Lifetime
    def get_Route_Age(self): return self.Route_Age
    def set_Route_Age(self, Route_Age): self.Route_Age = Route_Age
    def get_is_publish(self): return self.is_publish
    def set_is_publish(self, is_publish): self.is_publish = is_publish
    def get_is_autoconfigure_address(self): return self.is_autoconfigure_address
    def set_is_autoconfigure_address(self, is_autoconfigure_address): self.is_autoconfigure_address = is_autoconfigure_address
    def get_is_loopback(self): return self.is_loopback
    def set_is_loopback(self, is_loopback): self.is_loopback = is_loopback
    def get_is_immortal(self): return self.is_immortal
    def set_is_immortal(self, is_immortal): self.is_immortal = is_immortal
    def get_is_ipv6(self): return self.is_ipv6
    def set_is_ipv6(self, is_ipv6): self.is_ipv6 = is_ipv6
    def export(self, outfile, level, namespace_='NetworkRouteObj:', name_='NetRouteObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='NetRouteObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='NetworkRouteObj:', name_='NetRouteObjectType'):
        super(NetRouteObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='NetRouteObjectType')
        if self.is_publish is not None and 'is_publish' not in already_processed:
            already_processed.append('is_publish')
            outfile.write(' is_publish="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.is_publish)), input_name='is_publish'))
        if self.is_autoconfigure_address is not None and 'is_autoconfigure_address' not in already_processed:
            already_processed.append('is_autoconfigure_address')
            outfile.write(' is_autoconfigure_address="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.is_autoconfigure_address)), input_name='is_autoconfigure_address'))
        if self.is_loopback is not None and 'is_loopback' not in already_processed:
            already_processed.append('is_loopback')
            outfile.write(' is_loopback="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.is_loopback)), input_name='is_loopback'))
        if self.is_immortal is not None and 'is_immortal' not in already_processed:
            already_processed.append('is_immortal')
            outfile.write(' is_immortal="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.is_immortal)), input_name='is_immortal'))
        if self.is_ipv6 is not None and 'is_ipv6' not in already_processed:
            already_processed.append('is_ipv6')
            outfile.write(' is_ipv6="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.is_ipv6)), input_name='is_ipv6'))
    def exportChildren(self, outfile, level, namespace_='NetworkRouteObj:', name_='NetRouteObjectType', fromsubclass_=False, pretty_print=True):
        super(NetRouteObjectType, self).exportChildren(outfile, level, 'NetworkRouteObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(outfile, level, 'NetworkRouteObj:', name_='Description', pretty_print=pretty_print)
        if self.Network_Route_Entries is not None:
            self.Network_Route_Entries.export(outfile, level, 'NetworkRouteObj:', name_='Network_Route_Entries', pretty_print=pretty_print)
        if self.Preferred_Lifetime is not None:
            self.Preferred_Lifetime.export(outfile, level, 'NetworkRouteObj:', name_='Preferred_Lifetime', pretty_print=pretty_print)
        if self.Valid_Lifetime is not None:
            self.Valid_Lifetime.export(outfile, level, 'NetworkRouteObj:', name_='Valid_Lifetime', pretty_print=pretty_print)
        if self.Route_Age is not None:
            self.Route_Age.export(outfile, level, 'NetworkRouteObj:', name_='Route_Age', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Network_Route_Entries is not None or
            self.Preferred_Lifetime is not None or
            self.Valid_Lifetime is not None or
            self.Route_Age is not None or
            super(NetRouteObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='NetRouteObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.is_publish is not None and 'is_publish' not in already_processed:
            already_processed.append('is_publish')
            showIndent(outfile, level)
            outfile.write('is_publish = %s,\n' % (self.is_publish,))
        if self.is_autoconfigure_address is not None and 'is_autoconfigure_address' not in already_processed:
            already_processed.append('is_autoconfigure_address')
            showIndent(outfile, level)
            outfile.write('is_autoconfigure_address = %s,\n' % (self.is_autoconfigure_address,))
        if self.is_loopback is not None and 'is_loopback' not in already_processed:
            already_processed.append('is_loopback')
            showIndent(outfile, level)
            outfile.write('is_loopback = %s,\n' % (self.is_loopback,))
        if self.is_immortal is not None and 'is_immortal' not in already_processed:
            already_processed.append('is_immortal')
            showIndent(outfile, level)
            outfile.write('is_immortal = %s,\n' % (self.is_immortal,))
        if self.is_ipv6 is not None and 'is_ipv6' not in already_processed:
            already_processed.append('is_ipv6')
            showIndent(outfile, level)
            outfile.write('is_ipv6 = %s,\n' % (self.is_ipv6,))
        super(NetRouteObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(NetRouteObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Description is not None:
            showIndent(outfile, level)
            outfile.write('Description=model_.cybox_common_types_1_0.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Network_Route_Entries is not None:
            showIndent(outfile, level)
            outfile.write('Network_Route_Entries=model_.NetworkRouteEntriesType(\n')
            self.Network_Route_Entries.exportLiteral(outfile, level, name_='Network_Route_Entries')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Preferred_Lifetime is not None:
            showIndent(outfile, level)
            outfile.write('Preferred_Lifetime=model_.cybox_common_types_1_0.DurationObjectAttributeType(\n')
            self.Preferred_Lifetime.exportLiteral(outfile, level, name_='Preferred_Lifetime')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Valid_Lifetime is not None:
            showIndent(outfile, level)
            outfile.write('Valid_Lifetime=model_.cybox_common_types_1_0.DurationObjectAttributeType(\n')
            self.Valid_Lifetime.exportLiteral(outfile, level, name_='Valid_Lifetime')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Route_Age is not None:
            showIndent(outfile, level)
            outfile.write('Route_Age=model_.cybox_common_types_1_0.DurationObjectAttributeType(\n')
            self.Route_Age.exportLiteral(outfile, level, name_='Route_Age')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_publish', node)
        if value is not None and 'is_publish' not in already_processed:
            already_processed.append('is_publish')
            if value in ('true', '1'):
                self.is_publish = True
            elif value in ('false', '0'):
                self.is_publish = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_autoconfigure_address', node)
        if value is not None and 'is_autoconfigure_address' not in already_processed:
            already_processed.append('is_autoconfigure_address')
            if value in ('true', '1'):
                self.is_autoconfigure_address = True
            elif value in ('false', '0'):
                self.is_autoconfigure_address = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_loopback', node)
        if value is not None and 'is_loopback' not in already_processed:
            already_processed.append('is_loopback')
            if value in ('true', '1'):
                self.is_loopback = True
            elif value in ('false', '0'):
                self.is_loopback = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_immortal', node)
        if value is not None and 'is_immortal' not in already_processed:
            already_processed.append('is_immortal')
            if value in ('true', '1'):
                self.is_immortal = True
            elif value in ('false', '0'):
                self.is_immortal = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_ipv6', node)
        if value is not None and 'is_ipv6' not in already_processed:
            already_processed.append('is_ipv6')
            if value in ('true', '1'):
                self.is_ipv6 = True
            elif value in ('false', '0'):
                self.is_ipv6 = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(NetRouteObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common_types_1_0.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Network_Route_Entries':
            obj_ = NetworkRouteEntriesType.factory()
            obj_.build(child_)
            self.set_Network_Route_Entries(obj_)
        elif nodeName_ == 'Preferred_Lifetime':
            obj_ = cybox_common_types_1_0.DurationObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Preferred_Lifetime(obj_)
        elif nodeName_ == 'Valid_Lifetime':
            obj_ = cybox_common_types_1_0.DurationObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Valid_Lifetime(obj_)
        elif nodeName_ == 'Route_Age':
            obj_ = cybox_common_types_1_0.DurationObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Route_Age(obj_)
        super(NetRouteObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class NetRouteObjectType

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print(USAGE_TEXT)
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Network_Route_Object'
        rootClass = NetRouteObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Network_Route_Object'
        rootClass = NetRouteObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Network_Route_Object",
        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Network_Route_Object'
        rootClass = NetRouteObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from temp import *\n\n')
    sys.stdout.write('import temp as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "NetRouteObjectType",
    "NetworkRouteEntriesType"
    ]