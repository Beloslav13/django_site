<h1>
    VSEOBOVSEM
</h1>
<h4>
    Для того чтобы проект работал у вас локально необходимо:
</h4>
<p>
- склонировать его
</p>
<p>
- в файле settigns.py закомменировать DATABASES с PostgreSQL и раскомментировать с sqlite3
</p>
<p>
- установить все пакеты
</p>
<pre>
pip install -r requirements.txt
</pre>
<p>
- применить миграции
<pre>
python manage.py makemigrations blogengine
python manage.py migrate
</pre>
<p>
- и запустить сервер
</p>
<pre>
python manage.py runserver
</pre>
