# 🌎 Environment Setup

Once you have Python installed, we need to create a new folder in your filesystem.

But we are going to do it from the command line

=== "Windows"

    Open `PowerShell` again, then enter each line, one by one

=== "MacOS"

    Open `Terminal` again, then enter each line, one by one  


```powershell
mkdir Projects
```

!!! info "mkdir"

    The `mkdir` command **m**akes a **d**irectory (a folder)

```powershell
cd Projects
```

!!! info "mkdir"

    The `cd` command **c**hanges to a **d**irectory

```powershell
mkdir projectname
```

```powershell
cd projectname
```

## Virtual Environment

When you have different projects that depend on the same package, you might have a scenario where
project A needs version 2 of a package, but project B needs version 3 of a package.

To avoid this conflict, it's a good idea to create a **virtual environment**.
You can think of it like a container that isolates the packages from different projects

Create a virtual environement inside your `projectname` directory

=== "Windows"

    ```powershell
    python -m venv .venv
    ```

=== "MacOS"

    ```powershell
    python3 -m venv venv
    ```

!!! info "venv"

    Python comes with a package called `venv` (short for virtual environment), 
    and we are telling this package to create a virtual environment called `venv`

Next activate the environment

=== "Windows"

    ```powershell
    .\venv\Scripts\Activate.ps1
    ```

=== "MacOS"

    ```powershell
    source ./venv/bin/activate
    ```

Besides your prompt you should now see the name of the virtual environment in round brackets

