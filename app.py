from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    message = ""
    shift = ""
    mode = ""

    if request.method == "POST":
        message = request.form["message"]
        shift = int(request.form["shift"])
        mode = request.form["mode"]
        output = caesar_cipher(message, shift, mode)

    return render_template("index.html", output=output, message=message, shift=shift, mode=mode)


if __name__ == "__main__":
    app.run(debug=True)
