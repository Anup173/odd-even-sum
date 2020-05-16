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
  
    odd =odd_sum(int(u_input1),int(u_input2),int(u_input3),int(u_input4),int(u_input5))
    even=even_sum(int(u_input1),int(u_input2),int(u_input3),int(u_input4),int(u_input5))
    return render_template("result.html", sum_odd = odd, sum_even=even)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
