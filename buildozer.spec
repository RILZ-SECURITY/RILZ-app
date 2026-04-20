[app]
title = Rilz Security
package.name = rilzapp
package.domain = org.rilz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Cuma butuh python3 dan kivy versi stabil
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.accept_sdk_license = True
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
