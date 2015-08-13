#!/bin/bash

echo "Status: 200 Success"
echo "Content-type: text/plain"
echo ""

GPIO=/usr/local/bin/gpio

ROOM=`echo "$QUERY_STRING" | sed -n 's/^.*room=\([^&]*\).*$/\1/p'`
ACTION=`echo "$QUERY_STRING" | sed -n 's/^.*action=\([^&]\).*/\1/p'`

# read
READ=`$GPIO read $ROOM`

case $ACTION in
0)
	echo "$READ"
	;;
1)	
	$GPIO write $ROOM 1
	;;
2) 
	$GPIO write $ROOM 0
	;;
*)
	echo "Error doing $ACTION"
esac
