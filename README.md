# Image Comparison API

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Working within a virtual environment is recommended whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies
Once you have your virtual environment running. Install dependencies by
```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [OpenCV](http://opencv.org) OpenCV is an open-source library that includes several hundreds of computer vision algorithms.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

Ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:image-comparison`
6. Create new roles for:
    - Developer
        - can `get:image-comparison`

## Endpoints Reference

GET '/image-comparison?imageA=<image_path>&imageB=<image_path>'
- Fetches two pictures for comparison
- imagePath could be local file or url
- Request Arguments: None
- Returns: A simliarity percentage
- Sample: 
```bash
{
    "percentage": "36.26%",
    "success": true
}
```

## Error handling

The error will be return as JSON format as followed:
Not found error (404)
```bash
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

Authentication error (401)
```bash
{
    "error": 401,
    "message": {
        "code": "authorization_header_missing",
        "description": "Authorization header is expected."
    },
    "success": false
}
```
#### Test
To run the test, run 
```bash
python test.py
```
The authentication key will expires in 24 hours, please ask for new authentication token if you need access.

## Authors
Chia-Ning (Jeffrey) Lee is in charged of backend Web Api.
