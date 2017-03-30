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
    "token": "ba670d48832f90e0cef44e7cf22a99a70ecf5bf9171b4f40fe14aac499ef5ecbb8f30ae398dd75a330fc28213b92234d558bb5c3dbd3a94856f34afedb6d2283"
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
<br>

## GET/POST

### Upload player photo
* ***url***: '/players/photo/'
* ***variables in GET***: token
* ***raw data***: bit string encode base64 of .png
* ***return***: JSON

#### Example with python3 and urllib
```python
>>> from urllib import request
>>> url = 'http://localhost:8080/players/photo/?token=ba670d48832f90e0cef44e7cf22a99a70ecf5bf9171b4f40fe14aac499ef5ecbb8f30ae398dd75a330fc28213b92234d558bb5c3dbd3a94856f34afedb6d2283'
>>> photo_base64 = b'<bit string encode base64 of .png>'
>>> req = request.Request(url, photo_base64, {'Content-Type': 'application/octet-stream'})
>>> url_open = request.urlopen(req)
>>> url_open.read()
b'{"player_upload_photo": true}'
```
```python
>>> from urllib import request
>>> url = 'http://localhost:8080/players/photo/?token=ba670d48832f90e0cef44e7cf22a99a70e'
>>> photo_base64 = <bit string encode base64 of .png>
>>> req = request.Request(url, photo_base64, {'Content-Type': 'application/octet-stream'})
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
