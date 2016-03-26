pyinstaller --onefile --noconsole SameGame-Clone.py
rmdir build /s /q
del SameGame-Clone.spec
del SameGame-Clone.exe
move dist\SameGame-Clone.exe .
rmdir dist /s /q