# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
import os

# ========= CONFIG =========
APP_NAME = "Arrera Copilote"
ENTRY_SCRIPT = "main.py"
ICON_FILE = "asset/icone/linux/icon.png"
# IMPORTANT : Toujours False pour éviter l'erreur "ELF load command" sur Red Hat/Fedora
UPX_ENABLED = False
DEBUG_BUILD = False
HIDDENIMPORTS = [
    'PIL._tkinter_finder',
    'pyttsx3.drivers',
    'pyttsx3.drivers.espeak', # Driver standard sous Linux
    'pyttsx3.drivers.nsss',   # Au cas où tu compiles sur Mac plus tard
    'pyttsx3.drivers.sapi5',  # Au cas où tu compiles sur Windows
    'gtts',
    'speech_recognition'
]
EXCLUDES = []
# ========= FIN CONFIG =========

block_cipher = None
PROJECT_ROOT = os.path.abspath(".")

# --- Récupération massive des dépendances ---
libs = ['llama_cpp', 'customtkinter', 'pyttsx3', 'speech_recognition', 'playsound3']
combined_datas = []
combined_binaries = []
combined_hidden = []

for lib in libs:
    tmp = collect_all(lib)
    combined_datas += tmp[0]
    combined_binaries += tmp[1]
    combined_hidden += tmp[2]

final_hiddenimports = list(set(HIDDENIMPORTS + combined_hidden))

# --- Ajout des dossiers locaux ---
extra_datas = []
for folder in ['asset', 'config', 'keyword', 'language']:
    source_path = os.path.join(PROJECT_ROOT, folder)
    if os.path.exists(source_path):
        extra_datas.append((source_path, folder))

final_datas = combined_datas + extra_datas

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=combined_binaries,
    datas=final_datas,
    hiddenimports=final_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=EXCLUDES,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=APP_NAME,
    debug=DEBUG_BUILD,
    bootloader_ignore_signals=False,
    strip=False,
    upx=UPX_ENABLED,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False, # LAISSE SUR TRUE POUR VOIR LES ERREURS AUDIO DANS LE TERMINAL
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_FILE,
)