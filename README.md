# tutorialDjangoGirls
https://tutorial.djangogirls.org/ja/  をやる


## docker起動

```bash
# background起動なら[-d]つける
$ docker-compose up
```

```bash
# 起動確認
$ docker ps
```

## docker内に入る

```bash
$ docker-compose exec web bash
```

## 起動

```bash
$ python3 manage.py runserver 0:8000
```

## ログイン画面

`http://localhost:8000/admin`
