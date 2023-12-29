# Instruções Docker Solr
docker run -d -p 8983:8983 --name solr_instance -t solr

Cria o core arquivo_core para receber os dados do arquivo excel

    docker exec -it solr_instance solr create_core -c arquivo_core

# Instruções Docker aplicação
Necessário buildar o DockerFile para que ele possa baixar os pacotes e gerar a imagem.

    docker build -t desafio_ubc ./app/

Rodar o container com acesso ao container do Solr

    docker run -d --network=host -p 8000:8000 desafio_ubc


# A aplicação foi feita e FastApi, existem dois endpoints principais que servirão para manipular o processo.

  -> EndPoint para subir um arquivo .csv, que será tratado e enviado para o core arquivo_core do Solr

    curl -X 'POST' \
      'http://localhost:8000/processar_arquivo/add-arquivo' \
      -H 'accept: application/json' \
      -H 'Content-Type: multipart/form-data' \
      -F 'arquivo=@aluno.csv;type=text/csv'

-> EndPoint para extrir os dados de log do processo principais, logs totais estão no arquivo app/logs/todos_logs.log 

      curl -X 'GET' \
      'http://localhost:8000/logs/extrair-logs' \
      -H 'accept: application/json'
