# Verteego test

## Build and run 

To build and run the application, please use :

```
docker-compose up --build -d
```

The POST API `/usecase` can be accessed on 

```
127.0.0.1:5000/usecase
```

## Stop

To stop the app, you can use :

```
docker-compose down
```

## Unit tests

To run unit tests, please use the following command as the app is running :

```
docker exec <container name or id> py.test
```

It should be : 

```
docker exec verteego_test_web_1 py.test
```
