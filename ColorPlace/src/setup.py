# setup.py
from distutils.core import setup
from Cython.Build import cythonize

# Example:
# 
setup(
    ext_modules=cythonize(
        "*.pyx", compiler_directives={"language_level": "3"}
    )
)