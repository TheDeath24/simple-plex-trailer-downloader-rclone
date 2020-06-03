import os
import glob
import time

def youtubed(movie_name, movie_path, mbsize, rclone, cache_trailer_dir):
    suche=movie_name + ' ' + wordsearch
    if rclone == 1:
        filename= '"'+ cache_trailer_dir + movie_name + "/" + movie_name + " -trailer" + ".%(ext)s" + '"'        
    else:
        filename= '"'+ movie_path + "/" + movie_name + " -trailer" + ".%(ext)s" + '"'
    
    download='youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio" --min-filesize '+ mbsize +' --max-filesize '+ mbmax + ' -o '+ filename + ' --merge-output-format mp4 "ytsearch1:' + suche + '"'

    if geobypass==1:
        download.replace(" -o "," --geo-bypass -o ")

    os.system(download)

    if rclone == 1:
        os.system('/usr/bin/rclone --config \"' + rclone_configpath + '\" ' + rclone_option + ' \"' + rclone_pathfrom + '\" \"'  + rclone_pathto + '\"')


# Global Vars
start_time = time.clock()
append = "-trailer"  # Plex requires this
movie_dir = ""  # Your Movie directory
mdsize="0m"    #minium Downloadsize in MB
mbmax="200m"    #maximum Downloadsize in MB
wordsearch="German Trailer" #search words for youtube
geobypass=1 #use geo-bypass 1=true 0=disabled

# if you use rclone 
rclone=1 #rclone 1=autoupload 0=disabled
rclone_configpath="/opt/rclone.conf" #rclone config path+rclone.conf
rclone_option="move" #move or copy
rclone_pathto="upload:/movies"
cache_trailer_dir = "/opt/Trailer/" #temp dir for the trailer, when you use rclone its the bestway to cache and upload 
rclone_pathfrom=cache_trailer_dir #cachedir

# All movies must be in separate directories
movie_name_list = os.listdir(movie_dir)

# Empty lists for later
movie_dir_list = []
downloaded_trailer_list = []

# Filter dotfiles
for movie in movie_name_list:
    if movie.startswith('.'):
        movie_name_list.remove(movie)

# Get movie paths
for movie in movie_name_list:
    movie_dir_list.append(movie_dir + movie + "/")

# Download trailers
for x in range(len(movie_name_list)):
    # Check if trailer exists
    # If so, skip
    if glob.glob("{}*-trailer*".format(movie_dir_list[x])):
        print(
            "Pre-existing trailer for {}. Skipping...".format(movie_name_list[x]))
        continue

    else:
        youtubed(movie_name_list[x], movie_dir_list[x], mdsize, rclone, cache_trailer_dir)
        continue  

# If no trailers were downloaded / updated
if  len(downloaded_trailer_list) == 0:
    print("-----------------------------------------------------------")
    print("Done. All trailers up to date.")
    print("-----------------------------------------------------------")

# Some trailers were downloaded
if len(downloaded_trailer_list) > 0:
    print("-----------------------------------------------------------")
    print("Downloaded {} trailers for:".format(len(downloaded_trailer_list)))
    print("-----------------------------------------------------------")
    for x in range(len(downloaded_trailer_list)):
        print(downloaded_trailer_list[x])

# Total run time
print("-----------------------------------------------------------")
print("Total run time: {:.2} seconds".format(time.clock() - start_time))
print("-----------------------------------------------------------")






