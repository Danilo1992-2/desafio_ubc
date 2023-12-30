# Instruções Docker Solr

Executar um contêiner do Solr para o serviço:

    docker run -d -p 8983:8983 --name solr_instance -t solr
Criar o core "arquivo_core" para receber os dados do arquivo Excel:

    docker exec -it solr_instance solr create_core -c arquivo_core
Instruções Docker para a aplicação
É necessário construir o DockerFile para baixar os pacotes e gerar a imagem:

    docker build -t desafio_ubc ./app/
Executar o contêiner com acesso ao contêiner do Solr:

    docker run -d --network=host -p 8000:8000 desafio_ubc

Sobre a aplicação
A aplicação foi desenvolvida em FastAPI e possui três endpoints principais para manipular o processo.

-> Endpoint para enviar um arquivo .csv, que será processado e enviado para o núcleo "arquivo_core" do Solr:

    curl -X 'POST' \
      'http://localhost:8000/processar_arquivo/add-arquivo' \
      -H 'accept: application/json' \
      -H 'Content-Type: multipart/form-data' \
      -F 'arquivo=@aluno.csv;type=text/csv'
-> Endpoint para extrair os dados de log do processo principal. Todos os logs estão disponíveis no arquivo app/logs/todos_logs.log:

    curl -X 'GET' \
      'http://localhost:8000/logs/extrair-logs' \
      -H 'accept: application/json'
-> Endpoint para verificar métricas do arquivo:

    curl -X 'GET' \
      'http://localhost:8000/metricas/metricas' \
      -H 'accept: application/json'

#Observação
A aplicação é uma api e pode ser consumida via Postman ou através do Swagger pelo link http://localhost:8000/docs
