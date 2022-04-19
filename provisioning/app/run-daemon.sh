#!/bin/bash
docker run -d -t -i -e FLASK_APP="main" \
-e FLASK_APP=main \
-e FLASK_CONFIG=production \
-e USER_NAME=testModule1 \
-e PASSWORD=detteerentest \
-p 8081:80 \
  --restart no --name izy-infoboard-v2 izy-infoboard-v2:1.0