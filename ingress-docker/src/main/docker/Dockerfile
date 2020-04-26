FROM nginx:1.17.1-alpine
LABEL version="1.0.0"
LABEL maintainer="Constantin Nica"

COPY nginx.conf /etc/nginx/nginx.conf
#WORKDIR /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]