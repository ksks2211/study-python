from setuptools import setup, Extension



measurer_mod = Extension('measurer', sources=['measurermodule.c'])
setup(
    name='measurer',
    version='1.1',
    description="A Sample extension Module",
    ext_modules= [measurer_mod]
)