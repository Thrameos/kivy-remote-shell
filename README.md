Kivy Remote Shell
=================

Remote SSH+Python interactive shell application. Great for having a remote
python shell on an embed platform like android.


Instructions
------------

* start the application
* connect to the ssh `ssh -p8000 admin@serverip`
* enter the password: kivy
* enjoy your python shell


Compile for android
-------------------


```
$ pip install buildozer --user
$ git clone git://github.com/kivy/kivy-remote-shell
$ cd kivy-remote-shell
$ pip install -r requirements.txt
$ buildozer android debug deploy run logcat
```

Pre-built debug apk available at http://bit.ly/KivyRemote2


If you want to compile a release version for sharing, just replace `debug
installd` by `release`, and sign the APK!

Using on AS emulator
--------------------

- Set up an emulator with Android studio.
- Launch the emulator.
- Deploy the application
    buildozer android deploy run logcat >& run.log
- Set up port forwarding (Code is from the file shown)
    $ telnet localhost 5554
    auth <code>
    redir add tcp:8000:8000
    ^C
- Connect to host
    ssh -p 8000 admin@localhost


Running the test cases
----------------------

>>> import unittest
>>> import jpype
>>> import test_array
>>> suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_array.ArrayTestCase)
>>> unittest.TextTestRunner().run(suite)

