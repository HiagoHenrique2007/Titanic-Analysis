# Titanic Analysis


## Antes de tudo

Darei instruções de como popular seu banco de dados e instalar as dependencias.

**Primerio vamos installar as dependencias:**

recomendo criar um ambiente virtual, rode esse comando para cria-lo:
``` shell
python -m venv .env
./env/Scripts/activate
```
execulte esses comandos no seu terminal no diretorio root do projeto:

``` shell
python -m pip install --upgrade pip
python -m pip install -r packages.txt
```

**Agora vamos pupular seu banco de dados:**

Rode o arquivo commands.sql da pasta sql no seu mysql e depois rode o arquivo popular.py tambem da pasta sqle atenção, rode o popular.py no diretorio sql, senão ele não vai achar o datas.csv
