from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

compilation_args = ['-fopenmp', '-O3']

ext_modules = [
    Extension(
        "particle",
        ["particle.pyx"],
        extra_compile_args=compilation_args,
        extra_link_args =compilation_args,
        include_dirs=[numpy.get_include()],
    ),
    Extension(
        "maths",
        ["maths.pyx"],
        extra_compile_args=compilation_args,
        extra_link_args=compilation_args,
        include_dirs=[numpy.get_include()],
    ),
    Extension(
        "emf",
        ["emf.pyx"],
        extra_compile_args=compilation_args,
        extra_link_args =compilation_args,
        include_dirs=[numpy.get_include()],
    ),
    Extension(
        "boris_method",
        ["boris_method.pyx"],
        extra_compile_args=compilation_args,
        extra_link_args =compilation_args,
        include_dirs=[numpy.get_include()],
    ),
    Extension(
        "radiation",
        ["radiation.pyx"],
        extra_compile_args=compilation_args,
        extra_link_args =compilation_args,
        include_dirs=[numpy.get_include()],
    ),
]


setup(
    ext_modules=cythonize(ext_modules)
)