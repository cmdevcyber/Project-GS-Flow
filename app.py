import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# 1. INITIALIZATION & SECURITY MATRIX
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Resilient client initialization for both local .env and Streamlit Cloud secrets
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

client = genai.Client(api_key=api_key)

# 2. PREMIUM PAGE CONFIGURATION
st.set_page_config(
    page_title="GS-Flow Studio // Advanced Content Intelligence", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. HIGH-END PRODUCTION CSS (Studio Dark Custom Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Global Application Reset & Typography */
    .stApp {
        background-color: #0b0f19;
        background-image: 
            radial-gradient(at 0% 0%, rgba(31, 41, 234, 0.07) 0, transparent 50%),
            radial-gradient(at 100% 100%, rgba(99, 102, 241, 0.05) 0, transparent 50%);
        color: #f1f5f9;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Header Typography Customization */
    h1, h2, h3 {
        font-family: 'Plus Jakarta Sans', sans-serif;
        letter-spacing: -0.02em !important;
    }
    
    /* Hide default Streamlit aesthetic noise */
    #MainMenu, header, footer {visibility: hidden;}
    .embeddedApp_innerWindow__16g8_ {padding: 0;}
    
    /* Premium Glowing Workspace Cards */
    div[data-testid="stVerticalBlock"] > div:has(.glass-panel) {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 16px;
        padding: 28px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
    }
    
    /* Smooth Interactive Text Area */
    .stTextArea textarea {
        background-color: rgba(13, 18, 30, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 10px !important;
        color: #e2e8f0 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stTextArea textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.15) !important;
    }
    
    /* Ultra-Premium Action Button */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 50%, #4338ca 100%);
        color: #ffffff;
        border: none;
        padding: 14px 24px;
        font-weight: 600;
        letter-spacing: -0.01em;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.25);
        transition: all 0.25s ease;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 24px rgba(99, 102, 241, 0.4);
        background: linear-gradient(135deg, #5a52e6 0%, #6c6ff2 50%, #4c41d9 100%);
    }
    div.stButton > button:first-child:active {
        transform: translateY(1px);
    }
    
    /* Output Asset Containers */
    .asset-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .asset-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #818cf8;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .asset-content {
        color: #f1f5f9;
        font-size: 1.05rem;
        line-height: 1.5;
    }
    
    /* Custom Notification Badge */
    .status-badge {
        display: inline-block;
        padding: 4px 10px;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.2);
        color: #34d399;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        margin-bottom: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# 4. BRAND NAVIGATION HEADER
st.markdown("""
    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; padding: 10px 0;'>
        <div>
            <h1 style='font-size: 1.75rem; font-weight: 700; background: linear-gradient(90deg, #ffffff 0%, #94a3b8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>GS-FLOW <span style='color: #6366f1; -webkit-text-fill-color: initial;'>STUDIO</span></h1>
            <p style='color: #64748b; font-size: 0.85rem; margin: 0; font-weight: 500;'>ENGINE VERSION 2.5 // LIVE INTERACTIVE CORE</p>
        </div>
        <div class='status-badge'>● ENGINE OPERATIONAL</div>
    </div>
""", unsafe_allow_html=True)

# 5. SPLIT WORKSPACE INTERFACE (Balanced Columns)
left_workspace, right_workspace = st.columns([1, 1], gap="large")

with left_workspace:
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 1.15rem; font-weight: 600; color: #f8fafc; margin-bottom: 6px;'>Source Narrative</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 0.85rem; margin-bottom: 20px;'>Input your raw video scripts, film log drafts, or content ideation fragments below.</p>", unsafe_allow_html=True)
    
    video_script = st.text_area(
        label="Source Script Input",
        placeholder="Drop your sequence text or raw concepts here...",
        height=320,
        label_visibility="collapsed"
    )
    
    st.markdown("<div style='margin-top: 24px;'>", unsafe_allow_html=True)
    trigger_generation = st.button("Synthesize Assets →")
    st.markdown("</div></div>", unsafe_allow_html=True)

with right_workspace:
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 1.15rem; font-weight: 600; color: #f8fafc; margin-bottom: 6px;'>Distribution Kit Matrix</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 0.85rem; margin-bottom: 20px;'>AI-optimized high-engagement assets will compile instantly in this container.</p>", unsafe_allow_html=True)
    
    if trigger_generation:
        if not video_script.strip():
            st.toast("Initialization Error: Source input empty.", icon="❌")
            st.markdown("<p style='color: #64748b; font-size: 0.9rem; font-style: italic;'>Awaiting source execution signals...</p>", unsafe_allow_html=True)
        else:
            if not api_key:
                st.error("Authentication Error: API Core Key configuration missing in server environment.")
            else:
                with st.spinner("Processing through Gemini Neural Engine..."):
                    # Prompt designed for structured clean string slicing
                    prompt = f"""
                    You are an elite cinematic and brand copywriter. Analyze this script and construct high-performance assets.
                    
                    Script text:
                    "{video_script}"
                    
                    Provide your final output exactly inside this block format without changing the markers:
                    [TITLE_START]
                    (Write one catchy, high-CTR main title suited perfectly to the topic)
                    [TITLE_END]
                    [CAPTION_START]
                    (Write a highly engaging short description/caption with contextual emojis and 3 hyper-relevant trending hashtags specific to this exact script topic. Do not use generic placeholders.)
                    [CAPTION_END]
                    """
                    
                    try:
                        response = client.models.generate_content(
                            model='gemini-2.5-flash',
                            contents=prompt,
                        )
                        
                        raw_output = response.text
                        
                        # High-res structural parsing for elegant separation
                        title = "Generated Title Asset"
                        caption = "Generated Caption Asset"
                        
                        if "[TITLE_START]" in raw_output and "[TITLE_END]" in raw_output:
                            title = raw_output.split("[TITLE_START]")[1].split("[TITLE_END]")[0].strip()
                        if "[CAPTION_START]" in raw_output and "[CAPTION_END]" in raw_output:
                            caption = raw_output.split("[CAPTION_START]")[1].split("[CAPTION_END]")[0].strip()
                        
                        # Displaying assets inside professional design structures
                        st.markdown(f"""
                            <div class='asset-card'>
                                <div class='asset-label'>🎯 Optimized Headline / Viral Title</div>
                                <div class='asset-content' style='font-weight: 600; font-size: 1.25rem; color: #ffffff;'>{title}</div>
                            </div>
                            <div class='asset-card'>
                                <div class='asset-label'>📸 Distribution Caption & Metadata</div>
                                <div class='asset-content'>{caption}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        st.toast("Assets compiled successfully.", icon="⚡")
                        
                    except Exception as e:
                        st.error(f"Runtime Operational Failure: {e}")
    else:
        st.markdown("<p style='color: #475569; font-size: 0.9rem; font-style: italic; margin-top: 40px; text-align: center;'>Awaiting source execution signals...</p>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)