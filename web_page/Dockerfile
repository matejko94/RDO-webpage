FROM nginx:1.14.1-alpine

WORKDIR /usr/src/app

COPY .. /usr/share/nginx/html


COPY nginx/default.conf /etc/nginx/conf.d/

#RUN rm -rf /usr/share/nginx/html/*


#COPY /usr/src/app /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]