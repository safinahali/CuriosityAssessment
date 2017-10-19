# This sets up various variables and commands based on the platform we're on.

##############################################################################
# These are set based on the platform we're on.
windows = False
macintosh = False
linux = False

import os
import platform
import traceback
import shutil

if "ANT_HOME" in os.environ:
    del os.environ["ANT_HOME"]

def set_win32_java_home():

    if "JAVA_HOME" in os.environ:
        return

    import _winreg

    with _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\JavaSoft\Java Development Kit") as jdk: #@UndefinedVariable
        current_version, _type = _winreg.QueryValueEx(jdk, "CurrentVersion") #@UndefinedVariable

        with _winreg.OpenKey(jdk, current_version) as cv: #@UndefinedVariable
            java_home, _type = _winreg.QueryValueEx(cv, "JavaHome") #@UndefinedVariable

        os.environ["JAVA_HOME"] = java_home

def maybe_java_home(s):
    """
    If JAVA_HOME is in the environ, return $JAVA_HOME/bin/s. Otherwise, return
    s.
    """

    if "JAVA_HOME" in os.environ:
        return os.path.join(os.environ["JAVA_HOME"], "bin", s)
    else:
        return s

if platform.win32_ver()[0]:
    windows = True

    try:
        set_win32_java_home()
    except:
        traceback.print_exc()

    android = "android-sdk\\tools\\android.bat"
    ant = "apache-ant\\bin\\ant.bat"
    adb = "android-sdk\\platform-tools\\adb.exe"
    javac = maybe_java_home("javac.exe")
    keytool = maybe_java_home("keytool.exe")

elif platform.mac_ver()[0]:
    macintosh = True
    android = "android-sdk/tools/android"
    ant = "apache-ant/bin/ant"
    adb = "android-sdk/platform-tools/adb"
    javac = maybe_java_home("javac")
    keytool = maybe_java_home("keytool")

    os.environ.setdefault("JAVA_HOME", "/usr")

else:
    linux = True
    android = "android-sdk/tools/android"
    ant = "apache-ant/bin/ant"
    adb = "android-sdk/platform-tools/adb"
    javac = maybe_java_home("javac")
    keytool = maybe_java_home("keytool")

RAPT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sdk_version = "r24.4.1"
ant_version = "1.9.3"
build_version = "23.0.1"
target = "android-22"

def path(path, replace=True, relative=False):
    """
    Turns a relative path into an absolute path relative to the RAPT
    directory.

    `replace`
        If true, replaces apache-ant and android-sdk with versioned paths.
    """

    if replace:
        path = path.replace("android-sdk", "android-sdk-" + sdk_version)
        path = path.replace("apache-ant", "apache-ant-" + ant_version)


    if not relative:
        path = os.path.join(RAPT_PATH, path)

    return path

android = path(android)
ant = path(ant)
adb = path(adb)

# This gets set in the Ren'Py launcher if we're a Ren'Py build.
renpy = False

def rename(src, dst):
    """
    Renames src to dst.
    """

    if os.path.isdir(dst):
        shutil.rmtree(dst)
    elif os.path.exists(dst):
        os.unlink(dst)

    os.rename(src, dst)

