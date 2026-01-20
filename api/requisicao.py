from http.server import BaseHTTPRequestHandler
import json
import os

from pipeline import executa_pipeline


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            auth = self.headers.get("Authorization")
            expected = f"Bearer {os.getenv('INTERNAL_API_TOKEN')}"

            if auth != expected:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b"Unauthorized")
                return

            result = executa_pipeline()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps({
                    "status": "ok",
                    "result": result
                }).encode()
            )

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())
