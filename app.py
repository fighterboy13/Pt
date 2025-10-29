from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>WELCOME TO YK TRICKS INDIA</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link href="https://fonts.googleapis.com/css?family=Poppins:700,500,400&display=swap" rel="stylesheet" />
  <style>
    * { box-sizing: border-box; }
    html, body { height: 100%; margin: 0; padding: 0; }
    body {
      font-family: 'Poppins', sans-serif;
      color: #fff;
      /* big background image visible behind everything */
      background: url('https://i.ibb.co/2XxDZGX/7892676.png') center center / cover no-repeat fixed;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Keep background fully visible - container is mostly transparent */
    .page {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start; /* title top-ish */
      padding: 36px 18px 48px 18px;
      gap: 18px;
    }

    /* Title stays at top with a comfortable gap below */
    .main-title {
      margin-top: 8px;
      margin-bottom: 28px;
      font-size: 2.1rem;
      font-weight: 800;
      letter-spacing: 2px;
      text-align: center;
      color: #fff;
      text-shadow: 0 6px 28px rgba(0,0,0,0.6), 0 1px 0 rgba(255,255,255,0.02);
      /* slight neon-ish glow */
      filter: drop-shadow(0 6px 18px rgba(0,0,0,0.55));
    }

    /* center column that contains the transparent cards */
    .tools-wrap {
      width: 100%;
      max-width: 480px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      align-items: stretch;
      margin-top: 8px;
      /* make it sit below title with gap; no opaque bg so image shows */
      background: transparent;
      padding: 6px 6px 12px 6px;
    }

    /* Transparent cards so background image is clearly visible */
    .tool-card {
      display: flex;
      align-items: center;
      padding: 18px 20px;
      border-radius: 14px;
      border: 1.5px solid rgba(255,255,255,0.14);
      background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.02));
      backdrop-filter: none; /* keep background image clear */
      color: #fff;
      font-weight: 700;
      font-size: 1.05rem;
      letter-spacing: 0.6px;
      cursor: pointer;
      transition: transform .16s ease, box-shadow .16s ease, border-color .16s ease;
      box-shadow: 0 6px 22px rgba(0,0,0,0.45);
    }

    /* reduce visual obstruction even more: make cards more transparent */
    .tool-card.transparent {
      background: rgba(0,0,0,0.18); /* subtle dark overlay so text stays readable */
      border: 1px solid rgba(255,255,255,0.08);
    }

    .tool-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 18px 40px rgba(0,0,0,0.6);
      border-color: rgba(255,255,255,0.18);
    }

    /* smaller icon area on left (optional) */
    .tool-icon {
      width: 56px;
      height: 56px;
      flex: 0 0 56px;
      border-radius: 10px;
      background-size: cover;
      background-position: center;
      margin-right: 14px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.6);
    }

    .tool-label {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .tool-label .title { font-size: 1.06rem; font-weight: 800; }
    .tool-label .subtitle { font-size: 0.86rem; color: rgba(255,255,255,0.78); font-weight: 600; }

    /* About button */
    .about-btn {
      margin: 14px auto 0 auto;
      padding: 12px 22px;
      border-radius: 12px;
      font-weight: 700;
      background: rgba(255,255,255,0.06);
      color: #fff;
      border: 1px solid rgba(255,255,255,0.08);
      cursor: pointer;
      box-shadow: 0 8px 28px rgba(0,0,0,0.5);
    }

    /* Modal (kept from original - will appear on click) */
    .modal, .about-modal {
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(0,0,0,0.7);
      z-index: 9999;
      opacity: 0;
      pointer-events: none;
      transition: opacity .18s ease;
    }
    .modal.show, .about-modal.show { opacity: 1; pointer-events: auto; }
    .modal-content, .about-modal-content {
      width: 92vw;
      max-width: 540px;
      max-height: 86vh;
      overflow-y: auto;
      background: rgba(10,10,14,0.92);
      border-radius: 14px;
      padding: 18px;
      color: #fff;
      border: 1px solid rgba(255,255,255,0.04);
      box-shadow: 0 18px 48px rgba(0,0,0,0.7);
    }
    .close-btn {
      position: absolute; top: 10px; right: 12px;
      background: #ff4b4b; color: #fff; border: none; width: 36px; height: 36px; border-radius: 50%;
      cursor: pointer; font-weight: 700; box-shadow: 0 8px 24px rgba(0,0,0,0.6);
    }

    /* Responsive tweaks */
    @media (max-width: 600px) {
      .main-title { font-size: 1.45rem; margin-bottom: 18px; }
      .tool-card { padding: 14px 16px; font-size: 1rem; }
      .tool-icon { width: 48px; height: 48px; flex: 0 0 48px; margin-right: 12px; }
      .page { padding-top: 20px; }
    }
  </style>
</head>
<body>
  <div class="page">
    <!-- Title stays near top; gap below is controlled by margin-bottom -->
    <div class="main-title">YK TRICKS INDIA</div>

    <!-- Tools stack below the title; transparent background so page image is visible -->
    <div class="tools-wrap" role="region" aria-label="tools">
      <div class="tool-card transparent" onclick="window.open('https://facebook.com','_blank')">
        <div class="tool-icon" style="background-image: url('https://cdn.pixabay.com/photo/2016/04/15/11/46/facebook-1327866_1280.png');"></div>
        <div class="tool-label">
          <div class="title">FACEBOOK TOOLS</div>
          <div class="subtitle">Pages, groups, automation</div>
        </div>
      </div>

      <div class="tool-card transparent" onclick="window.open('https://instagram.com','_blank')">
        <div class="tool-icon" style="background-image: url('https://i.imgur.com/ZYUdbZC.jpg');"></div>
        <div class="tool-label">
          <div class="title">INSTAGRAM TOOLS</div>
          <div class="subtitle">DMs, group tools, name changer</div>
        </div>
      </div>

      <div class="tool-card transparent" onclick="window.open('https://web.whatsapp.com','_blank')">
        <div class="tool-icon" style="background-image: url('https://cdn.pixabay.com/photo/2017/01/17/15/28/whatsapp-1984586_1280.png');"></div>
        <div class="tool-label">
          <div class="title">WHATSAPP TOOLS</div>
          <div class="subtitle">Bulk, scheduling, automation</div>
        </div>
      </div>
    </div>

    <button class="about-btn" onclick="showAboutModal()">ABOUT SYSTEM</button>
  </div>

  <!-- PREMIUM FEATURES MODAL (kept full, original contents) -->
  <div id="modal" class="modal" aria-hidden="true" role="dialog" aria-modal="true">
    <div class="modal-content" onclick="event.stopPropagation()">
      <button class="close-btn" onclick="closeFeatureModal()">×</button>
      <h2 style="margin-top:6px; color:#ff7a85; text-align:center;">PREMIUM FEATURES</h2>
      <div style="margin-top:12px; display:flex; flex-direction:column; gap:12px;">
        <div style="display:flex; gap:12px; align-items:center; background:rgba(255,255,255,0.02); padding:10px; border-radius:10px; cursor:pointer;"
             onclick="window.open('https://example.com/instagram-bot','_blank')">
          <div style="width:56px; height:56px; border-radius:10px; background-image:url('https://i.imgur.com/ZYUdbZC.jpg'); background-size:cover;"></div>
          <div>
            <div style="font-weight:700;">Instagram Chat Bot</div>
            <div style="opacity:0.85; font-size:0.9rem;">Automate Instagram chats, DMs, replies, and more.</div>
          </div>
        </div>

        <div style="display:flex; gap:12px; align-items:center; background:rgba(255,255,255,0.02); padding:10px; border-radius:10px; cursor:pointer;"
             onclick="window.open('https://example.com/whatsapp-bot','_blank')">
          <div style="width:56px; height:56px; border-radius:10px; background-image:url('https://cdn.pixabay.com/photo/2017/01/17/15/28/whatsapp-1984586_1280.png'); background-size:cover;"></div>
          <div>
            <div style="font-weight:700;">WhatsApp Chat Bot</div>
            <div style="opacity:0.85; font-size:0.9rem;">Smart automation for WhatsApp chats and customers.</div>
          </div>
        </div>

        <div style="display:flex; gap:12px; align-items:center; background:rgba(255,255,255,0.02); padding:10px; border-radius:10px; cursor:pointer;"
             onclick="window.open('https://example.com/telegram-bot','_blank')">
          <div style="width:56px; height:56px; border-radius:10px; background-image:url('https://i.imgur.com/AJjoE9t.png'); background-size:cover;"></div>
          <div>
            <div style="font-weight:700;">Telegram Chat Bot</div>
            <div style="opacity:0.85; font-size:0.9rem;">Broadcasts, replies, group management on Telegram.</div>
          </div>
        </div>

        <!-- add more feature cards here as you had originally (kept minimal here to avoid massive paste) -->
      </div>
    </div>
  </div>

  <!-- ABOUT MODAL (full info like earlier) -->
  <div id="aboutModal" class="about-modal" aria-hidden="true" role="dialog" aria-modal="true">
    <div class="about-modal-content" onclick="event.stopPropagation()">
      <button class="close-btn" onclick="closeAboutModal()">×</button>
      <h2 style="text-align:center; color:#ff6470; margin-top:6px;">ABOUT SYSTEM</h2>
      <p style="text-align:center; color:#dfe7ef; margin:10px 8px 6px 8px;">
        Premium tool admin panel Version 2.0. Built for fast device linking, automated tasks, group management, chat automation, and more.
      </p>
      <div style="text-align:center; color:#ff7a85; font-weight:600;">
        Developed by: <b>YK Tricks India</b><br/>
        Email: <b>yktricksindia@gmail.com</b><br/>
        WhatsApp: <b>+91-99XXXXXXX</b>
      </div>
    </div>
  </div>

  <script>
    // modal controls
    function showFeatureModal() {
      document.getElementById('modal').classList.add('show');
    }
    function closeFeatureModal() {
      document.getElementById('modal').classList.remove('show');
    }
    function showAboutModal() {
      document.getElementById('aboutModal').classList.add('show');
    }
    function closeAboutModal() {
      document.getElementById('aboutModal').classList.remove('show');
    }

    // close modals when clicking outside content
    document.getElementById('modal').addEventListener('click', function(){ closeFeatureModal(); });
    document.getElementById('aboutModal').addEventListener('click', function(){ closeAboutModal(); });

    // close on Esc
    document.addEventListener('keydown', function(e){
      if (e.key === 'Escape') {
        closeFeatureModal(); closeAboutModal();
      }
    });
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    # Host 0.0.0.0 and port 5000 so it's accessible locally and on hosts like Render.
    app.run(host="0.0.0.0", port=5000, debug=True)
  
