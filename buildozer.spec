[app]
title = LibraryScanner
package.name = libraryscanner
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0,requests,urllib3,certifi,chardet,idna,openssl
orientation = portrait
fullscreen = 1

android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
