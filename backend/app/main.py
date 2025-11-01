from fastapi import FastAPI

from backend.model.Task import Task

app = FastAPI()


#TODO do the service
datas = [
    Task(id=1, name="aa", description="aaa")
]

@app.get("/")
def getTaskAll():
    return datas

@app.get("/{id}")
def getTaskById(id: int):
    for data in datas:
        if data.id == id:
            return data
    return {"mensagem": "Tarefa não encontrada"}

@app.post("/")
def postTask(task: Task):
    datas.append(task)
    return {"mensagem": "Tarefa adicionada com sucesso"}

@app.put("/{id}")
def putTask(id: int, task: Task):
    for i, data in enumerate(datas):
        if data.id == id:
            datas[i] = task
            return {"mensagem": "Tarefa atualizada com sucesso"}
    return {"mensagem": "Tarefa não encontrada"}

@app.delete("/")
def deleteAll():
    datas.clear()
    return {"mensagem": "Todas as tarefas foram deletadas"}

@app.delete("/{id}")
def deleteTask(id: int):
    global datas
    datas = [data for data in datas if data.id != id]
    return {"mensagem": f"Tarefa com id={id} deletada"}
