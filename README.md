# Python-Compilation-Test
Testing different Python compilers

## Compilers
### Nuitka
```
$ nuitka --no-pyi-file --onefile --remove-output --standalone main.py
```
### PyInstaller
```
$ pyinstaller -F --clean -o PyInstaller main.py
```
## Stats
| Compiler           | Time          |
| ------------------ | ------------- |
| Nuitka             | ≈ 3.3 seconds |
| PyInstaller        | ≈ 3.7 seconds |
| Python Interpreter | ≈ 3.7 seconds |
