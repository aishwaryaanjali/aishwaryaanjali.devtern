from flask import Flask, render_template ,url_for, request, redirect
import random
app = Flask(__name__) 
tasks=[
    {
        'id':1,
        'name':'TASK1',
        'checked':False

    }
]
@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
    if(request.method=="POST"):
        task_name = request.form["task_name"]
        task_id=random.randint(1,1000)
        tasks.append({
            'id':task_id,
            'name':task_name,
            'checked':False
        })
        return redirect(url_for("home"))
    return render_template("index.html",items=tasks)
@app.route("/checked/<int:task_id>",methods=["POST"])
def checked_task(task_id):
    for task in tasks:
        if task['id']==task_id:
            task['checked']= not task['checked']
            break
    return redirect(url_for("home"))
@app.route("/delete/<int:task_id>",methods=["POST"])
def delete_task(task_id):
    global tasks
    for task in tasks:
        if task['id']==task_id:
            tasks.remove(task)
    return redirect(url_for("home"))
if __name__=="__main__":
    app.run(debug=True)