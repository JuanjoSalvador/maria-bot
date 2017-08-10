#!/bin/sh

DAEMON="src/mariabot.py"
PIDFILE="mariabot.pid"

start () {
  $DAEMON &
  echo $! > $PIDFILE
}

stop () {
  cat $PIDFILE >> kill
}

case "$1" in

    start|stop)
        ${1}
        ;;

    reload)
        stop
        start
        ;;

    *)
        echo "Usage: manager.sh {start/stop/reload}"
        exit 1
        ;;

esac
exit 0
