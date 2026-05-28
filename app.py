import os
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# This is our simple storage box where your text will be saved
SAVED_DATA = {
    "text": "Welcome to your global notepad! Type anything here from any phone.",
    "link": "https://www.google.com"
}

# The website design (HTML)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>My Personal Cloud</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f9; padding: 20px; text-align: center; }
        .container { max-width: 500px; background: white; padding: 20px; border-radius: 10px; margin: auto; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }
        textarea { width: 90%; height: 100px; padding: 10px; border-radius: 5px; border: 1px solid #ccc; }
        input[type="text"] { width: 90%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #0056b3; }
        .box { background: #e9ecef; padding: 15px; border-radius: 5px; text-align: left; margin-top: 20px; word-wrap: break-word; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🌐 My Global Cloud Notepad</h2>
        
        <div class="box">
            <strong>Saved Text:</strong><p>{{ data['text'] }}</p>
            <strong>Saved Link:</strong><p><a href="{{ data['link'] }}" target="_blank">{{ data['link'] }}</a></p>
        </div>

        <hr>
        <h3>Update Data from Any Device:</h3>
        <form action="/save" method="POST">
            <textarea name="user_text" placeholder="Type your new note here..."></textarea><br>
            <input type="text" name="user_link" placeholder="Paste a link here..."><br>
            <button type="submit">Save to Cloud</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # Show the webpage and pass our saved data to it
    return render_template_string(HTML_PAGE, data=SAVED_DATA)

@app.route('/save', methods=['POST'])
def save():
    # Grab whatever you typed on your phone screen
    SAVED_DATA["text"] = request.form.get("user_text")
    SAVED_DATA["link"] = request.form.get("user_link")
    # Take you back to the home page to see the updated data
    return redirect('/')

if __name__ == '__main__':
    # host='0.0.0.0' opens the website up to your whole home network/Wi-Fi
    app.run(host='0.0.0.0', port=5000, debug=True)
import os
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# This is our simple storage box where your text will be saved
SAVED_DATA = {
    "text": "Welcome to your global notepad! Type anything here from any phone.",
    "link": "https://www.google.com"
}

# The website design (HTML)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>My Personal Cloud</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f9; padding: 20px; text-align: center; }
        .container { max-width: 500px; background: white; padding: 20px; border-radius: 10px; margin: auto; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }
        textarea { width: 90%; height: 100px; padding: 10px; border-radius: 5px; border: 1px solid #ccc; }
        input[type="text"] { width: 90%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #0056b3; }
        .box { background: #e9ecef; padding: 15px; border-radius: 5px; text-align: left; margin-top: 20px; word-wrap: break-word; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🌐 My Global Cloud Notepad</h2>
        
        <div class="box">
            <strong>Saved Text:</strong><p>{{ data['text'] }}</p>
            <strong>Saved Link:</strong><p><a href="{{ data['link'] }}" target="_blank">{{ data['link'] }}</a></p>
        </div>

        <hr>
        <h3>Update Data from Any Device:</h3>
        <form action="/save" method="POST">
            <textarea name="user_text" placeholder="Type your new note here..."></textarea><br>
            <input type="text" name="user_link" placeholder="Paste a link here..."><br>
            <button type="submit">Save to Cloud</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE, data=SAVED_DATA)

@app.route('/save', methods=['POST'])
def save():
    SAVED_DATA["text"] = request.form.get("user_text")
    SAVED_DATA["link"] = request.form.get("user_link")
    return redirect('/')

if __name__ == '__main__':
    # NEW: This line asks the cloud provider what port to use. If none exists, it defaults to 5000.
    cloud_port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=cloud_port)