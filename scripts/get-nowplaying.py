import subprocess
import obspython as obs
import threading
import sys
import re

name_source = obs.obs_get_source_by_name('name_source')
art_source = obs.obs_get_source_by_name('art_source')
audio_source = obs.obs_get_source_by_name('audio_source')
dj_source = obs.obs_get_source_by_name('dj_source')

btrue = 'true'
bfalse = 'false'

def getapidata():
  long_song_name = subprocess.check_output("curl -s 'https://stream.yourdomain.com/api/nowplaying' | jq -c '.[] | select(.station.id | contains('yourstationid'))' | jq -r '.now_playing.song.text'", shell=True).decode('utf-8')
  song_name = re.sub("(.{20})", "\\1\n", long_song_name, 0, re.DOTALL)
  name_data = obs.obs_data_create()
  obs.obs_data_set_string(name_data, "text", song_name)
  obs.obs_source_update(name_source, name_data)

  song_art = subprocess.check_output("curl -s 'https://stream.yourdomain.com/api/nowplaying' | jq -c '.[] | select(.station.id | contains('yourstationid'))' | jq -r '.now_playing.song.art'", shell=True).decode('utf-8')
  art_data = obs.obs_data_create()
  obs.obs_data_set_string(art_data, "url", song_art)
  obs.obs_source_update(art_source, art_data)

  song_audio = subprocess.check_output("curl -s 'https://stream.yourdomain.com/api/nowplaying' | jq -c '.[] | select(.station.id | contains('yourstationid'))' | jq -r '.station.listen_url'", shell=True).decode('utf-8')
  audio_data = obs.obs_data_create()
  obs.obs_data_set_string(audio_data, "url", song_audio)
  obs.obs_source_update(audio_source, audio_data)

  dj_name = 'Now live: ' + subprocess.check_output("curl -s 'https://stream.yourdomain.com/api/nowplaying' | jq -c '.[] | select(.station.id | contains('yourstationid'))' | jq -r '.live.streamer_name'", shell=True).decode('utf-8')
  dj_islive = subprocess.check_output("curl -s 'https://stream.yourdomain.com/api/nowplaying' | jq -c '.[] | select(.station.id | contains('yourstationid'))' | jq -r '.live.is_live'", shell=True).decode('utf-8')
  autodj_name = 'Now live: AutoDJ'
  if dj_islive == btrue:
    dj_data = obs.obs_data_create()
    obs.obs_data_set_string(dj_data, "text", dj_name)
    obs.obs_source_update(dj_source, dj_data)
  else:
    autodj_data = obs.obs_data_create()
    obs.obs_data_set_string(autodj_data, "text", autodj_name)
    obs.obs_source_update(dj_source, autodj_data)

  threading.Timer(1.0, getapidata).start()

getapidata()
