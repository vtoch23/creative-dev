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
        "title": "Six graphic design skills for a career change into software development",
        "description": "Considering a career change into software development? You may already have a lot of skills that will come in handy.",
        "image": "https://images.unsplash.com/photo-1626785774573-4b799315345d?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "link": "https://www.thoughtworks.com/en-gb/insights/blog/careers-at-thoughtworks/graphic-design-skills-career-change-software-development"
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
    },
    {
        "title": "Escape routes from dead end Design careers",
        "description": "Entering the design profession is sometimes like love at first sight, but it can also be something you simply want to do and learn to respect. ",
        "image": "https://miro.medium.com/v2/resize:fit:490/format:webp/0*ENwrYObZ4eJyIZrf.gif",
        "link": "https://uxplanet.org/escape-routes-from-dead-end-design-careers-c6886231c9d"
    },
    {
        "title": "Transition from Graphic Designer to Web Development: Navigating the Creative Shift",
        "description": "PGraphic designers, with their innate creativity and design sensibilities, are finding a natural transition into the realm of web development.",
        "image": "https://cdn.prod.website-files.com/63ffc13801c4ab3d3423fa79/655c98de7873e32172e20921_Screenshot%202023-11-21%20194130.png",
        "link": "https://www.skillspire.net/post/transition-from-graphic-designer-to-web-development-navigating-the-creative-shift"
    },
     {
        "title": "My career journey from graphic designer to software engineer",
        "description": "By Karen Evans, Engineer II, Development @ Wavelo.",
        "image": "https://miro.medium.com/v2/resize:fit:720/format:webp/1*5ObgPwaO2I_6k6uOEq8f-g.png",
        "link": "https://storiesfromtheherd.com/my-career-journey-from-graphic-designer-to-software-engineer-d3d1fffea1bb"
    }
]

@app.route('/')
def home():
    return render_template('home.html', articles=articles)

@app.route('/my-work')
def my_work():
    return render_template('myjourney.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)