# Cookity Cook

**Cookity Cook** is a recipe manager. It uses plain `.md` files to store recipes and a simple CLI to manage them.

## Usage

Rolling the dice to choose a breakfast-lunch-dinner combo:

```shell
% python -m dice
breakfast: crepes.md
    lunch: solyanka.md
   dinner: chicken-curry-with-rice.md
```

Listing ingredients for chosen recipes:

```shell
% python -m list ./recipes/breakfasts/crepes.md ./recipes/lunches/solyanka.md ./recipes/dinners/chicken-curry-with-rice.md
Вода                 2.5 л
Картофель            4 шт (~500 г)
Копчености           300 г
Куриное филе         1 шт
Лавровый лист        5 шт (~1 г)
Лимон                6 ломтиков (~40 г)
Лук                  1 шт (~100 г) + 1 шт
Молоко               0.75 ст (~175 г) + 0.75 ст (~175 г)
Морковь              1 шт (~100 г)
Мука                 1.25 ст (~200 г)
Оливки               1 уп (~70 г)
Перец душистый       5 шт (~1 г)
Приправа карри       0.5 ст.л.
Растительное масло   1 ч.л. (~3 г) + 1 ч.л. (~3 г)
Рис басмати          60 г
Сахар                1 ст.л. (~25 г) + 1 ч.л. (~8 г)
Сливки 20%           60 мл
Сливочное масло      2 ч.л. (~15 г)
Соленые огурцы       4 шт (~200 гр)
Соль                 0.25 ч.л. (~1 г) + 1 ст.л. (~30 г)
Стейк говяжий        1 шт (~200 г)
Томатная паста       1 ст.л. (~30 г)
Томатный соус        1.25 ст.л.
Чеснок               2 зубчика (~10 гр) + 1 зубчик
Яйца                 2 шт (~100 г)
```

Or you can use a glob to list the whole group of recipes:

```shell
% python -m list ./recipes/new-year/*.md
Ананасы            1 бан.
Горошек            1 бан.
Картофель          4 шт + 4 шт
Корнишоны          1 бан.
Крабовые палочки   1 шт
Кукуруза           1 бан.
Куриная грудка     225 г
Курица             1 грудка
Лосось             0.3 кг
Лук белый          1 шт
Майонез            0.1 кг + 0.1 кг + 0.1 кг + 0.1 кг
Морковь            1 шт + 1 шт
Пищевая пленка     1 шт
Репчатый лук       75 г
Свежие грибы       150 г
Свекла             2 шт
Сливки             150 мл
Сливочное масло    45 г
Сыр                0.2 кг + 150 г
Фисташки           ?
Форма для торта    1 шт
Яблоко             1 шт
Яйца               3 шт + 4 шт + 4 шт
```
