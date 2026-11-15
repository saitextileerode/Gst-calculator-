#!/usr/bin/env python3
"""Run after `npx cap add android`. Applies the app's look: dark bars, dark splash,
portrait lock and a custom launcher icon. Usage: python3 scripts/patch_android.py"""
import pathlib, re, sys

root = pathlib.Path("android/app/src/main")
if not root.exists():
    sys.exit("android/ folder not found - run `npx cap add android` first")
res = root / "res"

# 1) colors
(res / "values" / "gst_colors.xml").write_text(
    '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n'
    '    <color name="gst_bg">#0A1311</color>\n'
    '</resources>\n', encoding="utf-8")

# 2) theme: dark status bar + navigation bar, dark splash background
styles = res / "values" / "styles.xml"
s = styles.read_text(encoding="utf-8")
s = s.replace(
    '<item name="android:background">@null</item>',
    '<item name="android:background">@null</item>\n'
    '        <item name="android:statusBarColor">@color/gst_bg</item>\n'
    '        <item name="android:navigationBarColor">@color/gst_bg</item>\n'
    '        <item name="android:windowLightStatusBar">false</item>\n'
    '        <item name="android:windowBackground">@color/gst_bg</item>', 1)
s = s.replace('<item name="android:background">@drawable/splash</item>',
              '<item name="android:background">@color/gst_bg</item>')
styles.write_text(s, encoding="utf-8")

# 3) portrait only
manifest = root / "AndroidManifest.xml"
m = manifest.read_text(encoding="utf-8")
if "screenOrientation" not in m:
    m = m.replace('android:launchMode="singleTask"',
                  'android:launchMode="singleTask"\n            android:screenOrientation="portrait"', 1)
manifest.write_text(m, encoding="utf-8")

# 4) launcher icon (adaptive): dark background + a % sign
(res / "drawable" / "ic_gst_foreground.xml").write_text(
    '<?xml version="1.0" encoding="utf-8"?>\n'
    '<vector xmlns:android="http://schemas.android.com/apk/res/android"\n'
    '    android:width="108dp" android:height="108dp"\n'
    '    android:viewportWidth="108" android:viewportHeight="108">\n'
    '    <path android:strokeColor="#3CC2A8" android:strokeWidth="5" android:strokeLineCap="round"\n'
    '        android:pathData="M64,36 L44,72"/>\n'
    '    <path android:strokeColor="#3CC2A8" android:strokeWidth="5"\n'
    '        android:pathData="M37,42 a6.5,6.5 0 1,0 13,0 a6.5,6.5 0 1,0 -13,0"/>\n'
    '    <path android:strokeColor="#F0B36A" android:strokeWidth="5"\n'
    '        android:pathData="M57.5,66 a6.5,6.5 0 1,0 13,0 a6.5,6.5 0 1,0 -13,0"/>\n'
    '</vector>\n', encoding="utf-8")
icon = ('<?xml version="1.0" encoding="utf-8"?>\n'
        '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
        '    <background android:drawable="@color/gst_bg"/>\n'
        '    <foreground android:drawable="@drawable/ic_gst_foreground"/>\n'
        '</adaptive-icon>\n')
for name in ("ic_launcher.xml", "ic_launcher_round.xml"):
    (res / "mipmap-anydpi-v26" / name).write_text(icon, encoding="utf-8")

print("Android project patched.")
