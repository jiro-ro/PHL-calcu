[app]
title = PHL Calculator
package.name = phlcalculator
package.domain = org.civmatics

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.exclude_dirs = .github,bin,.buildozer

version = 1.0.0

requirements = python3==3.11.5,hostpython3==3.11.5,kivy==2.3.0

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png
android.presplash_color = #fde4df

android.permissions =

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
