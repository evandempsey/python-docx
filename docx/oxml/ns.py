# encoding: utf-8

"""
Namespace-related objects.
"""

from __future__ import absolute_import, print_function, unicode_literals


nsmap = {
    'a':   ('http://schemas.openxmlformats.org/drawingml/2006/main'),
    'c':   ('http://schemas.openxmlformats.org/drawingml/2006/chart'),
    'dgm': ('http://schemas.openxmlformats.org/drawingml/2006/diagram'),
    'pic': ('http://schemas.openxmlformats.org/drawingml/2006/picture'),
    'r':   ('http://schemas.openxmlformats.org/officeDocument/2006/relations'
            'hips'),
    'w':   ('http://schemas.openxmlformats.org/wordprocessingml/2006/main'),
    'wp':  ('http://schemas.openxmlformats.org/drawingml/2006/wordprocessing'
            'Drawing'),
    'xml': ('http://www.w3.org/XML/1998/namespace')
}


class NamespacePrefixedTag(str):
    """
    Value object that knows the semantics of an XML tag having a namespace
    prefix.
    """
    def __new__(cls, nstag, *args):
        return super(NamespacePrefixedTag, cls).__new__(cls, nstag)

    def __init__(self, nstag):
        self._pfx, self._local_part = nstag.split(':')
        self._ns_uri = nsmap[self._pfx]

    @property
    def clark_name(self):
        return '{%s}%s' % (self._ns_uri, self._local_part)

    @property
    def local_part(self):
        """
        Return the local part of the tag as a string. E.g. 'foobar' is
        returned for tag 'f:foobar'.
        """
        return self._local_part

    @property
    def nsmap(self):
        """
        Return a dict having a single member, mapping the namespace prefix of
        this tag to it's namespace name (e.g. {'f': 'http://foo/bar'}). This
        is handy for passing to xpath calls and other uses.
        """
        return {self._pfx: self._ns_uri}

    @property
    def nspfx(self):
        """
        Return the string namespace prefix for the tag, e.g. 'f' is returned
        for tag 'f:foobar'.
        """
        return self._pfx

    @property
    def nsuri(self):
        """
        Return the namespace URI for the tag, e.g. 'http://foo/bar' would be
        returned for tag 'f:foobar' if the 'f' prefix maps to
        'http://foo/bar' in nsmap.
        """
        return self._ns_uri