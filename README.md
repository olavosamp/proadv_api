# proadv_api

## API
O projeto suporta interação via uma API REST para os objetos Publicação e Termo de Busca. É possível interagir com a aplicação através de requisições HTTP ou da API navegável em http://localhost:8000/. Os métodos disponíveis são: CREATE, GET, PUT, DELETE. Os nomes dos objetos para uso nas requisições são *publications* (Publicações) e *searchterms* (Termos de Busca).

- CREATE:

- GET:
    Obter lista de objetos:
    ``curl -H 'Accept: application/json; indent=4' http://localhost:8000/<objeto>/``
    Obter objeto específico:
    ``curl -H 'Accept: application/json; indent=4' http://localhost:8000/<objeto>/<id_objeto>/``

- PUT:

- DELETE:

