#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
## 
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

"""Source code text utilities"""

__all__ = ["get_eol_chars", "get_os_name_from_eol_chars",
           "get_eol_chars_from_os_name", "has_mixed_eol_chars",
           "fix_indentation"]

__docformat__ = 'restructuredtext'

# Order is important:
EOL_CHARS = (("\r\n", 'nt'), ("\n", 'posix'), ("\r", 'mac'))

def get_eol_chars(text):
    """Get text EOL characters"""
    for eol_chars, _os_name in EOL_CHARS:
        if text.find(eol_chars) > -1:
            return eol_chars

def get_os_name_from_eol_chars(eol_chars):
    """Return OS name from EOL characters"""
    for chars, os_name in EOL_CHARS:
        if eol_chars == chars:
            return os_name

def get_eol_chars_from_os_name(os_name):
    """Return EOL characters from OS name"""
    for eol_chars, name in EOL_CHARS:
        if name == os_name:
            return eol_chars

def has_mixed_eol_chars(text):
    """Detect if text has mixed EOL characters"""
    eol_chars = get_eol_chars(text)
    if eol_chars is None:
        return False
    correct_text = eol_chars.join((text+eol_chars).splitlines())
    return repr(correct_text) != repr(text)

def fix_indentation(text):
    """Replace tabs by spaces"""
    return text.replace('\t', ' '*4)
    