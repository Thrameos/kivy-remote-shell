from pythonforandroid.recipe import CppCompiledComponentsPythonRecipe
from pythonforandroid.toolchain import shprint, current_directory, info
from pythonforandroid.patching import will_build
import sh
from os.path import join


class JPypeRecipe(CppCompiledComponentsPythonRecipe):
    version = '1.0.1'
    url = 'https://github.com/jpype-project/jpype/archive/v{version}.zip'
    name = 'jpype'
    depends = []
    site_packages_name = 'jpype'
    patches = []

    call_hostpython_via_targetpython = False
    ignore_setup_py = False

    def build_compiled_components(self, arch):
         info('Building compiled components in {}'.format(self.name))

         env = self.get_recipe_env(arch)
         hostpython = sh.Command(self.hostpython_location)
         with current_directory(self.get_build_dir(arch.arch)):
              if self.install_in_hostpython:
                   shprint(hostpython, 'setup.py', 'clean', '--all', _env=env)
              shprint(hostpython, 'setup.py', self.build_cmd, '-v', '--android',
                  _env=env, *self.setup_extra_args)
              build_dir = glob.glob('build/lib.*')[0]
              shprint(sh.find, build_dir, '-name', '"*.o"', '-exec',
                  env['STRIP'], '{}', ';', _env=env)

    # def postbuild_arch(self, arch):
    #      super().postbuild_arch(arch)
    #      info('Copying pyjnius java class to classes build dir')
    #      with current_directory(self.get_build_dir(arch.arch)):
    #          shprint(sh.cp, '-a', join('jnius', 'src', 'org'), self.ctx.javaclass_dir)


recipe = JPypeRecipe()
