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
import jpype
from jpype.types import *
from . import common
import sys


class HashTestCase(common.JPypeTestCase):

    def setUp(self):
        common.JPypeTestCase.setUp(self)

    def testHashString(self):
        self.assertIsNotNone(hash(JClass('java.lang.String')("upside down")))
        self.assertIsNotNone(hash(JString("upside down")))
        self.assertEqual(hash(JString("upside down")),
                         hash("upside down"))

    def testHashArray(self):
        self.assertIsNotNone(hash(JArray(jpype.JInt)([1, 2, 3])))

    def testHashObject(self):
        self.assertIsNotNone(hash(JClass('java.lang.Object')()))

    def testHashBoolean(self):
        self.assertIsNotNone(hash(JClass('java.lang.Boolean')(True)))
        self.assertEqual(hash(JClass('java.lang.Boolean')(True)), hash(True))

    def testHashByte(self):
        self.assertIsNotNone(hash(JClass('java.lang.Byte')(5)))
        self.assertEqual(hash(JClass('java.lang.Byte')(5)), hash(5))

    def testHashChar(self):
        self.assertIsNotNone(hash(JClass('java.lang.Character')("a")))
        # Differences in implementation yield different hashes currently.
        #self.assertEqual(hash(JClass('java.lang.Character')("a")), hash("a"))

    def testHashShort(self):
        self.assertIsNotNone(hash(JClass('java.lang.Short')(1)))
        self.assertEqual(hash(JClass('java.lang.Short')(1)), hash(1))

    def testHashLong(self):
        self.assertIsNotNone(hash(JClass('java.lang.Long')(55)))
        self.assertEqual(hash(JClass('java.lang.Long')(55)), hash(55))

    def testHashInteger(self):
        self.assertIsNotNone(hash(JClass('java.lang.Integer')(123)))
        self.assertEqual(hash(JClass('java.lang.Integer')(123)), hash(123))

    def testHashFloat(self):
        self.assertIsNotNone(hash(JClass('java.lang.Float')(3.141592)))

    def testHashDouble(self):
        self.assertIsNotNone(hash(JClass('java.lang.Double')(6.62607004e-34)))

    def testHashNone(self):
        self.assertEqual(hash(None), hash(JObject(None)))
        q = jpype.JObject(None, JClass('java.lang.Double'))
        self.assertEqual(hash(None), hash(JObject(None)))
