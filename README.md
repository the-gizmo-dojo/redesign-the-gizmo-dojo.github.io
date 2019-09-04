To Run in docker container run:

```bash
docker run -dit -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4
```