# Lineas de comando que permite ingresar a comandline de imagen de sqlserver

1. docker exec -it sqlserver bash

2. /opt/mssql-tools18/bin/sqlcmd  -S localhost -U sa -P (ingresapass de .env) -C

# Lineas de comando que permite ingresar a comandline de imagen de fastApi

1. Docker exec -it api bash

# Linea de comando para poder realizar la migracion de modelos a base de datos utilizando alembic (libreria)
1. alembic revision --autogenerate -m "Descripción del cambio"
2. alembic upgrade head


# Comandos que permite levantar servicio de docker, tanto imagen de fastapi y sqlserver
1. Docker compose up -d o Docker compose up