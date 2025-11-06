# ===========================================
# preload_patch.py — fixes Render proxy issue
# ===========================================
import os

# 🚫 Render injects these proxy variables by default.
# They interfere with Groq/OpenAI HTTPS calls.
for proxy_var in [
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
]:
    if proxy_var in os.environ:
        print(f"⚙️ Removing proxy var: {proxy_var}")
        os.environ.pop(proxy_var, None)
