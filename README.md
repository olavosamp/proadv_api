# proadv_api

## API
O projeto suporta interação via uma API REST para os objetos Publicação e Termo de Busca. É possível interagir com a aplicação através de requisições HTTP ou da API navegável em http://localhost:8000/. Os métodos disponíveis são: CREATE, GET, PUT, DELETE. Os nomes dos objetos para uso nas requisições são *publications* (Publicações) e *searchterms* (Termos de Busca).

- CREATE:
    
    Criar novo objeto:
    ``curl -d "<campo1>=<valor1>&<campo2>=<valor2>&..." -X POST -H "Accept: application/json; indent=4" http://localhost:8000/<objeto>/``

    Ex:
    Criar nova publicação com campo 'data' (um campo JSON).
    ``curl -d "data=\"{"Data": "2021-02-01T00:00:00.000000Z", "Conteudo": "Conteudo test", "Observacao": "Observacao test", "DiarioCodigo": 999}\"" -X POST -H "Accept: application/json; indent=4" http://localhost:8000/publications/``


- GET:

    Obter lista de objetos:
    ``curl -H 'Accept: application/json; indent=4' http://localhost:8000/<objeto>/``
    
    Obter objeto específico:
    ``curl -H 'Accept: application/json; indent=4' http://localhost:8000/<objeto>/<id_objeto>/``

- PUT:
    
    Atualizar elemento da tabela <objeto> e id <id_objeto>:
    ``curl -d "<campo1>=<valor1>&<campo2>=<valor2>&..." -X PUT -H "Accept: application/json; indent=4" http://localhost:8000/<objeto>/<id_objeto>/``

- DELETE:
    
    Deletar elemento da tabela <objeto> e id <id_objeto>:
    ``curl -H 'Accept: application/json; indent=4' -X DELETE http://localhost:8000/<objeto>/<id_objeto>/``
