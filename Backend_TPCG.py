from flask import Flask, render_template

app = Flask(__name__)

# Route để hiển thị template Frontend_TPCG.html
@app.route('/')
def home():
    return render_template('Frontend_TPCG.html')  # Flask sẽ tìm tệp HTML trong thư mục 'templates'

if __name__ == '__main__':
    app.run(debug=True)
