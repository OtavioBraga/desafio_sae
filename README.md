# Desafio SAE Digital - Controle de estoque

Esta aplicação foi feita para o desafio de Django da SAE digital. O seu conceito é propor uma sistema de controle de estoque onde é possível controlar a compra de produtos e seus preços médios. Esta aplicação é um desafio proposto pela empresa então não contém todas as funcinalidas de um sistema de estoque.

A aplicação conta com as seguintes funções:

- Listagem de produtos;
- Adição de novos produtos;
- Adição de nova compra;
- Listagem de compras;
- Cálculo de média de preço.

A aplicação faz o cálculo de preço de forma assincrona através do uso da biblioteca celery. Como o calculo de média de preço não tem um alto custo computacional foi adicionado um delay de 60 segundos na task para que seja possível observar a sua execução na listagem de tasks.

## Instalação
Para instalar essa aplicação, são necessárias duas dependências:
 - Docker
 - Docker compose

### Instalação do docker e do docker compose
Para instalar estas dependências é recomendade utilizar o guia disponibilizado na documentação das ferramentas.
 - Docker https://docs.docker.com/engine/installation/ 
 - Docker compose https://docs.docker.com/compose/install/

## Executando a aplicação

Após ter instalado o docker e o docker compose, clone este repositório e entre dentro da pasta. Observe se você está no nível que possui o arquivo docker-compose yml. Após isso execute o comando ```docker-compose up``` e aguarda até que o docker finalize todos os processos.

Após o docker terminar de criar todos os containers é só acessar http://0.0.0.0:8000 para fazer login na aplicação. Você pode fazer login com o usuário **root** e a senha **root1234**.

