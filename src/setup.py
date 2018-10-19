from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Build import cythonize
except ImportError:
    def cythonize(*args, **kwargs):
        from Cython.Build import cythonize
        return cythonize(*args, **kwargs)

try:
    from numpy import get_include
except ImportError:
    def get_include(*args, **kwargs):
        from numpy import get_include
        return get_include(*args, **kwargs)


sourcefiles = [
    'sent2vec.pyx',
    'fasttext.cc',
    'args.cc',
    'dictionary.cc',
    'matrix.cc',
    'qmatrix.cc',
    'model.cc',
    'real.cc',
    'utils.cc',
    'vector.cc',
    'real.cc',
    'productquantizer.cc'
]

compile_opts = ['-std=c++0x', '-Wno-cpp', '-pthread', '-Wno-sign-compare']

ext = [
    Extension(
        '*',
        sourcefiles,
        extra_compile_args=compile_opts,
        language='c++',
        include_dirs=[get_include()])
]

setup(
    name='sent2vec',
    ext_modules=cythonize(ext),
    install_requires=[
        'cython',
        'numpy'
    ]
)
