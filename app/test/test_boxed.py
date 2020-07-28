# *****************************************************************************
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   See NOTICE file for details.
#
# *****************************************************************************
import sys
import jpype
from . import common
from jpype.types import *


def passThrough(item):
    al = JClass("java.util.ArrayList")()
    al.add(item)
    return al.get(0)


class BoxedTestCase(common.JPypeTestCase):
    __name__ = "BoxedTestCase"

    def setUp(self):
        common.JPypeTestCase.setUp(self)
        self.TestBoxed = JClass('jpype.boxed.Boxed')
        self.Number = JClass('java.lang.Number')
        self.Comparable = JClass('java.lang.Comparable')

    def testShort(self):
        c1 = 12345
        # Check passed from and passed to
        d1 = self.TestBoxed.newShort(c1)
        d2 = JClass('java.lang.Short')(c1)
        self.assertEqual(d1, c1)
        self.assertEqual(d2, c1)
        self.assertEqual(c1, d1)
        self.assertEqual(c1, d2)
        self.assertEqual(d1, d2)
        self.assertEqual(self.TestBoxed.callShort(c1),
                         self.TestBoxed.callShort(d2))
        # Verify ops
        self.assertEqual(d1 + 2, d1 + 2)
        self.assertEqual(d1 * 2, d1 * 2)

    def testInteger(self):
        c1 = 12345
        # Check passed from and passed to
        d1 = self.TestBoxed.newInteger(c1)
        d2 = JClass('java.lang.Integer')(c1)
        self.assertEqual(d1, c1)
        self.assertEqual(d2, c1)
        self.assertEqual(c1, d1)
        self.assertEqual(c1, d2)
        self.assertEqual(d1, d2)
        self.assertEqual(self.TestBoxed.callInteger(c1),
                         self.TestBoxed.callInteger(d2))
        # Verify ops
        self.assertEqual(d1 + 2, d1 + 2)
        self.assertEqual(d1 * 2, d1 * 2)

    def testLong(self):
        c1 = 12345
        # Check passed from and passed to
        d1 = self.TestBoxed.newLong(c1)
        d2 = JClass('java.lang.Long')(c1)
        self.assertEqual(d1, c1)
        self.assertEqual(d2, c1)
        self.assertEqual(c1, d1)
        self.assertEqual(c1, d2)
        self.assertEqual(d1, d2)
        self.assertEqual(self.TestBoxed.callLong(c1),
                         self.TestBoxed.callLong(d2))
        # Verify ops
        self.assertEqual(d1 + 2, d1 + 2)
        self.assertEqual(d1 * 2, d1 * 2)

    def testDoubleFromFloat(self):
        JClass('java.lang.Double')(1.0)

    def testFloatFromInt(self):
        JClass('java.lang.Float')(1)

    def testDoubleFromInt(self):
        JClass('java.lang.Double')(1)

    def testBoxed2(self):
        JClass('java.lang.Short')(JClass('java.lang.Integer')(1))
        JClass('java.lang.Integer')(JClass('java.lang.Integer')(1))
        JClass('java.lang.Long')(JClass('java.lang.Integer')(1))
        JClass('java.lang.Float')(JClass('java.lang.Integer')(1))
        JClass('java.lang.Float')(JClass('java.lang.Long')(1))
        JClass('java.lang.Double')(JClass('java.lang.Integer')(1))
        JClass('java.lang.Double')(JClass('java.lang.Long')(1))
        JClass('java.lang.Double')(JClass('java.lang.Float')(1))

    def testFloat(self):
        c1 = 123124 / 256.0
        # Check passed from and passed to
        d1 = self.TestBoxed.newFloat(c1)
        d2 = JClass('java.lang.Float')(c1)
        self.assertEqual(d1, c1)
        self.assertEqual(d2, c1)
        self.assertEqual(c1, d1)
        self.assertEqual(c1, d2)
        self.assertEqual(d1, d2)
        self.assertEqual(self.TestBoxed.callFloat(c1),
                         self.TestBoxed.callFloat(d2))
        # Verify ops
        self.assertEqual(d1 + 2, d1 + 2)
        self.assertEqual(d1 * 2, d1 * 2)
        self.assertTrue(d2 < c1 + 1)
        self.assertTrue(d2 > c1 - 1)

    def testDouble(self):
        c1 = 123124 / 256.0
        # Check passed from and passed to
        d1 = self.TestBoxed.newDouble(c1)
        d2 = JClass('java.lang.Double')(c1)
        self.assertEqual(d1, c1)
        self.assertEqual(d2, c1)
        self.assertEqual(c1, d1)
        self.assertEqual(c1, d2)
        self.assertEqual(d1, d2)
        self.assertEqual(self.TestBoxed.callDouble(c1),
                         self.TestBoxed.callDouble(d2))
        # Verify ops
        self.assertEqual(d1 + 2, d1 + 2)
        self.assertEqual(d1 * 2, d1 * 2)
        self.assertTrue(d2 < c1 + 1)
        self.assertTrue(d2 > c1 - 1)

    def testShortResolve(self):
        self.assertEqual(self.TestBoxed.whichShort(1), 1)
        self.assertEqual(self.TestBoxed.whichShort(JClass('java.lang.Short')(1)), 2)

    def testIntegerResolve(self):
        self.assertEqual(self.TestBoxed.whichInteger(1), 1)
        self.assertEqual(self.TestBoxed.whichInteger(JClass('java.lang.Integer')(1)), 2)

    def testLongResolve(self):
        self.assertEqual(self.TestBoxed.whichLong(1), 1)
        self.assertEqual(self.TestBoxed.whichLong(JClass('java.lang.Long')(1)), 2)

    def testFloatResolve(self):
        self.assertEqual(self.TestBoxed.whichFloat(1.0), 1)
        self.assertEqual(self.TestBoxed.whichFloat(JClass('java.lang.Float')(1.0)), 2)

    def testDoubleResolve(self):
        self.assertEqual(self.TestBoxed.whichDouble(1.0), 1)
        self.assertEqual(self.TestBoxed.whichDouble(JClass('java.lang.Double')(1.0)), 2)

    def testPrivitiveToBoxed(self):
        JClass('java.lang.Boolean')(JBoolean(0))
        JClass('java.lang.Byte')(JByte(0))
        JClass('java.lang.Short')(JShort(0))
        JClass('java.lang.Integer')(JInt(0))
        JClass('java.lang.Long')(JLong(0))
        JClass('java.lang.Float')(JFloat(0))
        JClass('java.lang.Double')(JDouble(0))

    def testBooleanBad(self):
        # java.lang.Boolean(X) works like bool(X)
        # Explicit is a cast
        Boolean = JClass('java.lang.Boolean')
        self.assertFalse(Boolean(tuple()))
        self.assertFalse(Boolean(list()))
        self.assertFalse(Boolean(dict()))
        self.assertFalse(Boolean(set()))
        self.assertTrue(Boolean(tuple(['a'])))
        self.assertTrue(Boolean(['a']))
        self.assertTrue(Boolean({'a': 1}))
        self.assertTrue(Boolean(set(['a', 'b'])))

        # Implicit does not automatically cast
        fixture = JClass('jpype.common.Fixture')()
        with self.assertRaises(TypeError):
            fixture.callBoxedBoolean(tuple())
        with self.assertRaises(TypeError):
            fixture.callBoxedBoolean(list())
        with self.assertRaises(TypeError):
            fixture.callBoxedBoolean(dict())
        with self.assertRaises(TypeError):
            fixture.callBoxedBoolean(set())

    def testByteBad(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Byte')(tuple())

    def testCharacterBad(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Character')(tuple())

    def testShortBad(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Short')(tuple())

    def testIntegerBad(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Integer')(tuple())

    def testLongBad(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Long')(tuple())

    def testFloatBad(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Float')(tuple())

    def testDoubleBad(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Double')(tuple())

    def testBooleanBad2(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Boolean')(tuple(), tuple())

    def testByteBad2(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Byte')(tuple(), tuple())

    def testCharacterBad2(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Character')(tuple(), tuple())

    def testShortBad2(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Short')(tuple(), tuple())

    def testIntegerBad2(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Integer')(tuple(), tuple())

    def testLongBad2(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Long')(tuple(), tuple())

    def testFloatBad2(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Float')(tuple(), tuple())

    def testDoubleBad2(self):
        with self.assertRaises(TypeError):
            JClass('java.lang.Double')(tuple(), tuple())

    def compareTest(self, u, v):
        self.assertEqual(u, v)
        self.assertNotEqual(u, v - 1)
        self.assertTrue(u > v - 1)
        self.assertFalse(u > v + 1)
        self.assertTrue(u >= v)
        self.assertTrue(u <= v)
        self.assertFalse(u < v)
        self.assertFalse(u > v)
        self.assertTrue(u < v + 1)
        self.assertTrue(u > v - 1)

    def testByteBoxOps(self):
        u = JObject(81, JByte)
        self.assertIsInstance(u, JClass('java.lang.Byte'))
        self.compareTest(u, 81)

    def testCharBoxOps(self):
        u = JObject('Q', JChar)
        self.assertIsInstance(u, JClass('java.lang.Character'))
        self.compareTest(u, 81)

    def testShortBoxOps(self):
        u = JObject(81, JShort)
        self.assertIsInstance(u, JClass('java.lang.Short'))
        self.compareTest(u, 81)

    def testIntBoxOps(self):
        u = JObject(81, JInt)
        self.assertIsInstance(u, JClass('java.lang.Integer'))
        self.compareTest(u, 81)

    def testLongBoxOps(self):
        u = JObject(81, JLong)
        self.assertIsInstance(u, JClass('java.lang.Long'))
        self.compareTest(u, 81)

    def testIntBoxOps(self):
        u = JObject(81, JFloat)
        self.assertIsInstance(u, JClass('java.lang.Float'))
        self.compareTest(u, 81)

    def testLongBoxOps(self):
        u = JObject(81, JDouble)
        self.assertIsInstance(u, JClass('java.lang.Double'))
        self.compareTest(u, 81)

    def testCharBox(self):
        u = passThrough(JChar('Q'))
        self.assertIsInstance(u, JClass('java.lang.Character'))
        self.assertEqual(u, JClass('java.lang.Character')('Q'))

    def testBooleanBox(self):
        u = passThrough(JBoolean(True))
        self.assertIsInstance(u, JClass('java.lang.Boolean'))
        self.assertEqual(u, JClass('java.lang.Boolean')(True))
        self.assertEqual(u, True)
        u = passThrough(JBoolean(False))
        self.assertIsInstance(u, JClass('java.lang.Boolean'))
        self.assertEqual(u, JClass('java.lang.Boolean')(False))
        self.assertEqual(u, False)

    def testByteBox(self):
        u = passThrough(JByte(5))
        self.assertIsInstance(u, JClass('java.lang.Byte'))
        self.assertEqual(u, JClass('java.lang.Byte')(5))

    def testShortBox(self):
        u = passThrough(JShort(5))
        self.assertIsInstance(u, JClass('java.lang.Short'))
        self.assertEqual(u, JClass('java.lang.Short')(5))

    def testIntBox(self):
        u = passThrough(JInt(5))
        self.assertIsInstance(u, JClass('java.lang.Integer'))
        self.assertEqual(u, JClass('java.lang.Integer')(5))

    def testLongBox(self):
        u = passThrough(JLong(5))
        self.assertIsInstance(u, JClass('java.lang.Long'))
        self.assertEqual(u, JClass('java.lang.Long')(5))

    def testFloatBox(self):
        u = passThrough(JFloat(5))
        self.assertIsInstance(u, JClass('java.lang.Float'))
        self.assertEqual(u, JClass('java.lang.Float')(5))

    def testDoubleBox(self):
        u = passThrough(JDouble(5))
        self.assertIsInstance(u, JClass('java.lang.Double'))
        self.assertEqual(u, JClass('java.lang.Double')(5))

    def testBooleanNull(self):
        n = JObject(None, JBoolean)
        self.assertIsInstance(n, JClass('java.lang.Boolean'))
        self.assertEqual(n, None)
        self.assertNotEqual(n, True)
        self.assertNotEqual(n, False)
        with self.assertRaises(TypeError):
            int(n)
        with self.assertRaises(TypeError):
            float(n)
        self.assertEqual(str(n), str(None))
        self.assertEqual(repr(n), str(None))
        self.assertEqual(hash(n), hash(None))
        u = passThrough(n)
        self.assertEqual(u, None)

    def testCharNull(self):
        n = JObject(None, JChar)
        self.assertIsInstance(n, JClass('java.lang.Character'))
        self.assertNotEqual(n, 0)
        with self.assertRaises(TypeError):
            int(n)
        with self.assertRaises(TypeError):
            float(n)
        self.assertEqual(str(n), str(None))
        self.assertEqual(repr(n), str(None))
        self.assertEqual(hash(n), hash(None))
        u = passThrough(n)
        self.assertEqual(u, None)

    def testByteNull(self):
        n = JObject(None, JByte)
        self.assertIsInstance(n, JClass('java.lang.Byte'))
        self.assertNotEqual(n, 0)
        with self.assertRaises(TypeError):
            int(n)
        with self.assertRaises(TypeError):
            float(n)
        self.assertEqual(str(n), str(None))
        self.assertEqual(repr(n), str(None))
        self.assertEqual(hash(n), hash(None))
        u = passThrough(n)
        self.assertEqual(u, None)

    def testShortNull(self):
        n = JObject(None, JShort)
        self.assertIsInstance(n, JClass('java.lang.Short'))
        self.assertNotEqual(n, 0)
        with self.assertRaises(TypeError):
            int(n)
        with self.assertRaises(TypeError):
            float(n)
        self.assertEqual(str(n), str(None))
        self.assertEqual(repr(n), str(None))
        self.assertEqual(hash(n), hash(None))
        u = passThrough(n)
        self.assertEqual(u, None)

    def testIntNull(self):
        n = JObject(None, JInt)
        self.assertIsInstance(n, JClass('java.lang.Integer'))
        self.assertNotEqual(n, 0)
        with self.assertRaises(TypeError):
            int(n)
        with self.assertRaises(TypeError):
            float(n)
        self.assertEqual(str(n), str(None))
        self.assertEqual(repr(n), str(None))
        self.assertEqual(hash(n), hash(None))
        u = passThrough(n)
        self.assertEqual(u, None)

    def testLongNull(self):
        n = JObject(None, JLong)
        self.assertIsInstance(n, JClass('java.lang.Long'))
        self.assertNotEqual(n, 0)
        with self.assertRaises(TypeError):
            int(n)
        with self.assertRaises(TypeError):
            float(n)
        self.assertEqual(str(n), str(None))
        self.assertEqual(repr(n), str(None))
        self.assertEqual(hash(n), hash(None))
        u = passThrough(n)
        self.assertEqual(u, None)

    def testFloatNull(self):
        n = JObject(None, JFloat)
        self.assertIsInstance(n, JClass('java.lang.Float'))
        self.assertNotEqual(n, 0)
        self.assertNotEqual(n, 0.0)
        with self.assertRaises(TypeError):
            int(n)
        with self.assertRaises(TypeError):
            float(n)
        self.assertEqual(str(n), str(None))
        self.assertEqual(repr(n), str(None))
        self.assertEqual(hash(n), hash(None))
        u = passThrough(n)
        self.assertEqual(u, None)

    def testDoubleNull(self):
        n = JObject(None, JDouble)
        self.assertIsInstance(n, JClass('java.lang.Double'))
        self.assertNotEqual(n, 0)
        self.assertNotEqual(n, 0.0)
        with self.assertRaises(TypeError):
            int(n)
        with self.assertRaises(TypeError):
            float(n)
        self.assertEqual(str(n), str(None))
        self.assertEqual(repr(n), str(None))
        self.assertEqual(hash(n), hash(None))
        u = passThrough(n)
        self.assertEqual(u, None)

    def testAsNumber(self):
        Number = JClass('java.lang.Number')
        self.assertIsInstance(JClass('java.lang.Byte')(1), Number)
        self.assertIsInstance(JClass('java.lang.Short')(1), Number)
        self.assertIsInstance(JClass('java.lang.Integer')(1), Number)
        self.assertIsInstance(JClass('java.lang.Long')(1), Number)
        self.assertIsInstance(JClass('java.lang.Float')(1), Number)
        self.assertIsInstance(JClass('java.lang.Double')(1), Number)
