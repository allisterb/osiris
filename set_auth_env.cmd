@echo off

if not "%1"=="" (
   set OSIRIS_GRAPH_SERVER_USER=%1
) else (
    echo You must specify a graph server user name as the 1st argument.
    exit 1
)

if not "%2"=="" (
   set OSIRIS_GRAPH_SERVER_PASS=%2
) else (
    echo You must specify a graph server user password as the 2nd argument.
    exit 1
)

if not "%3"=="" (
   set OSIRIS_GRAPH_SERVER_TOKEN=%3
) else (
    echo You must specify a graph server authentication token as the 3rd argument.
    exit 1
)