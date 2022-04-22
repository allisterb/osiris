@echo off

if not "%1"=="" (
   set GRAPHISTRY_USER=%1
) else (
    echo You must specify a Graphistry user name as the 1st argument.
    exit 1
)

if not "%2"=="" (
   set GRAPHISTRY_PASS=%2
) else (
    echo You must specify a Graphistry user password as the 2nd argument.
    exit 1
)
echo GRAPHISTRY_USER and GRAPHISTRY_PASS set.