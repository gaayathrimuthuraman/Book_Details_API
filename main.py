from flask import Flask, jsonify

app = Flask(__name__)

books_data = {
    "The Lost Kingdom": {
        "author": "John Smith",
        "price": 22.50,
        "genre": "Historical Fiction",
        "rating": 4.3
    },
    "Realm of Dreams": {
        "author": "Jane Doe",
        "price": 17.99,
        "genre": "Fantasy",
        "rating": 4.6
    },
    "In the Footsteps of Giants": {
        "author": "Mark Johnson",
        "price": 27.99,
        "genre": "Non-Fiction",
        "rating": 4.1
    },
    "Whispers in the Shadows": {
        "author": "Emily White",
        "price": 19.99,
        "genre": "Young Adult",
        "rating": 4.4
    },
    "Beyond the Stars": {
        "author": "Alex Brown",
        "price": 31.99,
        "genre": "Science",
        "rating": 4.9
    },
    "The Enigma Files": {
        "author": "Michael Johnson",
        "price": 15.99,
        "genre": "Mystery",
        "rating": 4.2
    },
    "Eternal Love": {
        "author": "Sarah Davis",
        "price": 29.50,
        "genre": "Romance",
        "rating": 4.8
    },
    "Chasing Shadows": {
        "author": "Robert Turner",
        "price": 24.99,
        "genre": "Thriller",
        "rating": 4.7
    },
    "Dystopian Dreams": {
        "author": "Emma White",
        "price": 18.99,
        "genre": "Dystopian",
        "rating": 4.0
    },
    "The Quest for Atlantis": {
        "author": "Daniel Green",
        "price": 32.99,
        "genre": "Adventure",
        "rating": 4.5
    },
    "Sunset Serenade": {
        "author": "Grace Brown",
        "price": 20.50,
        "genre": "Contemporary",
        "rating": 4.4
    },
    "Beyond the Horizon": {
        "author": "Ryan Miller",
        "price": 26.99,
        "genre": "Biography",
        "rating": 4.3
    },
    "Galactic Odyssey": {
        "author": "Sophia Taylor",
        "price": 23.75,
        "genre": "Science Fiction",
        "rating": 4.6
    },
    "Laugh Out Loud": {
        "author": "Jack Robinson",
        "price": 14.50,
        "genre": "Humor",
        "rating": 4.1
    },
    "Echoes of Eternity": {
        "author": "Olivia Davis",
        "price": 30.99,
        "genre": "Historical",
        "rating": 4.9
    }
}

@app.route('/book/<string:book_name>', methods=['GET'])
def get_book_details(book_name):
    if book_name in books_data:
        return jsonify(books_data[book_name])
    else:
        return jsonify({"error": "Book not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
