 # Django Docker

 ```
 docker-compose run web django-admin.py startproject composeexample .
 docker-compose -f docker-compose-dev.yml up
 docker-compose -f docker-compose-dev.yml ps
 docker-compose -f docker-compose-dev.yml rm --all

 docker-compose -f docker-compose-dev.yml up
 docker-compose -f docker-compose-dev.yml run --service-ports web
 ```

# Linux

```
sudo chown -R $USER:$USER .
```
