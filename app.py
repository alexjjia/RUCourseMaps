from flask import Flask, request, render_template, url_for
#from rucoursemaps import getLists

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html") # Return form
    if request.method == 'POST':
        deptnum = request.form.get('deptnum')
        print "DEPTNUM"
        print deptnum
        classes, prereqs = "a", "b" #getLists(deptnum)
        return render_template("graph.html",
                               classes=classes,
                               prereqs=prereqs)


if __name__ == '__main__':
    app.run(debug=True)
