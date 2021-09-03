# blue-heron
python package for interacting with AutoDesk Eagle files

this is a pre-release version and the api is subject to change.

## installation


## development

### installation
to install for development:
```
git clone ${REPO_URL} ${PATH_TO_ROOT}
pip install -e ${PATH_TO_ROOT}
```

### tests
```
pytest --pyarg blueheron
```

## packaging

make sure the PyPA's build package is installed
```python3 -m pip install --upgrade build```

run build from the root dir
```python3 -m build```
