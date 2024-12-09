from django.http.response import HttpResponse
from django.shortcuts import render

data = {
    "blogs" : [
        {
            "id": 1,
            "title": "Sifirdan ileri Seviye Web Gelistirme",
            "image": "1.jpg",
            "is_active": True,
            "is_home": True,
            "description" : "Tam aradiginiz kurs"
        },
        {
            "id": 2,
            "title": "Python ile sifirdan ileri seviye programlama",
             "image": "2.jpg",
            "is_active": True,
            "is_home": False,
            "description" : "Tam aradiginiz kurs"
        },
        {
            "id": 3,
            "title": "Mobil Uygulama Gelistirme Kursu",
             "image": "3.jpg",
            "is_active": True,
            "is_home": True,
            "description" : "Tam aradiginiz kurs"
        },
        {
            "id": 4,
            "title": "Sifirdan ileri seviye Excel kursu",
             "image": "4.jpg",
            "is_active": False,
            "is_home": True,
            "description" : "Tam aradiginiz kurs"
        },
        {
            "id": 5,
            "title": "Etik Hacker olma kursu",
             "image": "5.jpg",
            "is_active": True,
            "is_home": True,
            "description" : "Tam aradiginiz kurs"
        }
        
    ]
}

# Create your views here.

def index(request):
    context = {
        "blogs": data["blogs"] #
    }
    return render(request, "blog/index.html",context)

def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/blogs.html",context)

def blog_details(request, id):
    # blogs = data["blogs"]
    # selectedBlog = None
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog
    blogs = data["blogs"]
    selectedBlog = [blog for blog in blogs if blog["id"] == id][0] 
    return render(request, "blog/blog-details.html", {
        "blog": selectedBlog
    })