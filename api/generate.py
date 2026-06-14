import os
import json
from http.server import BaseHTTPRequestHandler
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        payload = json.loads(post_data.decode('utf-8'))
        video_script = payload.get("script", "")

        prompt = f"""
        Analyze this script and construct high-performance distribution assets.
        Script: "{video_script}"
        
        Format the response exactly inside this block token framework:
        [TITLE_START]
        (Write a highly clickable viral title)
        [TITLE_END]
        [CAPTION_START]
        (Write an engaging short caption with emojis and 3 specific trending hashtags)
        [CAPTION_END]
        """

        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            raw_output = response.text
            
            title = "Title compile error."
            caption = "Caption compile error."
            
            if "[TITLE_START]" in raw_output and "[TITLE_END]" in raw_output:
                title = raw_output.split("[TITLE_START]")[1].split("[TITLE_END]")[0].strip()
            if "[CAPTION_START]" in raw_output and "[CAPTION_END]" in raw_output:
                caption = raw_output.split("[CAPTION_START]")[1].split("[CAPTION_END]")[0].strip()

            response_data = {"title": title, "caption": caption}
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))