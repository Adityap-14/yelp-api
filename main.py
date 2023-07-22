from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search = request.form['search']
        location = request.form['location']
        

        headers = {
            'Authorization': 'Bearer on7EtcpxnWoyLf5AFgNnz2dfIP8d3HfsjHI-9d-3wwWyVx5hQbvSzgeU0U86ykjpzmEKy0gDahgFX02sxZ99Pg2AklU3gJTMhomo8to5vaBSDTc7RdS8lCUYxgC7ZHYx',
        }

        params = {
            'term': search,
            'location': location,
            
        }

        response = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=params)
        data = response.json()

        results = []
        for business in data['businesses']:
            title = business['name']
            phone = business.get('phone', '')
            url = business.get('url', '')
            address = ', '.join(business['location'].get('display_address', []))
            city = business['location'].get('city', '')
            postalCode = business['location'].get('zip_code', '')
            state = business['location'].get('state', '')
            countryCode = business['location'].get('country', '')
            rating = business.get('rating', '')
            review_count = business.get('review_count', '')
            categories = ', '.join([category['title'] for category in business['categories']])
            image_url = business.get('image_url', '')
            latitude = business['coordinates'].get('latitude', '')
            longitude = business['coordinates'].get('longitude', '')

            results.append({
                'title': title,
                'phone': phone,
                'url': url,
                'address': address,
                'city': city,
                'postalCode': postalCode,
                'state': state,
                'countryCode': countryCode,
                'rating': rating,
                'review_count': review_count,
                'categories': categories,
                'image_url': image_url,
                'latitude': latitude,
                'longitude': longitude,})

        return render_template('results.html', results=results)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
