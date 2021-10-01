"""
This type stub file was generated by pyright.
"""

import os
import sys

extra_dll_dir = os.path.join(os.path.dirname(__file__), '.libs')
if sys.platform == 'win32' and os.path.isdir(extra_dll_dir):
    ...
blas_mkl_info = {  }
blis_info = {  }
openblas_info = { 'libraries': ['openblas', 'openblas'],'library_dirs': ['/usr/local/lib'],'language': 'c','define_macros': [('HAVE_CBLAS', None)] }
blas_opt_info = { 'libraries': ['openblas', 'openblas'],'library_dirs': ['/usr/local/lib'],'language': 'c','define_macros': [('HAVE_CBLAS', None)] }
lapack_mkl_info = {  }
openblas_lapack_info = { 'libraries': ['openblas', 'openblas'],'library_dirs': ['/usr/local/lib'],'language': 'c','define_macros': [('HAVE_CBLAS', None)] }
lapack_opt_info = { 'libraries': ['openblas', 'openblas'],'library_dirs': ['/usr/local/lib'],'language': 'c','define_macros': [('HAVE_CBLAS', None)] }
def get_info(name):
    ...

def show():
    """
    Show libraries in the system on which NumPy was built.

    Print information about various resources (libraries, library
    directories, include directories, etc.) in the system on which
    NumPy was built.

    See Also
    --------
    get_include : Returns the directory containing NumPy C
                  header files.

    Notes
    -----
    Classes specifying the information to be printed are defined
    in the `numpy.distutils.system_info` module.

    Information may include:

    * ``language``: language used to write the libraries (mostly
      C or f77)
    * ``libraries``: names of libraries found in the system
    * ``library_dirs``: directories containing the libraries
    * ``include_dirs``: directories containing library header files
    * ``src_dirs``: directories containing library source files
    * ``define_macros``: preprocessor macros used by
      ``distutils.setup``

    Examples
    --------
    >>> np.show_config()
    blas_opt_info:
        language = c
        define_macros = [('HAVE_CBLAS', None)]
        libraries = ['openblas', 'openblas']
        library_dirs = ['/usr/local/lib']
    """
    ...

