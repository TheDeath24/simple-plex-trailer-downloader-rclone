# simple-plex-trailer-downloader-rclone
Simple Plex Movie Trailer downloader with optional rclone support

# Must fill out:

movie_dir = ""  # Your Movie directory 

mdsize="0m"    #minium Downloadsize in MB

mbmax="200m"    #maximum Downloadsize in MB

wordsearch="German Trailer" #search words for youtube

geobypass=1 #use geo-bypass 1=true 0=disabled

# if you want use rclone you must set this to 1 and fill out all other options for rclone!
rclone=1 #rclone 1=autoupload 0=disabled

rclone_configpath="/opt/rclone.conf" #rclone config path+rclone.conf

rclone_option="move" #move or copy

rclone_pathto="upload:/movies"

cache_trailer_dir = "/opt/Trailer/" #temp dir for the trailer, when you use rclone its the bestway to cache and upload 

rclone_pathfrom=cache_trailer_dir #cachedir
