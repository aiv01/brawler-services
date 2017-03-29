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
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
  "player_already_exists": false
}
```
```
http http://www.example.com/players/already-exists/?nickname="player nickname"
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
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
  "player_register": true
}
```
```
> http -f POST http://www.example.com/players/register/ nickname="player nickname" password="player password" tagline="player tagline"
Connection: close
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
    "player_register": false,
    "fields": "nickname, password, tagline",
    "info": "this fields require a string of max 255 chars and nickname must be unique"
}
```

<br><br>
<hr>

##### TODO
* Player login
* Player reset password
