from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

CASES = ['test1', 'test2', 'test3', 'test4']

template='''
<form action="info" method="post" name="checks">
  {% for c in cases %}
  <input type="checkbox" name="checks" value="{{c}}"> {{c}}<br>
  {% endfor %}
  <br>
  <input type="submit" value="Submit">
</form>
'''


@app.route("/TestCases")
def TestCases():
    return render_template_string(template, cases=CASES, title="Test Cases")

@app.route("/info", methods=['POST'])
def getinfo():
    print "HELLO!"
    if request.method == 'POST':
        print request.form.keys()
        #test = request.form['checks']
        test = request.form.getlist('checks')
        print test
        return 'Thanks!'
        return redirect('/')
    else:
        return 'NOT POST, but thanks!'
        return redirect('/')

app.run(debug=True)
