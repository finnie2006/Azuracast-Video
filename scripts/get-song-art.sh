#!/bin/sh
curl -s 'https://stream.micmusicradio.be/api/nowplaying' | jq -c '.[] | select(.station.id | contains('1'))' | jq -r '.now_playing.song.art'
