from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>WELCOME TO YK TRICKS INDIA</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css?family=Poppins:700,500,400" rel="stylesheet">
  <style>
    body {
      margin: 0;
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(120deg, #232526 0%, #414345 100%);
      color: #fff;
      min-height: 100vh;
    }
    .main-title {
      text-align: center;
      font-size: 2.1rem;
      font-weight: 900;
      letter-spacing: 2px;
      margin: 36px 0 8px 0;
      background: linear-gradient(90deg,#ffe259,#ffa751,#43cea2,#185a9d);
      background-clip: text;
      -webkit-background-clip: text;
      color: transparent;
      text-shadow: 0 2px 18px #000a;
    }
    .premium-box {
      max-width: 390px;
      margin: 0 auto 28px auto;
      border-radius: 18px;
      position: relative;
      box-shadow: 0 8px 32px 0 rgba(31,38,135,0.18);
      background: linear-gradient(90deg, #f857a6 0%, #ff5858 40%, #fceabb 100%);
      cursor: pointer;
      padding: 28px 18px 26px 18px;
      text-align: center;
      font-weight: 800;
      font-size: 1.22rem;
      color: #fff;
      letter-spacing: 1.5px;
      border: 3px solid #ff3335;
      overflow: hidden;
      margin-top: 18px;
      margin-bottom: 18px;
      transition: box-shadow .15s, background .18s;
      animation: glow 1.8s linear infinite alternate;
    }
    @keyframes glow {
      0% { box-shadow: 0 3px 30px #faadb1a5; }
      100% { box-shadow: 0 8px 50px #fdc2bca5; }
    }
    .premium-box .underline {
      display:block;
      width:74%;
      margin:14px auto 0 auto;
      height:5px;
      border-radius:9px;
      background: linear-gradient(90deg,#fa5c64 30%,#ffe0bb 100%);
      box-shadow:0 1px 12px #fff2d7;
      animation: slide 2.5s infinite linear alternate;
    }
    @keyframes slide {
      0% { width: 70%; }
      100% { width: 95%; }
    }
    .panel {
      max-width: 420px;
      margin: 0 auto;
      padding: 16px 8px 30px 8px;
      border-radius: 22px;
      box-shadow: 0 8px 48px 0 rgba(31,38,135,0.12);
      background: url('https://i.ibb.co/2XxDZGX/7892676.png') center center/cover no-repeat;
      margin-bottom: 30px;
      position: relative;
      overflow: hidden;
      min-height: 570px;
    }
    .feature-row {
      display: flex; flex-direction: column; gap: 24px;
      margin-top: 4px;
    }
    .feature-card {
      border-radius: 16px;
      box-shadow: 0 3px 24px 0 rgba(22,44,120,0.16);
      overflow: hidden;
      cursor: pointer;
      transition: transform .12s, box-shadow .15s;
      position: relative;
      display: flex;
      align-items: flex-end;
      min-height: 116px;
      aspect-ratio: 15/7;
      border: 2px solid #f8f9fcee;
    }
    .feature-card:hover {
      transform: scale(1.044);
      box-shadow: 0 8px 32px 0 rgba(44,60,120,0.22);
      border: 2px solid #19f58c88;
    }
    .fb-card {
      background: url('https://cdn.pixabay.com/photo/2016/04/15/11/46/facebook-1327866_1280.png') center center/cover no-repeat, linear-gradient(135deg,#0866ff55, #fff0);
    }
    .ig-card {
      background: url('https://i.imgur.com/ZYUdbZC.jpg') center center/cover no-repeat, linear-gradient(135deg,#e1306c99,#fff0);
    }
    .wa-card {
      background: url('https://cdn.pixabay.com/photo/2017/01/17/15/28/whatsapp-1984586_1280.png') center center/cover no-repeat, linear-gradient(135deg,#25d366cc,#fff0);
    }
    .feature-label {
      z-index: 2;
      margin: 0 0 19px 16px;
      font-size: 1.15rem;
      font-weight: 700;
      text-shadow: 0 2px 8px #253c;
      padding: 8px 22px;
      border-radius: 24px;
      background: rgba(30,30,30,0.16);
      color: #fff;
      transition: background .22s;
      border: 2px solid #fff0;
    }
    .fb-card .feature-label { background: rgba(9, 86, 255, .78);}
    .ig-card .feature-label { background: rgba(225, 48, 108, .78);}
    .wa-card .feature-label { background: rgba(37, 211, 102, .77);}
    /* Features modal */
    .modal, .about-modal {
      position: fixed; z-index: 98; top: 0; left: 0; width: 100vw; height: 100vh;
      display: flex; align-items: center; justify-content: center;
      background: rgba(22,28,39,0.87); transition: opacity .15s;
    }
    .modal-content, .about-modal-content {
      background: linear-gradient(112deg, #f2f4f6 60%, #ffe5e2 100%);
      border-radius: 17px;
      max-width: 450px;
      width: 98vw;
      max-height: 85vh;
      overflow-y: auto;
      box-shadow: 0 10px 48px 0 #222c478f;
      padding: 18px 8px 12px 8px;
      position: relative;
      animation: fadeIn .2s linear;
    }
    .close-btn {
      position: absolute; top: 8px; right: 11px;
      background: #ef414d; color: #fff;
      border-radius: 50%;
      font-size: 1.3rem; width: 31px; height: 31px;
      display: flex;align-items: center;justify-content: center;
      cursor: pointer; border: none;transition: background .16s;
    }
    .close-btn:hover { background: #23262d; }
    .modal-title {
      text-align:center;color:#333;margin:5px 0 15px 0;font-weight:700;letter-spacing:1px;
      font-size:1.27rem;
    }
    .feature-list-grid { display:flex; flex-direction:column; gap:17px;}
    .modal-list-card {
      display: flex; align-items: center;
      border-radius: 13px; box-shadow: 0 2px 14px #1c1e2840;
      overflow: hidden; background: #fff;
      min-height: 78px; cursor: pointer;
      transition: box-shadow .14s, border .18s;
      border: 2px solid #fff8; position: relative;
      margin-bottom: 5px;
    }
    .modal-list-card:hover {
      border: 2px solid #2bcffe;
      box-shadow: 0 8px 24px #37bde254;
    }
    .list-card-bg {
      min-width: 62px; width: 62px; height: 62px;
      object-fit: cover; border-right: 5px solid #f6f6fa;
      background-size: cover; background-position: center; background-repeat: no-repeat;
      border-radius: 14px 0 0 14px;
    }
    .list-card-content {
      padding: 8px 12px 8px 18px; flex: 1; color: #232;
      display: flex; flex-direction: column; justify-content: center;
    }
    .list-card-title {
      font-size: 1.09rem; font-weight: 600;
      margin-bottom: 6px;
    }
    .list-card-desc {
      font-size: .93rem; color: #555b;
    }
    .about-btn {
      background: linear-gradient(90deg, #005aff 0%, #f857a6 100%);
      border-radius:11px;
      padding:12px 23px;
      font-weight:900;
      font-size:1.03rem;
      color:#fff;letter-spacing:1px;
      margin:0 auto;display:block;text-align:center;
      border:none;cursor:pointer;outline: none;
      margin-bottom:22px;margin-top:8px;
      box-shadow:0 2px 15px #4456be36;
      transition:background .12s;
    }
    .about-btn:hover {background:linear-gradient(90deg, #005aff 20%, #f857a6 100%);}
    /* About modal styles */
    .about-modal-content {
      padding:22px 18px 19px 18px;
      text-align:center;
      font-family:'Poppins',sans-serif;
    }
    .about-modal-content h2 {
      font-size:1.15rem;font-weight:700;margin-bottom:11px;letter-spacing:1px;
      background:linear-gradient(90deg,#0080ff,#fa5c68,#ffdbb9);background-clip:text;-webkit-background-clip:text;color:transparent;
    }
    .about-modal-content .info-txt {
      margin-bottom:14px;font-size:.98rem;color:#333;
    }
    .about-modal-content .contacts {
      font-size:.97rem;color:#193d98;margin:0 0 9px 0;
      word-break:break-all;
    }
    @keyframes fadeIn {
      from {opacity:0; transform:translateY(30px);}
      to {opacity:1; transform:translateY(0);}
    }
    @media (max-width: 700px) {
      .panel { min-height: 740px;}
    }
    @media (max-width: 430px) {
      .main-title { font-size: 1.08rem; }
      .panel { min-height:97vh; }
    }
  </style>
</head>
<body>
<div class="main-title">WELCOME TO YK TRICKS INDIA</div>
<div class="premium-box" onclick="showFeatureModal()">
  EXPLORE PREMIUM FEATURES
  <span class="underline"></span>
</div>
<div class="panel">
  <div class="feature-row">
    <div class="feature-card fb-card"><span class="feature-label">FACEBOOK TOOLS</span></div>
    <div class="feature-card ig-card"><span class="feature-label">INSTAGRAM TOOLS</span></div>
    <div class="feature-card wa-card"><span class="feature-label">WHATSAPP TOOLS</span></div>
  </div>
</div>
<button class="about-btn" onclick="showAboutModal()">ABOUT SYSTEM</button>

<!-- PREMIUM FEATURES MODAL -->
<div id="modal" class="modal" style="display:none;">
  <div class="modal-content">
    <button class="close-btn" onclick="closeFeatureModal()">×</button>
    <div class="modal-title">PREMIUM FEATURES</div>
    <div class="feature-list-grid">
      <div class="modal-list-card" onclick="window.open('https://example.com/instagram-bot','_blank')">
        <div class="list-card-bg" style="background-image:url('https://i.imgur.com/ZYUdbZC.jpg');"></div>
        <div class="list-card-content">
          <div class="list-card-title">Instagram Chat Bot</div>
          <div class="list-card-desc">Automate Instagram chats, DMs, replies, and more.</div>
        </div>
      </div>
      <!-- (Other modal cards remain same) -->
    </div>
  </div>
</div>

<!-- ABOUT MODAL -->
<div id="aboutModal" class="about-modal" style="display:none;">
  <div class="about-modal-content">
    <button class="close-btn" onclick="closeAboutModal()">×</button>
    <h2>ABOUT SYSTEM</h2>
    <div class="info-txt">Premium tool admin panel Version 2.0. Built for fast device linking, automated tasks, group management, chat automation, and more.</div>
    <div class="contacts">
      Developed by: <b>YK Tricks India</b><br>
      Contact: <b>yktricksindia@gmail.com</b><br>
      WhatsApp: <b>+91-99XXXXXXX</b><br>
      Instagram: <b>@yktricksindia</b><br>
      Website: <b>yktricksindia.com</b>
    </div>
  </div>
</div>

<script>
function showFeatureModal() {
  document.getElementById('modal').style.display = 'flex';
  document.body.style.overflowY = "hidden";
}
function closeFeatureModal() {
  document.getElementById('modal').style.display = 'none';
  document.body.style.overflowY = "auto";
}
function showAboutModal() {
  document.getElementById('aboutModal').style.display = 'flex';
  document.body.style.overflowY = "hidden";
}
function closeAboutModal() {
  document.getElementById('aboutModal').style.display = 'none';
  document.body.style.overflowY = "auto";
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
        
