@echo off

if not "%1"=="" (
   set OSIRIS_GRAPH_SERVER_TOKEN=%1
) else (
    echo You must specify a graph server token as the 1st argument.
    exit 1
)

echo OSIRIS_GRAPH_SERVER_TOKEN set. 