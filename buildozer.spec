[app]
title = LibraryScanner
package.name = libraryscanner
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,plyer,openssl
orientation = portrait
fullscreen = 1

android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.extra_manifest_application_attrs = android:usesCleartextTraffic="true"

# Добавьте эту строку для актуальных рецептов p4a
p4a.branch = develop

android.release_artifact = apk
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
