import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# 1. Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 2. Page Configuration
st.set_page_config(page_title="Project GS-Flow", page_icon="⚡", layout="wide")

# 3. Inject Premium Custom CSS (Modern Dark Studio Theme)
st.markdown("""
    <style>
    /* Main Background & Font Styling */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sleek Cards for UI Sections */
    .css-1r6slb0, .stTextArea, .stMarkdown {
        border-radius: 12px;
    }
    
    /* Premium Button Styling */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border: none;
        padding: 12px 30px;
        font-weight: 600;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.6);
        background: linear-gradient(90deg, #5a52e6 0%, #8b46f7 100%);
    }
    
    /* Divider lines styling */
    hr {
        border-color: rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 4. Header Section with Columns
col1, col2 = st.columns([1, 5])
with col1:
    st.write("") # Spacing
with col2:
    st.markdown("<h1 style='color: #a78bfa; margin-bottom: 0;'>⚡ PROJECT GS-FLOW</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; font-size: 1.1rem;'>Next-Generation Content Automation Engine</p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 5. Split UI into Two Side-by-Side Columns (Input vs Output)
left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown("### 📋 Creator Input Workspace")
    video_script = st.text_area(
        label="Paste your video script or cinematic intro drafts here:",
        placeholder="Type or paste your content here...",
        height=300,
        label_visibility="collapsed"
    )
    
    generate_btn = st.button("Deploy AI Core ✨")

with right_col:
    st.markdown("### 🚀 AI Generated Distribution Kit")
    
    if generate_btn:
        if not video_script.strip():
            st.warning("⚠️ Enter a script first to activate the generation matrix.")
        else:
            with st.spinner("Processing script through Gemini-2.5-Flash..."):
                prompt = f"""
                You are an elite, highly professional social media strategist. 
                Analyze this video script and deliver a premium distribution kit.
                
                Script:
                "{video_script}"
                
                Format the response beautifully using clear Markdown sections.
                Include an explosive Title section and an engaging Shorts Caption section with highly relevant, trending hashtags tailored perfectly to the theme of the text (no generic placeholders).
                """
                
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                    )
                    
                    # Output display inside a premium wrapper
                    st.markdown("<div style='background-color: rgba(255,255,255,0.05); padding: 20px; border-radius: 12px; border-left: 5px solid #7c3aed;'>", unsafe_allow_html=True)
                    st.markdown(response.text)
                    st.markdown("</div>", unsafe_allow_html=True)
                    st.toast("Assets Generated Successfully!", icon="🔥")
                    
                except Exception as e:
                    st.error(f"Execution Error: {e}")