from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    url = request.form['url']
    parts = url.split('&')
    highlighted_parts = []
    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
            highlighted_parts.append(f'<span style="color:blue;">{key}</span>={value}')
        else:
            highlighted_parts.append(part)
    highlighted_url = ' &\n'.join(highlighted_parts)
    return jsonify(highlighted_url=highlighted_url)

@app.route('/update_url', methods=['POST'])
def update_url():
    updated_text = request.form['updated_text']
    updated_url = updated_text.replace('\n', '').replace(' &', '&').strip()
    return jsonify(updated_url=updated_url)

if __name__ == "__main__":
    app.run(debug=True)
