# print("Hello World")
from flask import Flask, render_template, jsonify
# # # from flask import Flask

# # # app = Flask(__name__)
app = Flask(__name__)
# # # print(__name__)
JOBS=[
  {
    'id': 1,
    'title':'Data Analyst',
    'location':'Delhi, India',
    'salary': 'Rs 10,00,000'
  },
  {
    'id': 2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary': 'Rs 15,00,000'
  },
  {
    'id': 3,
    'title':'Frontend Engineer',
    'location':'Remote',
    # 'salary': 'Rs 12,00,000'
  },
  {
    'id': 4,
    'title':'Backend Engineer',
    'location':'New York, USA',
    'salary': '$150,000'
  }
]
@app.route("/")
def hello():
  return render_template('home.html',
                         jobs=JOBS,company_name='JOB DEKHO')
#return "Hello World"
@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)

#    # print("Inside the if now.")
