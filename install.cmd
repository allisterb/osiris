@echo off
python -m ensurepip

pip install wheel
pip install ext\gdeltPyR
pip install ext\graphistry
pip install -r osiris\requirements.txt