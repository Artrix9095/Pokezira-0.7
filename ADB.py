from flask import Flask
db = Flask('')
db.route('/css/index.css')
def index():
  return open(
    './templates/index.css', 'r'
  ).read()
if True:
  db.run()