# LEMON MARKETS TASK

## Overview:

API to place orders. 

## Requirements:
The API is built using following:
* OpenAPI Specification
* connexion


## Quick Start:

Install the dependencies using pipenv:
```
pipenv install
```

Run `app.py` from `service` or build and run the docker container as follows:

```
docker build -t lemonmarkets
docker run -p 0.0.0.0:5000:5000 lemonmarkets
```

To run the tests execute following from lemonmarkets:

```
python -m unittest discover
```

## Structure:

    - service
        - api
            - spec
                - api.yaml
            - orders.py
        - app.py
    - tests
        - test_orders.py
    - Pipfile
    - Pipfile.lock
    - Dockerfiler
        

* api.yaml contains the API specification
* orders.py contains the request handling.
* test_orders.py contains unittests.
* Pipfile contains all the dependencies. 


## Results:

The endpoint validates the request and returns the same result as of input/request.
Furthermore, Unittests covers following cases:
* valid request.
* request with invalid time.
* invalid request body.
