# Web Services

# Sprints and User Stories

Sprint 1 - March 20 - April 3
-

Player Registration: nickname, password, photo, audio, tagline

(sprint meeting)


Sprint 2 - April 3 - April 19
-

* store the ip address when doing login call
* check the ip address for any subsequent request
* add field for endpoint information (2 fields, one IPAddress and an unsigned short/int)
* the clients sends the udp endpoint in the setendpoint call
* implement the login call
* add get_photo call
* add get_audio call
* add the setendpoint call

(sprint meeting)

Sprint 3 - April 19 - May 3
- 

* Learn how to build graphs/charts from elasticsearch (evaluate javascript graphics libraries)
* Install elasticsearch

20170421 still missing microphone integration

(sprint meeting)

Sprint 4 - May 3 - May 17
-

* Study Elasticsearch
* Audio recording (TD)
* Server registration API for game server nodes


(sprint meeting)

20170517 TD Elasticsearch
20170517 postponed listing api for game clients

Sprint 5 - May 17 - May 31
-

* Ladder/Leaderboard api (Stefano, Christian, Alberto)
* Achievements (backstab, km run, number of attacks, combo length ...)
* Credits API (finalize)
* Study ElasticSearch
* Censorship api
* Default photos (Spare)

(sprint meeting)

Sprint 6 - May 31 - Jun 14 
-

* Server registration listing API for game clients
* json api for returning the list of playing warriors
* json api for spectators actions
* udp packets to brawler-server (https://docs.python.org/3/library/struct.html)

```python
import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(data, (ip_as_string, port_as_int))
```

(sprint meeting)

Sprint 7 - Jun 14 - Jun 28
-

(sprint meeting)
