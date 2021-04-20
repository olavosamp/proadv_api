# proadv_api
Projeto de avaliação cujo objetivo é gerenciar publicações de diários oficiais e classificá-las com base na utilização de expressões regulares.

## Configuração
### Requisitos
Docker, Docker-compose

### Instalação
1. Clone ou baixe o repositório ``git clone https://github.com/olavosamp/proadv_api.git``
2. Copie o arquivo de configuração de ambiente ``project.env`` para a pasta [proadv/](https://github.com/olavosamp/proadv_api/tree/main/proadv) (onde está o Dockerfile)
3. Construa o container do Docker executando o comando ``docker up --build`` na pasta [proadv/](https://github.com/olavosamp/proadv_api/tree/main/proadv)
4. Pronto! Interaja com a aplicação via API ou executando comandos do Django via terminal.
    
    a. (Em um novo terminal), execute comandos para o servidor Django ``docker exec django python manage.py <commando>``
    
    b. Acesse http://localhost:8000/ para utilizar a API navegável.

## Comandos do servidor
Os comandos podem ser invocados executando ``python manage.py <commando> <argumentos>`` dentro do container do Docker.
Comandos disponíveis:
- _load_publications_ <caminho_arquivo>:

    Carrega publicações para o banco de dados a partir de um arquivo JSON. O argumento <caminho_arquivo> é o caminho do arquivo JSON no container do Docker.

- _load_search_terms_ <caminho_arquivo>:

    Carrega termos de busca para o banco de dados a partir de um arquivo JSON. O argumento <caminho_arquivo> é o caminho do arquivo JSON no container do Docker.

- _search_in_publications_:

    Realiza uma busca de todos os termos de pesquisa sobre todas as publicações no banco de dados. Caso um termo seja encontrado em uma publicação, um relacionamento é criado no banco.



## API
O projeto suporta interação via uma API REST para os objetos Publicação e Termo de Busca. É possível interagir com a aplicação através de requisições HTTP ou da API navegável em http://localhost:8000/. Os nomes das tabelas disponíveis são *publications* (Publicações) e *searchterms* (Termos de Busca). Os métodos disponíveis são: 

- CREATE:
    
    Criar nova entrada na tabela '<objeto>':
    ``curl -d "<campo1>=<valor1>&<campo2>=<valor2>&..." -X POST -H "Accept: application/json; indent=4" http://localhost:8000/<objeto>/``


- GET:

    Obter lista de elementos da tabela 'objeto':
    ``curl -H 'Accept: application/json; indent=4' http://localhost:8000/<objeto>/``
    
    Obter elementos da tabela 'objeto' com id 'id_objeto':
    ``curl -H 'Accept: application/json; indent=4' http://localhost:8000/<objeto>/<id_objeto>/``

- PUT:
    
    Atualizar elemento da tabela 'objeto' com id 'id_objeto':
    ``curl -d "<campo1>=<valor1>&<campo2>=<valor2>&..." -X PUT -H "Accept: application/json; indent=4" http://localhost:8000/<objeto>/<id_objeto>/``

- DELETE:
    
    Deletar elemento da tabela 'objeto' com id 'id_objeto':
    ``curl -H 'Accept: application/json; indent=4' -X DELETE http://localhost:8000/<objeto>/<id_objeto>/``
    
Exemplos:
 
- Criar nova publicação.

    ``curl -d "data=\"{"Data": "2021-02-01T00:00:00.000000Z", "Conteudo": "Conteudo teste", "Observacao": "Observacao teste", "DiarioCodigo": 999}\"" -X POST -H "Accept: application/json; indent=4" http://localhost:8000/publications/``

- Atualizar publicação de ID 2:

    ``curl -d "data=\"{"Data": "2021-02-01T00:00:00.000000Z", "Conteudo": "Atualizar conteudo", "Observacao": "Atualizar observacao", "DiarioCodigo": 111}\"" -X PUT -H "Accept: application/json; indent=4" http://localhost:8000/publications/2/``
