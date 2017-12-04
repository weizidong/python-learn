#!/usr/bin/env bash

usage() {
    echo "----------USAGE:--------------------"
    echo "provider  start  xx"
    echo "provider  stop   xx"
    echo "-------------------------------------"
}

cmd=$1
module=$2
JAVA_OPTS="-server -Xms4096m  -Xmx4096m  -verbose:gc  -XX:+PrintGCDetails  -XX:PermSize=256M -XX:MaxPermSize=512m -Ddubbo.spring.config=classpath:spring-context.xml"
if [ $# -gt 2 ] || [ $# -lt 1 ]; then
    usage;
elif [ $cmd != 'start' ] && [ $cmd != 'stop' ]; then
    usage;
else
    case $cmd in
        'start')
            if [ $# -eq 1 ]; then
                echo "未指定模块！"
            else
                if [ -n $module".jar" ]; then
                    procid=`ps -fe | grep $module".jar" | grep -v grep | awk '{print $2}'`
                    if [ -z "$procid" ]; then
                        echo "启动模块【"$module"】中......"
                        echo
                        nohup java $JAVA_OPTS -jar $module".jar" > "./log/"$module".log" 2>&1 &
                        echo "模块【"$module"】启动成功！"
                    else
                        echo "模块【"$module"】重启中......pid:"$procid
                        echo
                        kill -15 $procid
                        nohup java $JAVA_OPTS -jar $module".jar" > "./log/"$module".log" 2>&1 &
                        echo "模块【"$module"】重启成功！"
                    fi
                else
                    echo "模块【$module】不存在！"
                fi
                echo
            fi
        ;;
        'stop')
            if [ $# -eq 1 ]; then
                echo "未指定模块！"
            else
                echo "停止模块【"$module"】......"
                echo
                procid=`ps -fe | grep $module".jar" | grep -v grep | awk '{print $2}'`
                if [ -z "$procid" ]; then
                    echo "模块【"$module"】未启动过！"
                else
                    kill -15 $procid
                    echo "模块【"$module"】停止成功！"
                fi
                echo
            fi
        ;;
    esac
fi