# Chessapi

Escrito com Python3/Django e utiliza API Graphql.

Link de demonstração hospedado no Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://chessapi-bravi.herokuapp.com/)

## Operações

Modificar o tabuleiro
```graphql
mutation{
  boardUpdate(
    cols: 8
    rows:8
  ){
    board{
      id
      cols
      rows
    }
  }
}
```

Criar nova peça
```graphql
mutation{
  pieceCreate(
    color: WHITE
    pieceType: KNIGHT
  ){
    piece{
      id
      color
      pieceType
    }
  }
}
```

Obter lista de movimentos
```graphql
query{
  movements(
    id: 1
    position: "d4"
  )
}
```
