# Desafio SAE Digital - Controle de estoque

Esta aplicação foi feita para o desafio de Django da SAE digital. O seu conceito é propor uma sistema de controle de estoque onde é possível controlar a compra de produtos e seus preços médios. Esta aplicação é um desafio proposto pela empresa então não contem todas as funcinalidas de um sistema de estoque.

A aplicação conta com as seguintes funções:

- Listagem de produtos;
- Adição de novos produtos;
- Adição de nova compra;
- Listagem de compras.
- Calculo de média de preço;

A aplicação faz o cálculo de preço de forma assincrona através do uso da biblioteca celery. Como o calculo de média de preço não tem um alto custo computacional foi adicionado um delay de 60 segundos na task para que seja possível observar a sua execução na listagem de tasks.

## Instalação
Para instalar essa aplicação, são necessárias duas dependências:
 - Docker
 - Docker compose

### Instação do docker e do docker compose
Para instalar estas dependências é recomendade utilizar o guia disponibilizado na docuemtanção das ferramentas
 - Docker https://docs.docker.com/engine/installation/ 
 - Docker compose https://docs.docker.com/compose/install/

## Executando a aplicação
