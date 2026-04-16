from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form9', methods=['GET', 'POST'])
def form9():
    if request.method == 'POST':
        sana = request.form.get('sana')
        vaqt = request.form.get('vaqt')
        return f"<h2>Tanlangan sana: {sana}<br>Vaqt: {vaqt}</h2><br><a href='/'>Orqaga</a>"
    return render_template('form9.html')

if __name__ == '__main__':
    app.run(debug=True)
