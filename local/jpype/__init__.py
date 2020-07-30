from pythonforandroid.recipe import CppCompiledComponentsPythonRecipe
from pythonforandroid.toolchain import shprint, current_directory, info
from pythonforandroid.patching import will_build
import sh
import os
from os.path import join
import glob


class JPypeRecipe(CppCompiledComponentsPythonRecipe):
    version = '1.0.1'
    url = 'https://github.com/jpype-project/jpype/archive/v{version}.zip'
    name = 'jpype'
    depends = []
    site_packages_name = 'jpype'
    patches = ['patch']

    call_hostpython_via_targetpython = False
    ignore_setup_py = False
    need_stl_shared = True

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

    def install_libraries(self, arch):
        super().install_libraries(arch)

        # Move the jar file to a staging area
        pythonHome = self.ctx.get_python_install_dir()
        jarHome = self.ctx.jar_dir
        print(pythonHome)
        print(jarHome)
        shprint(sh.mv, join(pythonHome, 'org.jpype.jar'), jarHome)

    def get_recipe_env(self, arch=None, with_flags_in_cc=True):
        env = super().get_recipe_env(arch, with_flags_in_cc)
        #env['LDFLAGS'] += ' -L{}'.format(self.ctx.get_libs_dir(arch.arch))
        env['LDFLAGS'] += ' -L{}'.format(join(self.ctx.bootstrap.build_dir, "libs", arch.arch))
        return env

    # avoid the cache for now
    def should_build(self, arch):
        return True

    def postbuild_arch(self, arch):
        super().postbuild_arch(arch)
        info("Copying JPype java class to classes build dir '%s'"%self.ctx.javaclass_dir)
        info("From %s"%self.get_build_dir(arch.arch))
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(sh.cp, '-r', join('build','temp.linux-x86_64-3.8','org.jpype','classes','org'), self.ctx.javaclass_dir)

    def apply_patches(self, arch, build_dir=None):
        super().apply_patches(arch, build_dir)
        build_dir = build_dir if build_dir else self.get_build_dir(arch.arch)

        # Remove modules that do not apply
        shprint(sh.rm, "-f", join(build_dir, "jpype", "pickle.py"))
        shprint(sh.rm, "-f", join(build_dir, "jpype", "beans.py"))
        shprint(sh.rm, "-f", join(build_dir, "jpype", "imports.py"))
        shprint(sh.rm, "-f", join(build_dir, "jpype", "_classpath.py"))
        shprint(sh.rm, "-f", join(build_dir, "jpype", "_gui.py"))
        shprint(sh.rm, "-f", join(build_dir, "native", "java", "org", "jpype","JPypeSignal.java"))
        shprint(sh.rm, '-Rf', join(build_dir, "native", "java", "org", "jpype","html"))
        shprint(sh.rm, '-Rf', join(build_dir, "native", "java", "org", "jpype","javadoc"))
        shprint(sh.rm, '-Rf', join(build_dir, "native", "java", "org", "jpype","classloader"))



    # def postbuild_arch(self, arch):
    #      super().postbuild_arch(arch)
    #      info('Copying pyjnius java class to classes build dir')
    #      with current_directory(self.get_build_dir(arch.arch)):
    #          shprint(sh.cp, '-a', join('jnius', 'src', 'org'), self.ctx.javaclass_dir)


recipe = JPypeRecipe()
