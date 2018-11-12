#!/usr/bin/bash

SCRIPT_DIR=$(cd $(dirname $0) && pwd)
APP_DIR=$(cd $SCRIPT_DIR/.. && pwd)

# Default parameters
JAVA=${JAVA:=java}
JAVA_HOME=${JAVA_HOME:=/usr/lib/jvm/java}
CLASSPATH=${CLASSPATH:=$CLASSPATH}
JAVA_OPTS=${RUN_JAVA_OPTS:=-Xmx4G}

if [ -d "$JAVA_HOME" ]; then
	JAVA="$JAVA_HOME/bin/java"
fi

$JAVA $JAVA_OPTS -cp $APP_DIR/lib:$CLASSPATH -jar $APP_DIR/lib/picard.jar $@
