# Demonstration of namespaced package pattern using Poetry

Install the package (creates a .venv dir) and run pytest:

```bash
poetry install
poetry run pytest
```

This demonstrates that the package is configured correctly to run tests.  However, running "Python: Run all tests" in VS Code:

- Works fine for Python extension up to v2020.9.114305
- Fails for newer versions:
    ```
    python /home/me/.vscode/extensions/ms-python.python-2020.11.358366026/pythonFiles/testing_tools/run_adapter.py discover pytest -- --rootdir /home/me/vscode-python-14570 -s --cache-clear
    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
    rootdir: /home/me/vscode-python-14570
    collected 0 items / 1 error

    ==================================== ERRORS ====================================
    ____________________ ERROR collecting tests/test_scripts.py ____________________
    ImportError while importing test module '/home/me/vscode-python-14570/tests/test_scripts.py'.
    Hint: make sure your test modules/packages have valid Python names.
    Traceback:
    /usr/lib/python3.8/importlib/__init__.py:127: in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
    tests/test_scripts.py:4: in <module>
        from my_namespace.scripts.foo import foobar
    E   ModuleNotFoundError: No module named 'my_namespace'
    -------------- generated xml file: /tmp/tmp-18265EPSI6IOeKeHX.xml --------------
    =========================== short test summary info ============================
    ERROR tests/test_scripts.py
    !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
    =============================== 1 error in 0.05s ===============================
    ```