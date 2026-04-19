[app]
# (panel by rilz)
title = Rilz Security
# (Nama Paket)
package.name = rilzapp
package.domain = org.rilz
# (Folder tempat main.py berada)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# (Bahan-bahan yang dibutuhin)
requirements = python3,kivy

# (Tampilan HP)
orientation = portrait
fullscreen = 0

# (Spek Android)
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.api = 31
android.minapi = 21

# (Izin Tambahan kalau perlu)
# android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
