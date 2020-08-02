from flask import Flask, redirect, request, render_template
import sqlite as sqlite

host = 'http://127.0.0.1:5000'

app = Flask(__name__, template_folder='templates')

#Only render the index.html template
@app.route('/')
def form():
    return render_template('index.html')

#Get URL from html form and provide the short url for it
@app.route('/', methods = ['POST']) 
def main(): 
   url = request.form.get("text")
   return render_template('response.html', url_from=host + str(sqlite.get_shortUrl_by_url(url)) )
      
#Check '/<URL>' in short url's to make redirect
@app.route('/<URL>', methods = ['GET']) 

def redir(URL): 
   print(URL)
   if request.method == 'GET':
      return redirect(sqlite.get_url_by_shortUrl("/" + URL), code=302)
  

if __name__ == '__main__':
    app.run(debug=True)

