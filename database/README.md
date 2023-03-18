# Build image
`docker build -t database:latest .`

# Create network
`docker network create moneyrobot`

# Run container

# TODO: Remove these passwords and put them in AWS.
```
docker run --name database -d \
    -p 3306:3306 \
    -e MYSQL_USER=moneyrobot \
    -e MYSQL_PASSWORD=CREAM \
    -e MYSQL_ROOT_PASSWORD=Password123! \
    -v mysql:/var/lib/mysql \
    --restart unless-stopped \
    database:latest
```

# Login as root user and give moneyrobot user privileges to moneyrobot database
- `docker exec -it database mysql -p`
- `mysql> GRANT ALL PRIVILEGES ON moneyrobot.* TO 'moneyrobot'@'%';`

# Get a shell inside the container
`docker exec -it database mysql -u moneyrobot -p`

# Access from host machine
`mysql -h 127.0.0.1 -P 3306 -u root -p `

# Example insert
