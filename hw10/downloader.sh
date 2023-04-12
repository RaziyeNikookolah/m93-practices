#!/bin/bash
printf "To download ... \nEnter your URL with https:// at first  \n"
read url_address
wget $url_address
exit_code=$?
if [ $exit_code -eq 0 ];then
    printf "$"
    echo "$url_address downloaded sucessfully :) " >> log.txt
else
    echo "$url_address failure on downloading :( " >> log.txt
fi 
#https://dl.download1music.ir/Music/Without-Words/0bikalam%20download1music.ir%20(1).mp3