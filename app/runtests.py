import unittest
import jpype
jpype.java =None
import importlib
import glob

## Uncomment to test locally
#jpype.startJVM(classpath='../jars/*')

tests = [i[5:-4] for i in glob.glob('test/test_*')]
suite = unittest.TestSuite()
loader = unittest.TestLoader()
for t in tests:
    m = importlib.import_module('test.%s'%t)
    for p,v in m.__dict__.items():
        if not isinstance(v, type):
            continue
        if not issubclass(v, unittest.TestCase):
            continue
        s = loader.loadTestsFromTestCase(v)
        suite.addTest(s)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
print(len(tests))

