#!/bin/sh
curl -s 'https://yourdomain.com/api/nowplaying' | jq -c '.[] | select(.station.id | contains('yourstationid'))' | jq -r '.station.listen_url'
