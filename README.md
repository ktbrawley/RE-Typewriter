## RE - Type Writer
---
### Instructions
1. Install necessary dependencies referenced in 'requirement.txt'.
    ```
    pip install -r requirements.txt
    ```
1. Run via the following:
    ```
    VSCode: F5
    ```
    ```
    Terminal: python3 typewriter.py
    ```
### Build to .EXE

In VSCode, you can build the python script to a Windows Executable (.exe) using the following command:

```
CTRL + SHIFT + B
```

This will generate a 'build' and dist' folder, respectively. 'Dist' contains the working .exe.

**N.B.** Alternatively, you can extract the command in the .vscode/tasks.json configuration which utilises [**pyinstaller**](https://www.pyinstaller.org/) to build the executable.