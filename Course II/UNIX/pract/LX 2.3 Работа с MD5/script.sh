FILE=$HOME/tmp/passwd.backup
ORIGINAL_FILE=/etc/passwd

if [ -f "$FILE" ]; then
    echo "$FILE exists."
    md5_first=$(md5sum $FILE | awk '{ print $1 }')
    md5_second=$(md5sum $ORIGINAL_FILE | awk '{ print $1 }')
    
    if [ "$md5_first" = "$md5_second" ]; then
	echo "MD5 OK"
    else
        echo "MD5 WARNING"
        cp $ORIGINAL_FILE $FILE
    fi

    echo $md5_first
    echo $md5_second

else 
    cp $ORIGINAL_FILE $FILE
fi
