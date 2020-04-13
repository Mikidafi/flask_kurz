from mdblog.app import app


if __name__ == "__main__":
    host = "0.0.0.0"
    debug = True
    app.run(host, debug=debug)