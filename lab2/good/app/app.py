from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os, time, platform, socket

START = time.time()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        uptime = int(time.time() - START)
        info = {
            "message": "Hello from container",
            "pid": os.getpid(),
            "python_version": platform.python_version(),
            "hostname": socket.gethostname(),
            "uptime_seconds": uptime
        }
        body = json.dumps(info).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # чтобы терминал был чище (не печатать каждый запрос)
    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    server = HTTPServer(("", port), Handler)
    print(f"Listening on 0.0.0.0:{port}")
    server.serve_forever()