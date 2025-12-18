# 🕶️ AKKI SocialRecon

AKKI SocialRecon is a professional **Kali Linux CLI-based OSINT (Open Source Intelligence)** tool designed to search and verify usernames across multiple social media platforms using **asynchronous requests** and a **hacker-style terminal interface**.

This tool is built especially for **cybersecurity students, OSINT researchers, and ethical hackers**.

---

## 🚀 Features

* 🔍 Username reconnaissance across multiple social media platforms
* ⚡ Fast scanning using asynchronous requests (`aiohttp`)
* 🧠 Hacker-style CLI banner & terminal UI
* 📊 Real-time progress bar
* 🖥️ Interactive mode (asks for username if not provided)
* 🐧 Optimized for Kali Linux (works on any Linux distro)
* ❌ No API keys required
* 📦 Lightweight, fast & easy to use

---

## 🌐 Supported Platforms

* GitHub
* GitLab
* Twitter (X)
* Instagram
* Facebook
* LinkedIn
* Reddit
* YouTube
* Telegram
* Snapchat
* TikTok
* Pinterest
* Medium
* WordPress
* SoundCloud
* Twitch

---

## 🛠️ Requirements

* Python **3.8+**
* Kali Linux / Any Linux distribution

### 📦 Required Python Libraries

```bash
pip3 install aiohttp rich colorama
```

---

## 📥 Installation

### 🔹 Clone the Repository

```bash
[https://github.com/ankit-sec/social-media-recon-akki.git]
cd social-media-recon
```

### 🔹 Install Dependencies

```bash
pip3 install -r requirements.txt
```

**OR install manually:**

```bash
pip3 install aiohttp rich colorama
```

---

## ▶️ Usage

### 🔹 Interactive Mode (Banner + Username Prompt)

```bash
python3 main.py
```

The tool will start and ask you to enter a username.

---

### 🔹 Direct Username Scan

```bash
python3 main.py akki_root
```

---

## 📊 Output

AKKI SocialRecon displays a clean and readable table containing:

* Platform Name
* Account Status (**FOUND / NOT FOUND**)
* Profile URL
* HTTP Status Code

---

## ⚠️ Disclaimer

This tool is developed **strictly for educational and ethical purposes only**.

* ❌ Do NOT use this tool for harassment, stalking, or illegal activities
* ⚖️ Always respect user privacy
* 📜 Follow the terms of service of each platform

The author is **not responsible for any misuse** of this tool.

---

## 👨‍💻 Author

**Ankit Kumar**
Cybersecurity | OSINT | Kali Linux
Ethical Hacking Enthusiast

---

## ⭐ Support & Contribution

If you like this project:

* ⭐ Star the repository
* 🍴 Fork the project
* 🧠 Contribute by adding new platforms or features

Pull requests are welcome!

---

## 🔮 Future Plans

* 🌐 Domain reconnaissance mode
* 📄 JSON / TXT report export
* 🧅 Tor / Proxy support
* 🔀 Username mutation engine
* 🎯 False-positive reduction

---

Happy Hunting 🕵️‍♂️ | Stay Ethical 🔐
