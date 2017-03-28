# Players API


## GET

### Check if player already exists
Pass nickname variable on url '/players/already-exists/' and return a JSON
* Example with httpie
```
http http://www.example.com/players/already-exists/?nickname=player_nickname

{
  "player_already_exists": true
}
```


## POST

### Register player
Pass nickname, password, photo, audio and tagline on url '/players/register/' and return a JSON
* Example with httpie
```
http -f POST http://www.example.com/players/register/ nickname=player_nickname password=player_password photo=path_to_photo audio=path_to_audio tagline=player_tagline

{
  "player_register": true
}
```


## TODO
* Player login
* Player reset password
