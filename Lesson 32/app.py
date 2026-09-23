from flask import Flask, render_template
from models import products

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/products")
def product_list():
    available_products = products.find({ "is_available": True})
    total = products.count_documents({ "is_available": True})

    return render_template('products.html', products=available_products, total=total)

if __name__ == "__main__":
    app.run(debug=True)