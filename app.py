from flask import Flask, redirect, request, render_template
import logic as logic

host = 'http://127.0.0.1:5000'

app = Flask(__name__, template_folder='templates')

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods = ['POST']) 
def main(): 
   url = request.form.get("text")
   return render_template('response.html', url_from=host + logic.get_short_url(logic.maps, url))
      

@app.route('/<URL>', methods = ['GET']) 

def redir(URL): 

   logic.get_short_url(logic.maps, URL) 

   if request.method == 'GET':
      return redirect(logic.get_url(logic.maps, URL), code=302)
  

if __name__ == '__main__':
    app.run(debug=True)

#need to implement mapping, and find a way to deal with input url for destination