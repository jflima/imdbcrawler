# imdbcrawler
A crawler to obtain, process and display data about movies and artists from IMDb.

-- Under development

# Como executar
## Obtenção dos arquivos 
É necessário obter os arquivos antes de tudo. Para tanto, executar o arquivo crawler/crawler.py. Os arquivos serão clonados no diretório raiz.

## Execução do servidor
O servidor exibe em uma página HTML o conteúdo do arquivo movies.json.

Para executar, entrar na pasta moviedata e rodar os  seguintes comandos.

```
export FLASK_APP=moviedata
export FLASK_ENV=development
flask run
```
