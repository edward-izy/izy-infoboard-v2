#!/bin/bash
docker run -d -t -i -e FLASK_APP="main" \
-e FLASK_APP=main \
-e FLASK_CONFIG=production \
-e USER_NAME=infoboardv2-sandbox \
-e PASSWORD=tcm-HVQ7kjx9ahx_ukg \
-e KV_PATH="module/parameters/sandbox/infoboardv2-sandbox" \
-e PUBLIC_PATH=jwt/sandbox/public \
-p 8081:80 \
  --restart no --name izy-infoboard-v2 izy-infoboard-v2:1.0