sudo ln -sf /home/crow/work_server/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

cd /home/crow/work_server/web/projects/mongel
gunicorn -c /home/crow/work_server/web/etc/gunicorn.config.py mongel.wsgi:application
cd 
