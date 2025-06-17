import streamlit as st
from prompts import * 
from main import Extractpdf, Response

# Streamlit App Layout Configuration
st.set_page_config(
    page_title="RESUME SCANNER", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for chocolate/coffee theme
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

    /* Background image styling */
    .stApp {
        background-image: url('background.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Overlay for better readability */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        margin: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    /* Custom title styling - Enhanced visibility */
    .custom-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: 
#3D1F12;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
        background: linear-gradient(135deg, 
#3D1F12, 
#584738);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 2px 4px rgba(255,255,255,0.8));
    }

    .custom-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: 
#3D1F12;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 500;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }

    /* Card styling */
    .upload-card, .analysis-card {
        background: rgba(61, 31, 18, 0.9);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(152, 117, 91, 0.3);
        margin-bottom: 2rem;
    }

    /* Analysis card grid */
    .analysis-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 1.5rem;
        justify-content: center;
        margin-top: 2rem;
    }

    .analysis-card-item {
        background: linear-gradient(145deg, 
#584738, 
#3D1F12);
        border-radius: 15px;
        padding: 1.5rem;
        width: 300px;
        height: 180px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        border: 1px solid rgba(152, 117, 91, 0.4);
        transition: all 0.3s ease;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .analysis-card-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(152, 117, 91, 0.4);
        background: linear-gradient(145deg, 
#7A5E47, 
#584738);
    }

    /* Button styling */
    .stButton > button {
        width: 100%;
        height: 60px;
        border-radius: 15px;
        border: none;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 1rem;
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin-bottom: 10px;
    }

    /* Individual button colors */
    .btn-espresso .stButton > button {
        background: linear-gradient(135deg, 
#3D1F12, 
#2A1308);
    }
    .btn-espresso .stButton > button:hover {
        background: linear-gradient(135deg, 
#2A1308, 
#1A0B05);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(61, 31, 18, 0.4);
    }

    .btn-mahogany .stButton > button {
        background: linear-gradient(135deg, 
#584738, 
#403226);
    }
    .btn-mahogany .stButton > button:hover {
        background: linear-gradient(135deg, 
#403226, 
#2D2419);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(88, 71, 56, 0.4);
    }

    .btn-light-brown .stButton > button {
        background: linear-gradient(135deg, 
#98755B, 
#7A5E47);
    }
    .btn-light-brown .stButton > button:hover {
        background: linear-gradient(135deg, 
#7A5E47, 
#5C4635);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(152, 117, 91, 0.4);
    }

    .btn-milk .stButton > button {
        background: linear-gradient(135deg, 
#F1EADA, 
#E8DCC0);
        color: 
#3D1F12 !important;
        border: 2px solid 
#98755B;
    }
    .btn-milk .stButton > button:hover {
        background: linear-gradient(135deg, 
#E8DCC0, 
#DFD1B0);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(152, 117, 91, 0.3);
    }

    .btn-premium .stButton > button {
        background: linear-gradient(135deg, 
#8B4513, 
#A0522D);
    }
    .btn-premium .stButton > button:hover {
        background: linear-gradient(135deg, 
#A0522D, 
#CD853F);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139, 69, 19, 0.4);
    }

    /* Section headers */
    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 600;
        color: 
#F1EADA;
        margin-bottom: 1rem;
        text-align: left;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* Text area styling - Dark theme */
    .stTextArea > div > div > textarea {
        border-radius: 15px;
        border: 2px solid 
#98755B !important;
        background: 
#2D2419 !important;
        color: 
#F1EADA !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
    }

    .stTextArea > div > div > textarea::placeholder {
        color: 
#98755B !important;
        opacity: 0.8 !important;
    }

    .stTextArea > div > div > textarea:focus {
        border-color: 
#F1EADA !important;
        box-shadow: 0 0 10px rgba(241, 234, 218, 0.3) !important;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, 
#F1EADA, 
#FFFFFF);
    }

    /* File uploader styling - Dark theme */
    .stFileUploader > div > div {
        background: rgba(45, 36, 25, 0.9) !important;
        border: 2px dashed 
#98755B !important;
        border-radius: 15px;
        padding: 2rem;
        color: 
#F1EADA !important;
    }

    .stFileUploader label {
        color: 
#F1EADA !important;
        font-weight: 500 !important;
    }

    /* Button styling - Updated for card layout */
    .analysis-btn {
        background: none !important;
        border: none !important;
        padding: 0 !important;
        width: 100% !important;
        height: auto !important;
    }

    .analysis-btn button {
        width: 100% !important;
        height: auto !important;
        background: transparent !important;
        border: none !important;
        color: 
#F1EADA !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        padding: 0 !important;
        cursor: pointer !important;
    }

    /* Hide Streamlit help buttons and blue boxes */
    .stButton > button[title] {
        display: none !important;
    }

    .stTooltipHoverTarget {
        display: none !important;
    }

    /* Hide the small blue help boxes */
    [data-testid="stTooltipHoverTarget"] {
        display: none !important;
    }

    /* Hide all help icons */
    .css-1kyxreq {
        display: none !important;
    }

    /* Success message styling */
    .stSuccess {
        background: linear-gradient(135deg, 
#98755B, 
#7A5E47);
        color: white;
        border-radius: 10px;
    }

    /* Warning message styling */
    .stWarning {
        background: linear-gradient(135deg, 
#D2691E, 
#CD853F);
        color: white;
        border-radius: 10px;
    }

    /* Response container */
    .response-container {
        background: linear-gradient(145deg, 
#F9F7F4, 
#F1EADA);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        border-left: 5px solid 
#98755B;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Hero Section with better visibility
st.markdown("""
<div style="text-align: center; padding: 2rem 0; background: rgba(255,255,255,0.9); border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
    <h1 class="custom-title">RESUME SCANNER</h1>
    <p class="custom-subtitle">Optimize your resume with AI-driven insights and personalized feedback</p>
</div>
""", unsafe_allow_html=True)

# Enhanced sidebar
st.sidebar.markdown("### 🎯 Navigation Guide")
st.sidebar.markdown("""
<div style="background: linear-gradient(145deg, 
#F1EADA, 
#FFFFFF); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
    <h4 style="color: 
#3D1F12; margin-bottom: 1rem;">📋 Steps to Follow:</h4>
    <ol style="color: 
#584738;">
        <li><strong>Job Description</strong>: Paste the target job description</li>
        <li><strong>Resume Upload</strong>: Upload your PDF resume</li>
        <li><strong>Analysis</strong>: Choose your preferred analysis type</li>
        <li><strong>Review</strong>: Get actionable insights and feedback</li>
    </ol>
</div>
""", unsafe_allow_html=True)



# Main content area with custom cards
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">📝 Job Description</h2>', unsafe_allow_html=True)
    jd_input = st.text_area(
        "",
        placeholder="Paste the job description for the position you're applying for...",
        key="text",
        height=200,
        help="Enter the complete job description to get better analysis results"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">📄 Resume Upload</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose your resume file", 
        type=["pdf"], 
        help="Upload your resume in PDF format for comprehensive analysis"
    )
    if uploaded_file:
        st.success("✅ Resume uploaded successfully!")
    st.markdown('</div>', unsafe_allow_html=True)

# Analysis buttons section with card layout
st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">🚀 Choose Your Analysis</h2>', unsafe_allow_html=True)

warning_placeholder = st.empty()

# Create analysis cards in a grid layout
analysis_options = [
    {"key": "submit1", "icon": "📊", "title": "Job Insights", "desc": "Get detailed insights about job requirements", "prompt": "prompt1"},
    {"key": "submit2", "icon": "🎯", "title": "Skills Gap", "desc": "Identify skills you need to develop", "prompt": "prompt2"},
    {"key": "submit3", "icon": "📈", "title": "Match Score", "desc": "See how well your resume matches", "prompt": "prompt3"},
    {"key": "submit4", "icon": "🤖", "title": "ATS Check", "desc": "Check if your resume is ATS-friendly", "prompt": "prompt4"},
    {"key": "submit5", "icon": "💡", "title": "Get Feedback", "desc": "Receive improvement suggestions", "prompt": "prompt5"},
    {"key": "submit6", "icon": "🔍", "title": "Deep Analysis", "desc": "Comprehensive resume evaluation", "prompt": "prompt1"}
]

# Create the grid layout
cols = st.columns(3, gap="large")
selected_analysis = None

for i, option in enumerate(analysis_options):
    col_idx = i % 3
    with cols[col_idx]:
        # Create clickable card
        card_html = f"""
        <div class="analysis-card-item" onclick="document.getElementById('{option["key"]}').click();">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{option["icon"]}</div>
            <h3 style="color: 
#F1EADA; margin-bottom: 0.5rem; font-family: 'Inter', sans-serif;">{option["title"]}</h3>
            <p style="color: 
#98755B; font-size: 0.9rem; margin: 0; font-family: 'Inter', sans-serif;">{option["desc"]}</p>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

        # Hidden button for functionality (no help text to avoid blue boxes)
        if st.button("Click Here", key=option["key"]):
            selected_analysis = option["prompt"]

st.markdown('</div>', unsafe_allow_html=True)

# Function to generate the response based on button clicked
def generate_response(prompt):
    if uploaded_file is not None:
        with st.spinner("🔄 Analyzing your resume... Please wait"):
            try:
                pdf_content = Extractpdf(uploaded_file)
                response = Response(jd_input, pdf_content, prompt)

                st.markdown('<div class="response-container">', unsafe_allow_html=True)
                st.markdown("### 📋 Analysis Results")
                st.write(response)
                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
    else:
        warning_placeholder.warning("⚠️ Please upload your resume to proceed with the analysis!")

# Button Logic to trigger respective analysis
if selected_analysis == "prompt1":
    generate_response(prompt1)
elif selected_analysis == "prompt2":
    generate_response(prompt2)
elif selected_analysis == "prompt3":
    generate_response(prompt3)
elif selected_analysis == "prompt4":
    generate_response(prompt4)
elif selected_analysis == "prompt5":
    generate_response(prompt5)

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #584738; font-family: Inter, sans-serif;">Made with ❤️ for better career opportunities</p>', 
    unsafe_allow_html=True
)