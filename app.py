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
      min-height: 50vh;
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
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>WELCOME TO YK TRICKS INDIA</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link href="https://fonts.googleapis.com/css?family=Poppins:700,500,400&display=swap" rel="stylesheet" />
  <style>
    /* Reset and typography */
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      font-family: 'Poppins', sans-serif;
      color: #eee;
      background: url('https://i.ibb.co/2XxDZGX/7892676.png') no-repeat center center fixed;
      background-size: cover;
      min-height: 100vh;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    /* Overlay to darken background image */
    body::before {
      content: "";
      position: fixed;
      top:0; left:0; right:0; bottom:0;
      background: rgba(10,10,10,0.55);
      z-index: 0;
      pointer-events: none;
    }
    .container {
      position: relative;
      z-index: 1;
      max-width: 480px;
      margin: 40px auto 50px;
      padding: 24px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      backdrop-filter: blur(16px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
      border: 1px solid rgba(255, 255, 255, 0.18);
    }
    .main-title {
      font-size: 2rem;
      font-weight: 800;
      letter-spacing: 2.3px;
      text-align: center;
      margin-bottom: 26px;
      color: #fff;
      text-shadow: 0 0 10px rgba(255,255,255,0.2);
    }
    .premium-box {
      background: linear-gradient(90deg, #ff416c, #ff4b2b);
      color: white;
      padding: 17px 0;
      border-radius: 14px;
      font-weight: 700;
      font-size: 1.23rem;
      text-align: center;
      cursor: pointer;
      user-select: none;
      transition: background 0.3s ease;
      box-shadow: 0 6px 16px #ff4b2baa;
      margin-bottom: 28px;
      letter-spacing: 1.2px;
    }
    .premium-box:hover {
      background: linear-gradient(90deg, #ff4b2b, #ff416c);
      box-shadow: 0 8px 28px #ff416ccc;
    }
    .feature-row {
      display: flex;
      flex-direction: column;
      gap: 22px;
    }
    .feature-card {
      position: relative;
      border-radius: 20px;
      height: 110px;
      display: flex;
      align-items: center;
      padding-left: 24px;
      cursor: pointer;
      background-size: contain;
      background-repeat: no-repeat;
      background-position: left center;
      box-shadow: 0 6px 20px rgba(255,255,255,0.1);
      transition: transform 0.22s ease, box-shadow 0.28s ease;
      color: #fff;
      font-weight: 700;
      font-size: 1.15rem;
      letter-spacing: 1px;
      text-shadow: 0 2px 7px rgba(0,0,0,0.65);
      user-select: none;
      padding-right: 18px;
      border: 1.5px solid rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(8px);
      background-color: rgba(255,255,255,0.07);
    }
    .feature-card:hover {
      box-shadow: 0 12px 48px rgba(255,71,110,0.7);
      transform: scale(1.05);
      border-color: #ff416c;
      background-color: rgba(255,255,255,0.12);
    }
    .fb-card {
      background-image: url('https://cdn.pixabay.com/photo/2016/04/15/11/46/facebook-1327866_1280.png');
    }
    .ig-card {
      background-image: url('https://i.imgur.com/ZYUdbZC.jpg');
    }
    .wa-card {
      background-image: url('https://cdn.pixabay.com/photo/2017/01/17/15/28/whatsapp-1984586_1280.png');
    }
    .about-btn {
      display: block;
      margin: 0 auto;
      margin-top: 30px;
      padding: 14px 36px;
      border-radius: 16px;
      font-weight: 600;
      font-size: 1.13rem;
      color: #ff5864;
      background: rgba(255, 255, 255, 0.12);
      border: 2.5px solid #ff5864;
      cursor: pointer;
      user-select: none;
      transition: background 0.3s ease, color 0.3s ease;
      box-shadow: 0 4px 24px rgba(255, 88, 100, 0.35);
      text-align: center;
    }
    .about-btn:hover {
      background: #ff5864;
      color: #fff;
      box-shadow: 0 8px 38px #ff5864cc;
    }
    /* Modal style */
    .modal, .about-modal {
      position: fixed; 
      top: 0; left:0;
      width: 100vw; height: 100vh;
      background: rgba(0,0,0,0.78);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }
    .modal.show, .about-modal.show {
      opacity: 1;
      pointer-events: auto;
    }
    .modal-content, .about-modal-content {
      background: #1a1a1a;
      border-radius: 20px;
      max-width: 480px;
      width: 90vw;
      max-height: 85vh;
      overflow-y: auto;
      padding: 24px 18px;
      box-shadow: 0 12px 48px #ff416caa;
      color: #eee;
      position: relative;
      font-size: 1rem;
      font-weight: 400;
      letter-spacing: 0.6px;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    .close-btn {
      position: absolute;
      top: 14px;
      right: 14px;
      background: #ff4b2b;
      border: none;
      width: 36px;
      height: 36px;
      font-size: 26px;
      color: #fff;
      font-weight: 700;
      border-radius: 50%;
      cursor: pointer;
      box-shadow: 0 0 12px #ff416ccc;
      transition: background 0.3s ease;
      line-height: 1;
    }
    .close-btn:hover {
      background: #ff0040;
    }
    .modal-title {
      font-size: 1.5rem;
      font-weight: 800;
      margin-bottom: 20px;
      text-align: center;
      color: #ff6570;
      letter-spacing: 1.2px;
      text-shadow: 0 0 10px #ff5864bb;
    }
    .feature-list-grid {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }
    .modal-list-card {
      cursor: pointer;
      background: #292929;
      padding: 12px 16px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      gap: 16px;
      box-shadow: 0 4px 20px rgba(255, 101, 112, 0.3);
      transition: background 0.3s ease;
      border: 1px solid transparent;
      user-select: none;
    }
    .modal-list-card:hover {
      background: #ff4b51;
      border-color: #ff4141;
      box-shadow: 0 6px 24px #ff2a2acc;
    }
    .list-card-bg {
      width: 56px;
      height: 56px;
      border-radius: 14px;
      background-size: cover;
      background-position: center;
      flex-shrink: 0;
      box-shadow: 0 0 8px rgba(255,101,112,0.6);
    }
    .list-card-content {
      color: #fff;
    }
    .list-card-title {
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 4px;
      letter-spacing: 0.7px;
    }
    .list-card-desc {
      font-weight: 400;
      font-size: 0.9rem;
      opacity: 0.85;
      white-space: normal;
      max-width: calc(100% - 72px);
      line-height: 1.3;
    }
    @media (max-width: 570px) {
      .container {
        max-width: 96vw;
        margin: 28px auto 40px;
      }
      .feature-card {
        font-size: 1.05rem;
        height: 95px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1 class="main-title">WELCOME TO YK TRICKS INDIA</h1>
    <div class="premium-box" onclick="showFeatureModal()">EXPLORE PREMIUM FEATURES</div>
    <div class="feature-row">
      <div class="feature-card fb-card">FACEBOOK TOOLS</div>
      <div class="feature-card ig-card">INSTAGRAM TOOLS</div>
      <div class="feature-card wa-card">WHATSAPP TOOLS</div>
    </div>
    <button class="about-btn" onclick="showAboutModal()">ABOUT SYSTEM</button>
  </div>

  <!-- PREMIUM FEATURES MODAL -->
  <div id="modal" class="modal" tabindex="-1" aria-hidden="true" role="dialog" aria-modal="true">
    <div class="modal-content" role="document">
      <button class="close-btn" aria-label="Close modal" onclick="closeFeatureModal()">×</button>
      <div class="modal-title">PREMIUM FEATURES</div>
      <div class="feature-list-grid">
        <div class="modal-list-card" onclick="window.open('https://example.com/instagram-bot','_blank')">
          <div class="list-card-bg" style="background-image:url('https://i.imgur.com/ZYUdbZC.jpg');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Instagram Chat Bot</div>
            <div class="list-card-desc">Automate Instagram chats, DMs, replies, and more.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/whatsapp-bot','_blank')">
          <div class="list-card-bg" style="background-image:url('https://cdn.pixabay.com/photo/2017/01/17/15/28/whatsapp-1984586_1280.png');"></div>
          <div class="list-card-content">
            <div class="list-card-title">WhatsApp Chat Bot</div>
            <div class="list-card-desc">Smart automation for WhatsApp chats and customers.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/telegram-bot','_blank')">
          <div class="list-card-bg" style="background-image:url('https://i.imgur.com/AJjoE9t.png');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Telegram Chat Bot</div>
            <div class="list-card-desc">Broadcasts, replies, group management on Telegram.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/facebook-bot','_blank')">
          <div class="list-card-bg" style="background-image:url('https://cdn.pixabay.com/photo/2016/04/15/11/46/facebook-1327866_1280.png');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Facebook Chat Bot</div>
            <div class="list-card-desc">Chat and automation for Facebook pages and groups.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/facebook-automation','_blank')">
          <div class="list-card-bg" style="background-image:url('https://i.imgur.com/EUj4c1H.jpg');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Facebook Automation</div>
            <div class="list-card-desc">Auto-like, group post, comment scheduling tools.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/instagram-automation','_blank')">
          <div class="list-card-bg" style="background-image:url('https://i.imgur.com/vKraKOK.jpg');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Instagram Automation</div>
            <div class="list-card-desc">Auto-follow, comment, story view and more.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/instagram-recovery','_blank')">
          <div class="list-card-bg" style="background-image:url('https://i.imgur.com/CKUfYYS.jpg');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Instagram Account Recovery</div>
            <div class="list-card-desc">Fast Insta account recovery with full support.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/whatsapp-automation','_blank')">
          <div class="list-card-bg" style="background-image:url('https://cdn.pixabay.com/photo/2017/01/17/15/28/whatsapp-1984586_1280.png');"></div>
          <div class="list-card-content">
            <div class="list-card-title">WhatsApp Automation</div>
            <div class="list-card-desc">Bulk messages, scheduled text, replies, and more.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/telegram-automation','_blank')">
          <div class="list-card-bg" style="background-image:url('https://i.imgur.com/AJjoE9t.png');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Telegram Automation</div>
            <div class="list-card-desc">Automate posting, group and user management.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/facebook-comment','_blank')">
          <div class="list-card-bg" style="background-image:url('https://cdn.pixabay.com/photo/2016/11/19/14/00/facebook-1834007_1280.jpg');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Facebook Post Comment</div>
            <div class="list-card-desc">Auto-comment and reply for posts/groups.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/facebook-chat','_blank')">
          <div class="list-card-bg" style="background-image:url('https://cdn.pixabay.com/photo/2016/04/24/17/52/facebook-1349727_1280.png');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Facebook Automation Chat</div>
            <div class="list-card-desc">Automate group chat and inbox responses fast.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/instagram-group','_blank')">
          <div class="list-card-bg" style="background-image:url('https://i.imgur.com/vKraKOK.jpg');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Instagram Group Chat Automation</div>
            <div class="list-card-desc">Auto-moderate and engage Instagram groups.</div>
          </div>
        </div>
        <div class="modal-list-card" onclick="window.open('https://example.com/instagram-dm','_blank')">
          <div class="list-card-bg" style="background-image:url('https://i.imgur.com/tKQw9Id.jpg');"></div>
          <div class="list-card-content">
            <div class="list-card-title">Instagram Inbox DM</div>
            <div class="list-card-desc">Automate Instagram DMs for outreach/support.</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ABOUT MODAL -->
  <div id="aboutModal" class="about-modal" tabindex="-1" aria-hidden="true" role="dialog" aria-modal="true">
    <div class="about-modal-content" role="document">
      <button class="close-btn" aria-label="Close modal" onclick="closeAboutModal()">×</button>
      <h2 style="color:#ff6470; text-align:center; margin-bottom: 22px; font-weight: 900;">ABOUT SYSTEM</h2>
      <div style="text-align:center; font-size:1.05rem; line-height:1.5; color:#eee; margin-bottom: 18px;">
        Premium tool admin panel Version 2.0. Built for fast device linking, automated tasks, group management, chat automation, and more.
      </div>
      <div style="color:#ff7a85; font-weight: 600; text-align:center; line-height: 1.4; font-size: 1rem;">
        Developed by: <b>YK Tricks India</b><br />
        Contact: <b>yktricksindia@gmail.com</b><br />
        WhatsApp: <b>+91-99XXXXXXX</b><br />
        Instagram: <b>@yktricksindia</b><br />
        Website: <b>yktricksindia.com</b>
      </div>
    </div>
  </div>

  <script>
    function showFeatureModal() {
      const modal = document.getElementById('modal');
      modal.classList.add('show');
      document.body.style.overflowY = "hidden";
    }
    function closeFeatureModal() {
      const modal = document.getElementById('modal');
      modal.classList.remove('show');
      document.body.style.overflowY = "auto";
    }
    function showAboutModal() {
      const modal = document.getElementById('aboutModal');
      modal.classList.add('show');
      document.body.style.overflowY = "hidden";
    }
    function closeAboutModal() {
      const modal = document.getElementById('aboutModal');
      modal.classList.remove('show');
      document.body.style.overflowY = "auto";
    }

    // Accessibility: close modals on ESC key
    document.addEventListener('keydown', function(e) {
      if (e.key === "Escape") {
        closeFeatureModal();
        closeAboutModal();
      }
    });
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
        
