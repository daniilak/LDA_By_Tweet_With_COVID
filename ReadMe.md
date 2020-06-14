# Вступительное задание
## Тематическое моделирование на твитах

Обучить‌ ‌модель‌ ‌LDA‌ ‌на‌ ‌20,30,50‌  топиках‌ ‌(поочередно)‌ ‌на‌ ‌твитах.‌

### Зависимости pip
- peewee
- pandas
- nltk

#### файл config.py состоит из 4 констант
```
DB_USER=""
DB_NAME=""
DB_PASS=""
DB_HOST=""
```

### Создание базы для работы со словами

```
CREATE TABLE words (
    id          SERIAL,
    word varchar(255)
);

CREATE TABLE dict_words (
    id          SERIAL,
    word varchar(255),
    count int
);
```

### Фильтрация слов

```
INSERT INTO dict_words (word, count)
  SELECT word, COUNT(*) 
  FROM words 
  GROUP BY word;
```
