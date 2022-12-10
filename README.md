# plantpedea
Application for querying information about plants


## Running the database
```
docker run --detach -p 3306:3306 --name plantpedia --env MARIADB_USER=plantpedia --env MARIADB_PASSWORD=plantpedia --env MARIADB_ROOT_PASSWORD=plantpedia --env MARIADB_DATABASE=plantpedia --rm mariadb:latest
```