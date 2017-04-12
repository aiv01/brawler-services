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

### Get player's photo and audio
* ***url***: '/players/photo-audio/'
* ***variable***: nickname
* ***return***: JSON

#### Examples with httpie:
```
> http http://www.example.com/players/photo-audio/?nickname="player nickname"
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "photo": "www.example.com/media/players/photos/photo_player_nickname.png",
    "audio": "www.example.com/media/players/audio/audio_player_nickname.ogg"
}
```
```
> http http://www.example.com/players/photo-audio/?nickname="player nickname 2"
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "photo": null,
    "audio": null
}
```
```
> http http://www.example.com/players/photo-audio/?nickname="player nick"
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "error": "player with this nickname does not exists"
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
<br>

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
    "token": "e1cdcd42-0b98-4d12-82fd-53d0fb241ec6"
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

### Auth player (server)
* ***url***: '/players/server-auth/'
* ***variables***: token, ip
* ***return***: JSON

#### Examples with httpie:
```
http -f POST http://example:8080/players/server-auth/ token="e1cdcd42-0b98-4d12-82fd-53d0fb241ec6" ip="89.100.11.22"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "auth_ok": true,
    "nickname": "player nickname"
}
```
```
http -f POST http://example:8080/players/server-auth/ token="e1cdcd42-0b98-4d12-82fd-53d0fb241ec6" ip="89.100.11.22"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "aut_ok": false,
    "fields": "ip",
    "info": "ip are not equal"
}
```
```
http -f POST http://example:8080/players/server-auth/ token="4d12-82fd-53d0fb241ec6" ip="89.100.11.22"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "auth_ok": false,
    "fields": "token",
    "info": "player with this token does not exists"
}
```
<br>

### Auth player (client)
* ***url***: '/players/client-auth/'
* ***variables***: token, port
* ***return***: JSON

#### Examples with httpie:
```
http -f POST http://example:8080/players/client-auth/ token="e1cdcd42-0b98-4d12-82fd-53d0fb241ec6" port="2468"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "auth_ok": true
}
```
```
http -f POST http://example:8080/players/client-auth/ token="e1cdcd42-0b98-4d12-82fd-53d0fb241ec6" port="2468"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "aut_ok": false,
    "fields": "ip",
    "info": "ip are not equal"
}
```
```
http -f POST http://example:8080/players/client-auth/ token="4d12-82fd-53d0fb241ec6" port="2468"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "auth_ok": false,
    "fields": "token",
    "info": "player with this token does not exists"
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
