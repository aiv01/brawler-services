# Players API

<br>

## GET

### Check if player already exists
* ***url***: '/players/already-exists/'
* ***variable***: nickname
* ***return***: JSON

#### Examples with httpie:
```
> http http://www.example.com/players/already-exists/?nickname="player nickname"
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
  "player_already_exists": false
}
```
```
> http http://www.example.com/players/already-exists/?nickname="player nickname"
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "player_already_exists": true
}
```

<br>

## POST

### Register player
* ***url***: '/players/register/'
* ***variables***: nickname, password, tagline
* ***return***: JSON

#### Examples with httpie:
```
> http -f POST http://www.example.com/players/register/ nickname="player nickname" password="player password" tagline="player tagline"
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
  "player_register": true
  "token": "e1cdcd42-0b98-4d12-82fd-53d0fb241ec6"
}
```
```
> http -f POST http://www.example.com/players/register/ nickname="player nickname" password="player password" tagline="player tagline"
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "player_register": false,
    "fields": "nickname, password, tagline",
    "info": "this fields require a string of max 255 chars and nickname must be unique"
}
```

### Login player
* ***url***: '/players/login/'
* ***variables***: nickname, password
* ***return***: JSON

#### Examples with httpie:
```
> http -f POST http://www.example.com/players/register/ nickname="player nickname" password="player password"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "player_login": true
}
```
```
> http -f POST http://www.example.com/players/register/ nickname="player nickname" password="player password"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "fields": "nickname, password",
    "info": "wrong nickname and/or password",
    "player_login": false
}
```
<br>

## GET/POST

### Upload player photo
* ***url***: '/players/photo/'
* ***variables in GET***: token
* ***raw data***: bit string of .png
* ***return***: JSON

#### Example with python3 and urllib
```python
>>> from urllib import request
>>> url = 'http://localhost:8080/players/photo/?token=e1cdcd42-0b98-4d12-82fd-53d0fb241ec6'
>>> photo = b'<bit string of .png>'
>>> req = request.Request(url, photo, {'Content-Type': 'application/octet-stream'})
>>> url_open = request.urlopen(req)
>>> url_open.read()
b'{"player_upload_photo": true}'
```
```python
>>> from urllib import request
>>> url = 'http://localhost:8080/players/photo/?token=4d12-82fd-53d0fb241ec6'
>>> photo = b'<bit string of .png>'
>>> req = request.Request(url, photo, {'Content-Type': 'application/octet-stream'})
>>> url_open = request.urlopen(req)
>>> url_open.read()
b'{"player_upload_photo": false, "info": "player with this token does not exists"}
```

<br><br>
<hr>

##### TODO
* Player login
* Player upload audio
* Player change password
