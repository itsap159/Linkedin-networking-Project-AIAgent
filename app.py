from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from start import generate

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    info = request.form['info']
    final = f"Name:{name}, Information:{info}"
    summary, profile_pic = generate(final)
    print(summary)
    print(profile_pic)
    return jsonify(
        {
            "summary_and_facts" : summary.to_dict(),
            "picture_url": profile_pic
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)