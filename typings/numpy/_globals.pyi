"""
This type stub file was generated by pyright.
"""

"""
Module defining global singleton classes.

This module raises a RuntimeError if an attempt to reload it is made. In that
way the identities of the classes defined here are fixed and will remain so
even if numpy itself is reloaded. In particular, a function like the following
will still work correctly after numpy is reloaded::

    def foo(arg=np._NoValue):
        if arg is np._NoValue:
            ...

That was not the case when the singleton classes were defined in the numpy
``__init__.py`` file. See gh-7844 for a discussion of the reload problem that
motivated this module.

"""
__ALL__ = ['ModuleDeprecationWarning', 'VisibleDeprecationWarning', '_NoValue']
if '_is_loaded' in globals():
    ...
_is_loaded = True
class ModuleDeprecationWarning(DeprecationWarning):
    """Module deprecation warning.

    The nose tester turns ordinary Deprecation warnings into test failures.
    That makes it hard to deprecate whole modules, because they get
    imported by default. So this is a special Deprecation warning that the
    nose tester will let pass without making tests fail.

    """
    ...


class VisibleDeprecationWarning(UserWarning):
    """Visible deprecation warning.

    By default, python will not show deprecation warnings, so this class
    can be used when a very visible warning is helpful, for example because
    the usage is most likely a user bug.

    """
    ...


class _NoValueType:
    """Special keyword value.

    The instance of this class may be used as the default value assigned to a
    deprecated keyword in order to check if it has been given a user defined
    value.
    """
    __instance = ...
    def __new__(cls):
        ...
    
    def __reduce__(self):
        ...
    
    def __repr__(self):
        ...
    


_NoValue = _NoValueType()
