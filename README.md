 # Create a Django project

 ```
 docker-compose run web django-admin.py startproject composeexample .
 ```

 # Compose UP

 ```
 docker-compose -f docker-compose-dev.yml up
 ```

 # Compose ps

 ```
 docker-compose -f docker-compose-dev.yml ps
 docker-compose -f docker-compose-dev.yml rm --all
 ```