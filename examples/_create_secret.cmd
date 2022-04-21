
if "%1"=="" (
   echo You must specify the graph server URL as the first argument.
   exit /b 1
)
if "%2"=="" (
   echo You must specify the graph name as the first argument.
   exit /b 1
)
if "%3"=="" (
   echo You must specify the secret alias as the third argument.
   exit 1
)
@for /f "delims=" %a in ('osi graph create-secret') do @set OSIRIS_GRAPH_SERVER_SECRET=%a
echo %OSIRIS_GRAPH_SERVER_SECRET%