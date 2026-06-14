import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# 1. INITIALIZATION & SECURITY MATRIX
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

client = genai.Client(api_key=api_key)

# 2. Page Configuration (Set to dark theme base defaults)
st.set_page_config(
    page_title="GS-Flow Studio", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. HIGH-PERFORMANCE PREMIUM PURE BLACK CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&none');
    
    /* True Black Background Reset & Performance Optimization */
    .stApp {
        background-color: #000000 !important;
        color: #f1f5f9;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Remove default layout padding noise for instantaneous rendering */
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding-top: 2rem !important; padding-bottom: 2rem !important;}
    
    /* Targeted Panel Styling (Fixes the ghost/empty boxes) */
    .studio-panel {
        background: #090d16;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    
    /* Optimized Inputs */
    .stTextArea textarea {
        background-color: #020617 !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        color: #f1f5f9 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
    }
    .stTextArea textarea:focus {
        border-color: #6366f1 !important;
    }
    
    /* High-Performance Action Button */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
        color: #ffffff;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
        border-radius: 8px;
        transition: transform 0.1s ease, background 0.2s ease;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #5a52e6 0%, #4c41d9 100%);
        border: none;
        color: white;
    }
    div.stButton > button:first-child:active {
        transform: scale(0.99);
    }
    
    /* Output Asset Containers */
    .asset-card {
        background: #020617;
        border: 1px solid #1e293b;
        border-radius: 10px;
        padding: 18px;
        margin-top: 14px;
    }
    .asset-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #818cf8;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .asset-content {
        color: #f1f5f9;
        font-size: 1rem;
        line-height: 1.5;
    }
    
    /* Clean Status Indicator */
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        background: rgba(16, 185, 129, 0.06);
        border: 1px solid rgba(16, 185, 129, 0.15);
        color: #34d399;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# 4. BRAND NAVIGATION HEADER
st.markdown("""
    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;'>
        <div>
            <h1 style='font-size: 1.6rem; font-weight: 700; color: #ffffff; margin: 0; letter-spacing: -0.03em;'>GS-FLOW <span style='color: #6366f1;'>STUDIO</span></h1>
            <p style='color: #475569; font-size: 0.8rem; margin: 2px 0 0 0; font-weight: 500; letter-spacing: 0.05em;'>LIVE INTERACTIVE CORE v2.5</p>
        </div>
        <div class='status-badge'>● ONLINE</div>
    </div>
""", unsafe_allow_html=True)

# 5. SPLIT WORKSPACE INTERFACE (Pure HTML grid injection for zero container lag)
left_workspace, right_workspace = st.columns(2, gap="large")

with left_workspace:
    # Injecting our specific custom panel container
    st.markdown("""
        <div class='studio-panel'>
            <h3 style='font-size: 1.1rem; font-weight: 600; color: #ffffff; margin: 0 0 4px 0;'>Source Narrative</h3>
            <p style='color: #475569; font-size: 0.8rem; margin: 0 0 20px 0;'>Input your raw video scripts or creative thoughts below.</p>
        </div>
    """, unsafe_allow_html=True)
    
    video_script = st.text_area(
        label="Source Script Input",
        placeholder="Drop your script text here...",
        height=280,
        label_visibility="collapsed"
    )
    
    trigger_generation = st.button("Synthesize Assets →")

with right_workspace:
    st.markdown("""
        <div class='studio-panel'>
            <h3 style='font-size: 1.1rem; font-weight: 600; color: #ffffff; margin: 0 0 4px 0;'>Distribution Kit Matrix</h3>
            <p style='color: #475569; font-size: 0.8rem; margin: 0 0 20px 0;'>AI-optimized production assets will compile instantly below.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if trigger_generation:
        if not video_script.strip():
            st.toast("Input required.", icon="⚠️")
            st.markdown("<p style='color: #334155; font-size: 0.9rem; font-style: italic;'>Awaiting execution signals...</p>", unsafe_allow_html=True)
        else:
            with st.spinner("Processing through Gemini Engine..."):
                prompt = f"""
                You are an elite content strategist. Analyze this script and construct high-performance distribution assets.
                
                Script:
                "{video_script}"
                
                Provide your output exactly inside this block format without changing the structural tokens:
                [TITLE_START]
                (Write a highly clickable viral title)
                [TITLE_END]
                [CAPTION_START]
                (Write an engaging short caption with relevant emojis and 3 highly specific trending hashtags)
                [CAPTION_END]
                """
                
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                    )
                    
                    raw_output = response.text
                    title = "Processing error on title extraction."
                    caption = "Processing error on caption extraction."
                    
                    if "[TITLE_START]" in raw_output and "[TITLE_END]" in raw_output:
                        title = raw_output.split("[TITLE_START]")[1].split("[TITLE_END]")[0].strip()
                    if "[CAPTION_START]" in raw_output and "[CAPTION_END]" in raw_output:
                        caption = raw_output.split("[CAPTION_START]")[1].split("[CAPTION_END]")[0].strip()
                    
                    st.markdown(f"""
                        <div class='asset-card'>
                            <div class='asset-label'>🎯 Optimized Headline / Viral Title</div>
                            <div class='asset-content' style='font-weight: 600; font-size: 1.1rem; color: #ffffff;'>{title}</div>
                        </div>
                        <div class='asset-card'>
                            <div class='asset-label'>📸 Distribution Caption & Metadata</div>
                            <div class='asset-content'>{caption}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Runtime Operational Failure: {e}")
    else:
        st.markdown("<p style='color: #334155; font-size: 0.9rem; font-style: italic; text-align: center; margin-top: 20px;'>Awaiting execution signals...</p>", unsafe_allow_html=True)