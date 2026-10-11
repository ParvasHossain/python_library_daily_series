from flask import Flask, request, g

app = Flask(__name__)

@app.before_request
def load_user():
    # Application/Request context automatically active for this thread
    g.user_id = request.headers.get("X-User-ID", "Guest")

@app.route("/api")
def api():
    # LocalProxy resolves 'g' and 'request' to current thread's state
    return {"message": f"Hello, {g.user_id}!"}

if __name__ == "__main__":
    app.run()