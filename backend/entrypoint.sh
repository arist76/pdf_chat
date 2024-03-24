
echo "----- Collect static files ------ " 
python pdf_chat/manage.py collectstatic --noinput

echo "-----------Apply migration--------- "
python pdf_chat/manage.py makemigrations 
python pdf_chat/manage.py migrate

echo "-----------Run gunicorn--------- "
cd pdf_chat
gunicorn -b :8000 pdf_chat.wsgi:application

