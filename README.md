# Parser of books from tululu.org and presentation library on the website

App for parsing info and downloading books and their covers from of [Tululu](https://tululu.org/).

## Usage online

Online-library is available at GitHub Pages website: [Sci-Fi-Library](https://circlsun.github.io/sci-fi-library/pages/index1.html)

## Usage offline

Download this repository to your computer and open any  `index(1..10).html` from the `pages` folder or [here](http://127.0.0.1:5500/) with any browser and click button `Читать`. Have fun reading!

## How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Usage parse_tululu_all.py

Just run the python script `main.py` with the following concole command:
```
python main.py 30 40
```
Where argument <30> is the starting book, and <40> is the last book to download.

#### For example:
```
python main.py 50 53
```
Books from <50> to <53> will be downloaded to the 'media/books' folder and their covers to the 'medai/images' folder.
And in console the result will be: 
```
Заголовок: Этика перераспределения
Автор: Жувенель Бертран     
Жанр: ['Деловая литература']
Комментарии: []

Заголовок: Как это делается - Финансовые, социальные и информационные технологии
Автор: Автор неизвестен     
Жанр: ['Деловая литература']
Комментарии: []

Заголовок: Как найти высокооплачиваемую работу с помощью Internet
Автор: Рудинштейн Марк
Жанр: ['Деловая литература', 'Прочая компьютерная литература']
Комментарии: ['Набор общеизвестных фраз и ничего личного, привнесенного автором. Скучно, малоинформативно, не стоит тратить время на книгу тем, кто собирается таким образом искать работу через Интернет.']
```
### Usage parse_tululu_category.py

Just run the python script `parse_tululu_category.py` with the following concole command:
```
python parse_tululu_category.py
```
Only the first five sci-fi pages of books will be downloaded to the default folder `books` And the `book_description.json` to the default folder `json` (this is about 95 books).

And in console the result will be: 
```
Link of the book: https://tululu.org/b239/
:
Link of the book: https://tululu.org/b8467/

The previous book is not available for download.
HTTP error: [<Response [302]>]. Use google.com to translate.

Link of the book: https://tululu.org/b8559/
```
#### Optional arguments:

The program accepts the following optional arguments:

`--start_page`: after this argument, the number of the page from which to start downloading is specified. If not specified, the download starts from 1 page;

`--end_page`: after this argument, the number of the page to finish downloading (not inclusive) is specified. If not specified, all subsequent pages are downloaded (no more than 701);

`--skip_imgs`: if this flag is present, images of books are not downloaded;

`--skip_txt`: if this flag is present, the texts of books are not downloaded;

`--dest_folder`: after this argument, the destination folder is specified in which the text of books and images will be created;

`--json_path`: path to ***.json file with results

Example for all arguments:
```
python parse_tululu_category.py --start_page 698 --end_page 700 --skip_imgs --skip_txt --json_path 'books_json'  --dest_folder 'new_books'
```
And in console the result will be:
```
Link of the book: https://tululu.org/b44561/
Link of the book: https://tululu.org/b44562/
:
Link of the book: https://tululu.org/b59280/
Link of the book: https://tululu.org/b59440/
```
### If you want to create your own website

1. Delete `json`, `pages` and `media` derectories from your repo.
2. Run parse_tululu_category.py:
```
python parse_tululu_category.py --start_page 500 --end_page 600
```
3. Run render_website.py:
```
python render_website.py
```
4. Open any `index(1..10).html` from the `pages` folder or [here](http://127.0.0.1:5500/) with any browser and click button `Читать`.


### Project Goals

The code is written for educational purposes for the online-course of the Python Web developer on [Devmen](https://dvmn.org/)