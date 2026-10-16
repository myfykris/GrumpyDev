FROM php:8.2-cli
RUN apt-get update && apt-get install -y libxml2-dev && docker-php-ext-install soap pdo_mysql
WORKDIR /app
COPY . .
CMD ["php", "-S", "0.0.0.0:8080", "-t", "public"]
