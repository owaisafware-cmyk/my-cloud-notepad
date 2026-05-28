from flask import Flask, request, render_template_string

app = Flask(__name__)

# Default cloud storage data
saved_text = "Welcome to your global notepad! Type anything here from any phone."
saved_link = "https://www.google.com"

# 🔒 YOUR SECRET PIN (Change "1234" to any password/code you want!)
SECRET_PIN = "1234"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My One Web</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* 💡 Clean CSS System Variables for 2026 Light & Dark Layouts */
        :root {
            --bg-gradient: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
            --card-bg: #ffffff;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --card-display-bg: #f8fafc;
            --border-color: #e2e8f0;
            --input-border: #cbd5e1;
            --input-bg: #ffffff;
            --btn-bg: #4f46e5;
            --btn-hover: #4338ca;
            --shadow: rgba(0, 0, 0, 0.04);
        }

        body.dark {
            --bg-gradient: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            --card-bg: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --card-display-bg: #0f172a;
            --border-color: #334155;
            --input-border: #475569;
            --input-bg: #1e293b;
            --btn-bg: #6366f1;
            --btn-hover: #4f46e5;
            --shadow: rgba(0, 0, 0, 0.4);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Plus Jakarta Sans', sans-serif;
            transition: background 0.25s ease, color 0.25s ease, border-color 0.25s ease;
        }

        body {
            background: var(--bg-gradient);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: var(--card-bg);
            width: 100%;
            max-width: 540px;
            border-radius: 24px;
            box-shadow: 0 12px 40px var(--shadow), 0 1px 3px rgba(0, 0, 0, 0.02);
            padding: 32px;
            border: 1px solid var(--border-color);
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 28px;
        }

        .header h2 {
            font-size: 24px;
            color: var(--text-primary);
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .theme-toggle-btn {
            background: var(--card-display-bg);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 8px 14px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            box-shadow: 0 2px 4px var(--shadow);
        }

        .theme-toggle-btn:hover {
            transform: translateY(-1px);
        }

        .display-card {
            background: var(--card-display-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 28px;
        }

        .section-title {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-secondary);
            font-weight: 700;
            margin-bottom: 6px;
        }

        .saved-text {
            font-size: 15px;
            color: var(--text-primary);
            line-height: 1.6;
            margin-bottom: 18px;
            white-space: pre-wrap;
        }

        .saved-link-wrapper {
            border-top: 1px solid var(--border-color);
            padding-top: 14px;
        }

        .saved-link {
            font-size: 14px;
            color: var(--btn-bg);
            text-decoration: none;
            font-weight: 500;
            word-break: break-all;
            display: inline-block;
        }

        .saved-link:hover {
            text-decoration: underline;
        }

        .form-title {
            font-size: 15px;
            color: var(--text-primary);
            font-weight: 600;
            margin-bottom: 16px;
        }

        .input-group {
            margin-bottom: 16px;
        }

        textarea, input[type="text"], input[type="password"] {
            width: 100%;
            background: var(--input-bg);
            border: 1px solid var(--input-border);
            border-radius: 12px;
            padding: 14px;
            font-size: 14px;
            color: var(--text-primary);
            outline: none;
        }

        textarea {
            min-height: 110px;
            resize: vertical;
        }

        textarea:focus, input[type="text"]:focus, input[type="password"]:focus {
            border-color: var(--btn-bg);
            box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.15);
        }

        textarea::placeholder, input[type="text"]::placeholder, input[type="password"]::placeholder {
            color: var(--text-secondary);
        }

        .btn-submit {
            width: 100%;
            background: var(--btn-bg);
            color: #ffffff;
            border: none;
            border-radius: 12px;
            padding: 14px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
        }

        .btn-submit:hover {
            background: var(--btn-hover);
            transform: translateY(-1px);
        }

        /* Security Feedback Boxes */
        .alert {
            padding: 12px 16px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 20px;
            text-align: center;
        }
        .alert-error {
            background: rgba(239, 68, 68, 0.15);
            color: #ef4444;
            border: 1px solid rgba(239, 68, 68, 0.2);
        }
        .alert-success {
            background: rgba(34, 197, 94, 0.15);
            color: #22c55e;
            border: 1px solid rgba(34, 197, 94, 0.2);
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="header">
            <h2>🌐 My One Web</h2>
            <button class="theme-toggle-btn" id="themeToggle" type="button">🌙 Dark Mode</button>
        </div>

        <!-- Displays security processing status message -->
        {% if error %}
            <div class="alert alert-error">{{ error }}</div>
        {% endif %}
        {% if success %}
            <div class="alert alert-success">{{ success }}</div>
        {% endif %}

        <div class="display-card">
            <div class="section-title">Saved Note</div>
            <div class="saved-text">{{ saved_text }}</div>
            
            <div class="saved-link-wrapper">
                <div class="section-title">Saved Link</div>
                {% if saved_link and saved_link != 'None' and saved_link != '' %}
                    <a href="{{ saved_link }}" target="_blank" class="saved-link">{{ saved_link }}</a>
                {% else %}
                    <span style="color: var(--text-secondary); font-size: 14px;">No link saved yet</span>
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

            <!-- 🔒 Password Input Field Added -->
            <div class="input-group">
                <input type="password" name="pin_data" placeholder="🔑 Enter Secret PIN to lock update" required>
            </div>
            
            <button type="submit" class="btn-submit">Save to Cloud</button>
        </form>
    </div>

    <script>
        const themeToggleBtn = document.getElementById('themeToggle');
        
        // Checks Device LocalStorage memory to preserve theme layout configuration
        if (localStorage.getItem('theme') === 'dark') {
            document.body.classList.add('dark');
            themeToggleBtn.innerHTML = '☀️ Light Mode';
        }

        themeToggleBtn.addEventListener('click', () => {
            document.body.classList.toggle('dark');
            
            if (document.body.classList.contains('dark')) {
                localStorage.setItem('theme', 'dark');
                themeToggleBtn.innerHTML = '☀️ Light Mode';
            } else {
                localStorage.setItem('theme', 'light');
                themeToggleBtn.innerHTML = '🌙 Dark Mode';
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, saved_text=saved_text, saved_link=saved_link, error="", success="")

@app.route('/save', methods=['POST'])
def save():
    global saved_text, saved_link
    user_pin = request.form.get('pin_data', '')
    
    # 🔐 Security Checkpoint: Validates user input request before updating live stream database variables
    if user_pin == SECRET_PIN:
        saved_text = request.form.get('text_data', '')
        saved_link = request.form.get('link_data', '')
        return render_template_string(HTML_TEMPLATE, saved_text=saved_text, saved_link=saved_link, error="", success="✨ Data successfully saved to the cloud!")
    else:
        return render_template_string(HTML_TEMPLATE, saved_text=saved_text, saved_link=saved_link, error="❌ Incorrect PIN! Update rejected.", success="")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
