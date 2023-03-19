# 📝 Editor Setup


We will use jupyter lab to edit code

Install jupyterlab

=== "Windows"

    ```powershell
    python -m pip install jupyterlab
    ```

=== "MacOS"

    ```powershell
    python3 -m pip install jupyterlab
    ```

Then add the virtual environment to Jupyter

```powershell
ipython kernel install --user --name=venv
```

Then run jupyter lab

```powershell
jupyter lab
```

Your browser will open up to a new page, then click on the tile that says `venv` under the **Notebooks** section

Save the notebook, and rename to `mynotebook.ipynb`

## Test your setup

In the little box with your cursor, type

```python
print("Hello")
```

Then press `shift` and `enter` keys
