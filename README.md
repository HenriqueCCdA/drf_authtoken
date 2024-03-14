# drf_authtoken

[![Backend](https://github.com/HenriqueCCdA/drf_authtoken/actions/workflows/CI.yml/badge.svg)](https://github.com/HenriqueCCdA/drf_authtoken/actions/workflows/CI.yml)

Projeto com a base com o AuthToken do DRF.

## Subindo o banco de dados

Para o banco de dados foi usado a imagem `postgres:16.1-alpine`.

Subindo o banco de dados com `taskipy`:

```bash
task up_db
```

Ou pode-se subir direto com o `docker compose`:

```bash
docker compose -f docker-compose-dev.yml up database -d
```

## Desenvolvimento local

Para instalar as dependencias:

```bash
poetry install --no-root
```

Rodando os testes:

```bash
pytest
```

Foi usado o pacote `pytest-randomly` então a ordem dos teste é aleatoria. Para rodar os teste sempre na mesma ordem:

```bash
pytest -p no:randomly
```

Formatar o código com `black` e `ruff`:

```bash
task fmt
```

Para usar o `ruff` como linter:

```bash
task linter
```

Para subir o servidor local com `gunicorn`

```bash
task server_prod
```

## Desenvolvimento com Docker

Caso você queria é possivel desenvolver interiamente `conteiners`. Para subir os `conteiners` da aplicação e banco de dados:

```bash
docker compose -f docker-compose-dev.yml up -d
```

Para rodar os testes.

```bash
docker compose -f docker-compose-dev.yml run api pytest
```

Para ver os logs

```bash
docker compose -f docker-compose-dev.yml logs
```

Caso você queria acompanhar o log de um serviço específico:

```bash
docker compose -f docker-compose-dev.yml logs api -f
```

Formatar o código com `black` e `ruff`:

```bash
docker compose -f docker-compose-dev.yml run api task fmt
```

Para usar o `ruff` como linter:

```bash
docker compose -f docker-compose-dev.yml run api task lint
```
