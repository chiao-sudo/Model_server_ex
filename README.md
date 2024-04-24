## Intro
這是用來測試熟悉 model manager 的範例server.
將其包成docker即可獲得.tar檔上傳給model manager 的 upload model 相關 endpoint.

## Docker 指令
docker build -t  model_server_example .
docker save -o model_server_example.tar model_server_example

## Endpoint
endpoint 有兩個
1. '/' 回傳hello
2. '/predict' 回傳你的input 使用時可以用json={params}來傳遞進去