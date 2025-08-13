# -*- mode: python ; coding: utf-8 -*-

# ========= CONFIG À ADAPTER (Windows) =========
APP_NAME = "arrera-copilote"            # Nom du binaire (PyInstaller ajoutera .exe)
ENTRY_SCRIPT = "main.py"         # Script d'entrée (if __name__ == "__main__")
ICON_FILE = "icon.ico"            # Exemple: r"assets\icon.ico" (doit être .ico sous Windows)
UPX_ENABLED = True               # Désactive si UPX n'est pas installé sur la machine
DEBUG_BUILD = False              # True pour debug
HIDDENIMPORTS = []               # Ajoute ici des imports dynamiques si nécessaire
EXCLUDES = []                    # Modules à exclure si besoin
# ========= FIN CONFIG =========

import os, sys
block_cipher = None

# Sécurité: ce .spec ne doit être utilisé que sous Windows
if not sys.platform.startswith("win"):
    raise SystemExit("Ce fichier .spec est prévu uniquement pour Windows.")

PROJECT_ROOT = os.path.abspath(".")

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=[],
    datas=[],                     # Pas de fichiers supplémentaires intégrés
    hiddenimports=HIDDENIMPORTS,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=EXCLUDES,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Patron one-folder (onedir): EXE avec exclude_binaries=True, puis COLLECT
exe = EXE(
    pyz,
    a.scripts,
    [],                           # NE PAS passer a.binaries/zipfiles/datas ici
    exclude_binaries=True,
    name=APP_NAME,
    debug=DEBUG_BUILD,
    bootloader_ignore_signals=False,
    strip=False,
    upx=UPX_ENABLED,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,                # appli GUI: pas de fenêtre console
    disable_windowed_traceback=False,
    icon=ICON_FILE,               # .ico uniquement sous Windows
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=UPX_ENABLED,
    upx_exclude=[],
    name=APP_NAME,
)