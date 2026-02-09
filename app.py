from flask import Flask, render_template

app = Flask(__name__)

articles = [
    {
        "title": "Why Coding Can Be a Great Career for Creatives",
        "description": "How creative thinking and software development complement each other in modern careers.",
        "image": "https://images.unsplash.com/photo-1492724441997-5dc865305da7",
        "link": "https://blog.makersacademy.com/why-coding-can-be-a-great-career-for-creatives-8e0d56f9d285"
    },
    {
        "title": "Creative Software Development",
        "description": "Exploring how creativity influences modern software engineering practices.",
        "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
        "link": "https://tsh.io/blog/creative-software-development"
    },
    {
        "title": "Creativity in Software Engineering",
        "description": "Why creativity is a critical skill for developers in the AI age.",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "link": "https://newsletter.getdx.com/p/creativity-in-software-engineering"
    },
    {
        "title": "Tech Lead Journal – Creativity in Software",
        "description": "Podcast discussion on creativity and engineering leadership.",
        "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085",
        "link": "https://techleadjournal.dev/episodes/161/"
    },
    {
        "title": "Dynamics of Creativity in Software Development",
        "description": "Understanding creativity as a driver of innovation in software teams.",
        "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
        "link": "https://www.interinnova.com/blogposts/the-dynamics-of-creativity-in-software-development"
    }
]

@app.route('/')
def home():
    return render_template('index.html', articles=articles)

@app.route('/my-work')
def my_work():
    return render_template('mywork.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)