**below you will find commands to run the admin site**

```sh
cd backend/pdf_chat/
pip install -r requirements.txt

```

then you should create an admin user

```sh
python manage.py createsuperuser
```
You can enter your credentials there. you can set
Username: abc
email: you can skip this part
password: your preferenced password. It will ask twice

after the above step is done. you can go to 
`localhost:8000/admin` to go to the admin site. there you can
enter your credentials you entered above. in the admin site
you can see, create, delete and update subjects, pdfs, 
user's information their preferences and their messages