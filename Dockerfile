FROM        ec2-deploy.base

COPY        . /srv/project
CMD         pkill nginx


RUN         cp -f /srv/project/.config/nginx.conf /etc/nginx/nginx.conf
RUN         cp -f /srv/project/.config/nginx-app.conf /etc/nginx/sites-available/
RUN         rm -f /etc/nginx/sites-enabled/*
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/

RUN         cp /srv/project/.config/supervisord.conf /etc/supervisor/conf.d/

CMD         pkill nginx; supervisord -n