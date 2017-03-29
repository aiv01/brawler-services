# Players API

<br>

## GET

### Check if player already exists
* ***url***: '/players/already-exists/'
* ***variable***: nickname
* ***return***: JSON

#### Example with httpie
```
> http http://www.example.com/players/already-exists/?nickname="player nickname"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
  "player_already_exists": false
}
```

<br>

## POST

### Register player
* ***url***: '/players/register/'
* ***variables***: nickname, password, tagline
* ***return***: JSON

#### Example with httpie
```
> http -f POST http://www.example.com/players/register/ nickname="player nickname" password="player password" tagline="player tagline"
HTTP/1.1 200 OK
Content-Type: application/json
X-Frame-Options: SAMEORIGIN

{
  "player_register": true
}
```

<br><br>
<hr>

##### TODO
* Player login
* Player reset password
