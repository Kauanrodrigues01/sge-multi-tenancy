FROM nginxinc/nginx-unprivileged:1-alpine

RUN chmod 644 /etc/nginx/conf.d/default.conf
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

RUN chmod 755 /etc/nginx/conf.d

USER root

RUN mkdir -p /sge/static
RUN chmod 755 /sge/static

EXPOSE 80