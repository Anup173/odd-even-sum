from flask import redirect, request, render_template, url_for, Flask
from fib import fb

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/result", methods=["POST"])
def result():
    u_input1 = request.form.get("num1")
    u_input2 = request.form.get("num2")
     u_input3 = request.form.get("num3")
    u_input4 = request.form.get("num4")  
   u_input5 = request.form.get("num5")
    if not u_input:
        return redirect("/")
    odd = odd_sum(int(u_input1,u_input2,u_input3,u_input4,u_input5))
    even=even_sum(int(u_input1,u_input2,u_input3,u_input4,u_input5))
    return render_template("result.html", fib_num = number, usr_input = u_input)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
