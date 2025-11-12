Commands:
- docker-compose up --build


GUI home page: http://localhost:2525
API domain: http://localhost:8090/users

Create new imposter from json file: 
- curl -X POST -H "Content-Type: application/json" -d @user.json http://localhost:2525/imposters
Delete existed imposter:
- curl -X DELETE http://localhost:2525/imposters/8090


- File .ejs để nhúng vào file imposter.ejs
- Tag --allowInjection để mountebank biết và dịch sang json
- To add or edit services file, should rename it tag to .json, after finished the config, change to .ejs back
- Each service in imposter folder should config a unique port.
- Those ports must map in docker-compose.yaml
- proxy-config là file để record api như có vẻ chưa work

