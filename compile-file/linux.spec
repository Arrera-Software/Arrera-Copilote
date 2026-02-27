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
HIDDENIMPORTS = []
EXCLUDES = []
# ========= FIN CONFIG =========

block_cipher = None
PROJECT_ROOT = os.path.abspath(".")

# --- Récupération de llama_cpp ---
tmp_ret = collect_all('llama_cpp')
llama_datas = tmp_ret[0]
llama_binaries = tmp_ret[1]
llama_hiddenimports = tmp_ret[2]

final_hiddenimports = HIDDENIMPORTS + llama_hiddenimports

# --- Ajout des dossiers asset, config, keyword, language ---
extra_datas = []
for folder in ['asset', 'config', 'keyword', 'language']:
    source_path = os.path.join(PROJECT_ROOT, folder)
    if os.path.exists(source_path):
        extra_datas.append((source_path, folder))

final_datas = llama_datas + extra_datas

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=llama_binaries,
    datas=final_datas,
    hiddenimports=final_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=EXCLUDES,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# --- MODE ONE-FILE (Fichier unique) ---
# Tout est compacté dans l'EXE. Il n'y a plus de section COLLECT.
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,   # <-- AJOUTÉ ICI
    a.zipfiles,   # <-- AJOUTÉ ICI
    a.datas,      # <-- AJOUTÉ ICI
    [],
    name=APP_NAME,
    debug=DEBUG_BUILD,
    bootloader_ignore_signals=False,
    # IMPORTANT : Strip désactivé pour compatibilité Linux (Red Hat/Fedora)
    strip=False,
    upx=UPX_ENABLED,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_FILE,
)