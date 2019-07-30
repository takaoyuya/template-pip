template-pip
## how to install 
### make package
```
python setup.py test
```
then. you can find .whl file in ./dest

### install
```
pip install {generated.whl}
```

## update pakage
### install
```
pip install {generated.whl}
```

## Error
invalid command 'bdist_wheel’が＝エラーが発生する場合は
```
pip install wheel
```
を実行してください。
