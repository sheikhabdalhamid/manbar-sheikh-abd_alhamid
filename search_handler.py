import json
import sys

# محتوى تجريبي للبحث
content = [
    {"title": "فتاوى", "url": "fatwa.html"},
    {"title": "دروس ومواعظ", "url": "lessons.html"},
    {"title": "خطب الجمعة", "url": "friday-sermons.html"},
    {"title": "صوتيات", "url": "audios.html"},
    {"title": "مرئيات", "url": "videos.html"},
    {"title": "استفسارتكم", "url": "messages.html"}
]

def search(query):
    query = query.lower()
    results = [item for item in content if query in item['title'].lower()]
    if results:
        return json.dumps(results[0])
    else:
        return json.dumps({"error": "لا يوجد نتائج للبحث"})

if __name__ == '__main__':
    query = sys.argv[1]
    print(search(query))
