 # Django Docker

 ```
 docker-compose run web django-admin.py startproject composeexample .
 docker-compose -f docker-compose-dev.yml up
 docker-compose -f docker-compose-dev.yml run --service-ports web
 docker-compose -f docker-compose-dev.yml stop
 docker-compose -f docker-compose-dev.yml ps
 docker-compose -f docker-compose-dev.yml rm --all
 ```

# Linux

```
sudo chown -R $USER:$USER .
```
