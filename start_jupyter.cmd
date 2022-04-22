@echo off
if not "%1"=="" (
   jupyter notebook %1
) else (
    echo You must specify the path to your Jupyter notebooks.
)
