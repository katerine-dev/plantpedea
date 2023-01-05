# plantpedia
Application for querying information about plants

## Managing Dependencies 

### Activating venv

```
source venv/bin/activate
```

### Installing project dependencies

```
pip install -r requirements.txt
```
### Adding dependency 

```
pip install <PACKAGE_NAME>
pip freeze > requirements.txt
``` 

## Running the database

```
docker run --detach -p 3306:3306 --name plantpedia -v /Users/katerinelindawitkoski/Documents/plantpedia/.dbdata:/var/lib/mysql --env MARIADB_USER=plantpedia --env MARIADB_PASSWORD=plantpedia --env MARIADB_ROOT_PASSWORD=plantpedia --env MARIADB_DATABASE=plantpedia --rm mariadb:latest
```
