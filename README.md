# Azuracast-Video
Azuracast-Video is a solution to stream your Azuracast radio to rtmp or a service such as YouTube or Twitch.

This image is based on https://github.com/accetto/ubuntu-vnc-xfce OBS is installed by default, and some OBS scripts are added to get data from your Azuracast API. 

Create Container: 

```docker
docker run -d -p 25901:5901  ghcr.io/finnie2006/azuracast-video:18.04
```

To use the default scene follow these instructions:
1. Open OBS
2. Select Scene Collection > Import
3. For Name type anything such as Default
4. For Collection Path enter `/home/headless/Desktop/OBS-Default-Scene/Default.json`
5. Leave Detected Application blank and then click Import
6. Then select Scene Collection > Default
7. If you don't like the background being just black, we have an mp4 you can use as the background:
   https://github.com/finnie2006/Azuracast-Video/raw/main/other-assets/example.mp4
9. Your good to go!

To use these scripts follow these instructions:
1. Open OBS
2. Select Tools > Scripts
3. Click the plus symbol and then select `/usr/share/obs/obs-plugins/frontend-tools/scripts/get-nowplaying.py`
4. It's ok if it errors out, then edit `/usr/share/obs/obs-plugins/frontend-tools/scripts/get-nowplaying.py` and change
5. Your good to go!


More info soon TM
