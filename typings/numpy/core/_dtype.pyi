"""
This type stub file was generated by pyright.
"""

"""
A place for code to be called from the implementation of np.dtype

String handling is much easier to do correctly in python.
"""
_kind_to_stem = { 'u': 'uint','i': 'int','c': 'complex','f': 'float','b': 'bool','V': 'void','O': 'object','M': 'datetime','m': 'timedelta','S': 'bytes','U': 'str' }
def __str__(dtype) -> str:
    ...

def __repr__(dtype):
    ...

