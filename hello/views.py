# hello/views.py

from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Test Web Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #007bff;
                color: white;
                padding: 10px;
                text-align: center;
            }
            main {
                padding: 20px;
                text-align: center;
            }
            footer {
                background-color: #007bff;
                color: white;
                padding: 10px;
                text-align: center;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to the Django Test Web Application!</h1>
        </header>
        <main>
            <p>This is a simple test page with some styling applied.</p>
        </main>
        <footer>
            <p>&copy; 2024 Django Test Application</p>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html)


# Create your views here.
