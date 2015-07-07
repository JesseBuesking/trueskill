from distutils.core import setup, Extension

module_def = Extension(
    "trueskill",
    sources=[
        "src/python_wrapper.cpp",
        "src/const.cpp",
        "src/mathexpr.cpp",
        "src/ndtr.cpp",
        "src/ndtri.cpp",
        "src/pdf.cpp",
        "src/trueskill.cpp"],
    language="c++",
    include_dirs=['./src'])

setup(
    name="trueskill",
    version="1.0",
    description="trueskill implementation using c++",
    ext_modules=[module_def])