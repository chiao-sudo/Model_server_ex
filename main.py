from fastapi import FastAPI, Body, Request

# 创建FastAPI应用
app = FastAPI()

# 定义根端点
@app.get("/")
async def root():
    # 记录日志消息
    print("Hello Docker!")
    return {"message": "Hello World"}

# 定义predict端点
@app.post("/predict/")
async def predict(request: Request, features = Body()):
    # 打印参数
    print("Predict params:", features)
    # 返回预测结果
    return {"prediction": f"Your input is {features}"}
