from flask import Flask, redirect, request, render_template
import logic as logic


app = Flask(__name__, template_folder='templates')

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods = ['POST']) 
def main(): 
   url = request.form.get("text")
   print(url)
   return redirect('/', code=302)
      

@app.route('/<URL>', methods = ['GET']) 

def redir(URL): 

   logic.get_short_url(logic.url, logic.short_url, URL) 

   if request.method == 'GET':
      return redirect(logic.get_url(logic.url, logic.short_url, URL), code=302)
  

if __name__ == '__main__':
    app.run(debug=True)

#need to implement mapping, and find a way to deal with input url for destination