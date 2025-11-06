# test_groq_connectivity.py
import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "gsk_your_actual_key_here"

print("🔍 Checking Groq connectivity...")
try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    models = client.models.list()
    print(f"✅ Groq reachable: {len(models.data)} models available.")
    for m in models.data[:3]:
        print("   -", m.id)
except Exception as e:
    print("❌ Groq connectivity failed:", e)
