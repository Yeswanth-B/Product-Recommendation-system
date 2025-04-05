from flask import Flask, render_template, request

app = Flask(__name__)

# Simple rule-based recommender
def recommend_product(form_data):
    product_type = form_data['product_type']
    budget = int(form_data['budget'])
    usage = form_data['usage']
    brand = form_data['brand']

    if product_type == 'Laptop':
        if budget < 400:
            return f"{brand} Chromebook - Good for light {usage} tasks"
        elif 400 <= budget <= 1000:
            return f"{brand} Mid-range Laptop - Balanced for {usage}"
        else:
            return f"{brand} High-end Laptop - Excellent for {usage}"
    else:
        if budget < 300:
            return f"{brand} Budget Smartphone - Basic {usage}"
        elif 300 <= budget <= 800:
            return f"{brand} Mid-range Smartphone - Great for {usage}"
        else:
            return f"{brand} Flagship Smartphone - Top-tier {usage} experience"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recommendation = recommend_product(request.form)
        return render_template('result.html', recommendation=recommendation)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
