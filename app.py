from flask import Flask, request, jsonify

app = Flask(__name__)

# محتوى تجريبي للبحث
content = [
    {"title": "فتاوى", "url": "fatwa.html"},
    {"title": "دروس ومواعظ", "url": "lessons.html"},
    {"title": "خطب الجمعة", "url": "friday-sermons.html"},
    {"title": "صوتيات", "url": "audios.html"},
    {"title": "مرئيات", "url": "videos.html"},
    {"title": "استفسارتكم", "url": "messages.html"}
]

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    results = [item for item in content if query in item['title'].lower()]
    if results:
        return jsonify(results[0])
    else:
        return jsonify({"error": "لا يوجد نتائج للبحث"}), 404

if __name__ == '__main__':
    app.run(debug=True)
