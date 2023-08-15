# セットアップ

```
$ cp .env.template .env
$ docker network create fastapi_vue_env

.envの mysql用の定数を各々で設定

$ docker-compose up -d
```

# .envの編集

```
COMPOSE_PROJECT_NAME=fastapi_vue_env

MYSQL_USER=[各々で記載]
MYSQL_PASSWORD=[各々で記載]
MYSQL_ROOT_PASSWORD=[各々で記載]
MYSQL_HOST=[各々で記載]
MYSQL_DATABASE=[各々で記載]

PYTHONPATH=/usr/src/app/backend
```

# マイグレーション

```
$ docker-compose exec back bash
root@~~~~~:/usr/src/app/scripts# cd /usr/src/app/db
root@~~~~~:/usr/src/app/backend# alembic revision --autogenerate -m 'create_users' # マイグレーションファイル作成
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'users'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_users_id' on '['id']'
  Generating /usr/src/app/db/migrations/versions/ff4d47f6a0af_create_users.py ...  done

root@~~~~~:/usr/src/app/backend# alembic upgrade head # マイグレーション
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> ff4d47f6a0af, create users
```

# seeding
サンプルデータ作成

```sh
$ docker-compose exec back bash
root@~~~~~:/usr/src/app/scripts# cd /usr/src/app/backend
root@~~~~~:/usr/src/app/backend# python seed.py

2022-11-06 14:36:19,271 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
2022-11-06 14:36:19,272 INFO sqlalchemy.engine.base.Engine ()
.
.
2022-11-06 14:36:19,303 INFO sqlalchemy.engine.base.Engine ('アンパンマン',)
2022-11-06 14:36:19,309 INFO sqlalchemy.engine.base.Engine COMMIT
```

# local host

```
http://localhost:8888/docs # Open API
http://localhost:8080
```

# 参考
https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5

https://github.com/testdrivenio/fastapi-vue
