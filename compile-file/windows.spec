# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
import os, sys

# ========= CONFIG À ADAPTER (Windows) =========
APP_NAME = "Arrera Copilote"
ENTRY_SCRIPT = "main.py"
ICON_FILE = "asset/icone/win/icon.ico"
# CONSEIL : Mettre à False pour éviter les faux positifs antivirus
# et les erreurs de DLL corrompues avec llama_cpp
UPX_ENABLED = False
DEBUG_BUILD = False
HIDDENIMPORTS = []
EXCLUDES = []
# ========= FIN CONFIG =========

block_cipher = None

# Sécurité: ce .spec ne doit être utilisé que sous Windows
if not sys.platform.startswith("win"):
    raise SystemExit("Ce fichier .spec est prévu uniquement pour Windows.")

PROJECT_ROOT = os.path.abspath(".")

# -----------------------------------------------------------
# AJOUT POUR LLAMA CPP
# -----------------------------------------------------------
tmp_ret = collect_all('llama_cpp')
datas_llama, binaries_llama, hiddenimports_llama = tmp_ret

# On fusionne avec vos listes existantes
HIDDENIMPORTS += hiddenimports_llama

# --- Ajout des dossiers asset, config, keyword, language ---
extra_datas = []
for folder in ['asset', 'config', 'keyword', 'language']:
    source_path = os.path.join(PROJECT_ROOT, folder)
    if os.path.exists(source_path):
        extra_datas.append((source_path, folder))

final_datas = datas_llama + extra_datas

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=binaries_llama,
    datas=final_datas,
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

# --- MODE ONE-FILE (Windows) ---
# Tout est dans l'EXE, pas de COLLECT
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,   # <-- AJOUTÉ : Les binaires (DLLs)
    a.zipfiles,   # <-- AJOUTÉ
    a.datas,      # <-- AJOUTÉ : Les assets
    [],
    name=APP_NAME,
    debug=DEBUG_BUILD,
    bootloader_ignore_signals=False,
    strip=False,
    upx=UPX_ENABLED,
    upx_exclude=[],
    runtime_tmpdir=None,
    # Mettre à False pour une appli graphique (GUI) sans fenêtre noire
    # Mettre à True si c'est un outil en ligne de commande
    console=False,
    disable_windowed_traceback=False,
    icon=ICON_FILE,
)