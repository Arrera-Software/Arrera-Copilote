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
HIDDENIMPORTS = [
    'PIL._tkinter_finder', 'pyttsx3.drivers', 'pyttsx3.drivers.sapi5',
    'gtts', 'speech_recognition', 'pyaudio', 'numpy', 'google.protobuf',
    'PIL', 'PIL.Image', 'tkinter', 'sounddevice'
]
EXCLUDES = [
    "tensorflow", "tensorflow_estimator", "tensorboard", "keras", "cv2", "torch"
]
# ========= FIN CONFIG =========

block_cipher = None

# Sécurité: ce .spec ne doit être utilisé que sous Windows
if not sys.platform.startswith("win"):
    raise SystemExit("Ce fichier .spec est prévu uniquement pour Windows.")

PROJECT_ROOT = os.path.abspath(".")

# -----------------------------------------------------------
# COLLECTE DES DÉPENDANCES COMPLEXES
# -----------------------------------------------------------
libs = ['llama_cpp', 'customtkinter', 'pyttsx3', 'speech_recognition', 'playsound3']
combined_datas = []
combined_binaries = []
combined_hidden = []

for lib in libs:
    try:
        tmp = collect_all(lib)
        combined_datas += tmp[0]
        combined_binaries += tmp[1]
        combined_hidden += tmp[2]
    except Exception as e:
        print(f"⚠️ Attention : {lib} n'a pas pu être collecté. ({e})")

final_hiddenimports = list(set(HIDDENIMPORTS + combined_hidden))

# --- Ajout des dossiers locaux ---
extra_datas = []
for folder in ['asset', 'config', 'keyword', 'language', 'json_conf', 'instruction_ia']:
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