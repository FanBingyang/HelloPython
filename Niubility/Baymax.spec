# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Baymax.py'],
             pathex=['G:\\CodeSpace\\HelloPaChong\\Niubility'],
             binaries=[],
             datas=[('source/bye_0.mp3','.'),('source/error_0.mp3','.'),('source/sleep_0.mp3','.'),('source/welcome_0.mp3','.'),
             ('source/bye_1.mp3','.'),('source/error_1.mp3','.'),('source/sleep_1.mp3','.'),('source/welcome_1.mp3','.'),
             ('source/bye_3.mp3','.'),('source/error_3.mp3','.'),('source/sleep_3.mp3','.'),('source/welcome_3.mp3','.'),
             ('source/bye_4.mp3','.'),('source/error_4.mp3','.'),('source/sleep_4.mp3','.'),('source/welcome_4.mp3','.'),
             ('source/appPath_List.txt','.'),('source/temp.wav','.'),('source/temp.mp3','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Baymax',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)
