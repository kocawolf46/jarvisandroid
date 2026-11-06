[app]

# (str) Title of your application
title = J.A.R.V.I.S

# (str) Package name
package.name = jarvis

# (str) Package domain (needed for android/ios packaging)
package.domain = org.alikoca

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,config/*,memory/*,actions/*,core/*

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec,pyc,pyo,lnk,bat

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, venv, .venv, .git, .vscode, .claude, __pycache__

# (string) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,google-genai,requests,urllib3,certifi,charset-normalizer,idna,pydantic,typing-extensions

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# Android specific
fullscreen = 0
android.presplash_color = #0f172a

# Permissions
android.permissions = INTERNET,RECORD_AUDIO,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.hardware.camera = True

# Target Android API
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.allow_backup = False
android.format = apk
android.enable_androidx = True

# Architectures
android.archs = arm64-v8a, armeabi-v7a

p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = ./bin