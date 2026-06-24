from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "xebrid2026"

@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge

    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)
    return "OK", 200

if __name__ == "__main__":
    app.run()
