# -*- mode: python ; coding: utf-8 -*-

# ========= CONFIG À ADAPTER (Linux, Arch x86_64) =========
APP_NAME = "arrera-copilote"            # Nom du dossier/binaire final
ENTRY_SCRIPT = "main.py"         # Script d'entrée (if __name__ == "__main__")
ICON_FILE =  icon.png                # Exemple: "assets/icon.png" ou ".ico" (optionnel)
UPX_ENABLED = True               # Désactive si UPX indisponible
DEBUG_BUILD = False              # True pour debug
HIDDENIMPORTS = []               # Ajoute ici des imports dynamiques si nécessaire
EXCLUDES = []                    # Modules à exclure si besoin
# ========= FIN CONFIG =========

import os
block_cipher = None

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

# Patron one-folder: exclude_binaries=True dans EXE, puis COLLECT(...)
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
    console=False,                # appli graphique, pas de terminal
    disable_windowed_traceback=False,
    icon=ICON_FILE,               # .png ou .ico (selon ton DE)
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
