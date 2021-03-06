from flask import Flask, render_template
app = Flask(__name__)
from sampling import *
import histogram
text = handle_input('text.txt')
histogram = histogram.Hi
weighted_arr = weighted_hist(histogram.tuple)
print(weighted_arr)

@app.route('/<int:population>')
def index():
    return render_template('hello.html', histogram=histogram)

if __name__ == '__main__':
    app.run(debug=True)
