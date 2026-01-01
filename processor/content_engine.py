import os import openai import requests

class AIContentEngine: def init(self, api_key): self.client = openai.OpenAI(api_key=api_key)

def generate_marketing_assets(self, text_input):
    """
    Transforms raw book text into structured marketing assets.
    """
    response = self.client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an elite direct-response copywriter."},
            {"role": "user", "content": f"Create a TikTok script and a newsletter from this text: {text_input}"}
        ],
        response_format={ "type": "json_object" }
    )
    return response.choices[0].message.content

def trigger_heygen_video(self, script, webhook_url):
    """
    Dispatches a video generation request to HeyGen.
    """
    payload = {
        "video_inputs": [
            {
                "character": {"type": "avatar", "avatar_id": "daisy_exp_20230101"},
                "voice": {"type": "text", "input_text": script}
            }
        ],
        "callback_url": webhook_url
    }
    # Mocking API Call
    return {"status": "processing", "video_id": "v_12345"}