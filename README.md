# Back-end for Notes application created in Django Rest Framework
##  Required for running the project:
First of all you have to clone github project and install dependencies

First: 

 ```git clone https://github.com/Insanch1k/Notes-App.git```
 
 
Next:
 
 ```pip install -r requirements.txt```
 
 For set up database:
 
 ```python manage.py migrate```
 
 Create admin account:
 
 ```python manage.py createsuperuser```
 
 Then:
 
 ```python manage.py makemigrations ```
 
 Then again run:
 
 ```python manage.py migrate```
 
 Start the development server:
 
 ```python manage.py runserver```
 
##Examples:

 Get all notes:
 
 ```
 curl  http://127.0.0.1:8000/api/notes/list/
```
 
 
 ```
[{"id":8,"title":"new title","content":"new_content","created":"2020-10-11T18:32:28.638826Z","modified":"2020-10-12T10:07:22.794555Z"}
{"id":9,"title":"test2","content":"test2","created":"2020-10-12T22:44:22.036672Z","modified":"2020-10-12T22:44:22.036705Z"}]
```
 
 Get detail information:
 
 ```
 curl  http://127.0.0.1:8000/api/notes/detail/8/
```
 
 
 ```
 [{"id":8,"title":"new title","content":"new_content","created":"2020-10-11T18:32:28.638826Z","modified":"2020-10-12T10:07:22.794555Z"}]
```
 
 Get history:
 
 ```
 curl  http://127.0.0.1:8000/api/notes/history/8/
```


```
[{"version":1,"changed_note":8,"changed_at":"2020-10-11T18:32:50.654155Z","title":"DELETE","content":"We are testing delete  function"},{"version":2,"changed_note"
:8,"changed_at":"2020-10-12T10:03:31.151175Z","title":"DELETE","content":"We are testing delete  function (Updated)"},{"version":2,"changed_note":8,"changed_at":"2
020-10-12T10:04:20.218468Z","title":"id7777","content":"new id"},{"version":3,"changed_note":8,"changed_at":"2020-10-12T10:07:22.638259Z","title":"frfrfr","content
":"frfrfrf"}]
```
 
 
 
 
 
