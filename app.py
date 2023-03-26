# print("Hello World")
from flask import Flask, render_template
# # # from flask import Flask

# # # app = Flask(__name__)
app = Flask(__name__)
# # # print(__name__)
@app.route("/")
def hello():
  return render_template('home.html')
#return "Hello World"

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)

#    # print("Inside the if now.")
