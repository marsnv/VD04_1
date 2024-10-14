from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


posts = []
@app.route('/blog/', methods=['GET', 'POST'])
def blog():
    if request.method == 'POST':
        post_content = request.form.get('content')
        if post_content:
            posts.append(post_content)
        return redirect(url_for('blog'))
    return render_template('blog.html', posts=posts)

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

if __name__ == '__main__':
    app.run(debug=True)