from flask import Flask, request, render_template_string

app = Flask(__name__)

# Temporary cloud storage variables
saved_text = "Welcome to your global notepad! Type anything here from any phone."
saved_link = "https://www.google.com"

# The gorgeous new modern user interface design
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My One Web</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: #ffffff;
            width: 100%;
            max-width: 540px;
            border-radius: 24px;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.04), 0 1px 3px rgba(0, 0, 0, 0.02);
            padding: 32px;
            border: 1px solid rgba(255, 255, 255, 0.8);
        }

        .header {
            text-align: center;
            margin-bottom: 28px;
        }

        .header h2 {
            font-size: 24px;
            color: #1e293b;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .display-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 28px;
        }

        .section-title {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            font-weight: 700;
            margin-bottom: 6px;
        }

        .saved-text {
            font-size: 15px;
            color: #334155;
            line-height: 1.6;
            margin-bottom: 18px;
            white-space: pre-wrap;
        }

        .saved-link-wrapper {
            border-top: 1px solid #edf2f7;
            padding-top: 14px;
        }

        .saved-link {
            font-size: 14px;
            color: #4f46e5;
            text-decoration: none;
            font-weight: 500;
            word-break: break-all;
            display: inline-block;
            transition: color 0.2s;
        }

        .saved-link:hover {
            color: #3730a3;
            text-decoration: underline;
        }

        .form-title {
            font-size: 15px;
            color: #1e293b;
            font-weight: 600;
            margin-bottom: 16px;
        }

        .input-group {
            margin-bottom: 16px;
        }

        textarea, input[type="text"] {
            width: 100%;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            padding: 14px;
            font-size: 14px;
            color: #1e293b;
            outline: none;
            transition: all 0.2s ease;
        }

        textarea {
            min-height: 110px;
            resize: vertical;
        }

        textarea:focus, input[type="text"]:focus {
            border-color: #4f46e5;
            box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1);
        }

        textarea::placeholder, input[type="text"]::placeholder {
            color: #94a3b8;
        }

        .btn-submit {
            width: 100%;
            background: #4f46e5;
            color: #ffffff;
            border: none;
            border-radius: 12px;
            padding: 14px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
        }

        .btn-submit:hover {
            background: #4338ca;
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(79, 70, 229, 0.3);
        }

        .btn-submit:active {
            transform: translateY(0);
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="header">
            <h2>🌐 My One Web</h2>
        </div>

        <div class="display-card">
            <div class="section-title">Saved Note</div>
            <div class="saved-text">{{ saved_text }}</div>
            
            <div class="saved-link-wrapper">
                <div class="section-title">Saved Link</div>
                {% if saved_link and saved_link != 'None' and saved_link != '' %}
                    <a href="{{ saved_link }}" target="_blank" class="saved-link">{{ saved_link }}</a>
                {% else %}
                    <span style="color: #94a3b8; font-size: 14px;">No link saved yet</span>
                {% endif %}
            </div>
        </div>

        <form action="/save" method="POST">
            <div class="form-title">Update Dashboard Data</div>
            
            <div class="input-group">
                <textarea name="text_data" placeholder="Type your new note here..."></textarea>
            </div>
            
            <div class="input-group">
                <input type="text" name="link_data" placeholder="Paste a web link here...">
            </div>
            
            <button type="submit" class="btn-submit">Save to Cloud</button>
        </form>
    </div>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, saved_text=saved_text, saved_link=saved_link)

@app.route('/save', methods=['POST'])
def save():
    global saved_text, saved_link
    saved_text = request.form.get('text_data', '')
    saved_link = request.form.get('link_data', '')
    return render_template_string(HTML_TEMPLATE, saved_text=saved_text, saved_link=saved_link)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
