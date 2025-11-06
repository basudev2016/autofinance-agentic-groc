#!/usr/bin/env bash
# ===========================================
# render_start.sh — startup command for Render
# ===========================================

echo "🧹 Cleaning proxy variables..."
unset HTTP_PROXY
unset HTTPS_PROXY
unset ALL_PROXY
unset http_proxy
unset https_proxy
unset all_proxy

echo "🚀 Starting Streamlit app..."
streamlit run app.py --server.port $PORT --server.headless true
