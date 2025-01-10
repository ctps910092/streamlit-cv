import streamlit as st
from PIL import Image, ImageEnhance

def adjust_brightness(image_path, brightness_factor):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(brightness_factor)

st.set_page_config(
    page_title="Resume",
    page_icon="📄",
    layout="centered"  # Options: "centered" or "wide"
)

st.markdown("""
    <style>
        .main {
            max-width: 700px; /* Adjust the width as needed */
            margin: auto;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
        /* Change sidebar background color to yellow and text color to black */
        [data-testid="stSidebar"] {
            background-color: #073763; /* Light yellow */
            color: #ffffff;
        }

                /* Center align all headings in the sidebar */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3 {
            text-align: center;
        }
        
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("Resume")
    st.subheader("Machine Learning Engineer, Data Scientist")
    st.image("static/profile.jpg")

    col1, col2 = st.columns([0.5, 5]) 
    with col1:
        st.image("static/user.png") 
    with col2:
        st.write("Shih-Ying Chen")
    
    col1, col2 = st.columns([0.5, 5])
    with col1:
        st.image("static/mail.png") 
    with col2:
        st.write("shihying0516@gmail.com")
    
    col1, col2 = st.columns([0.5, 5])
    with col1:
        st.image("static/telephone.png") 
    with col2:
        st.write("+886 938599730")


    st.subheader("Certification")
    st.image("static/Certification.png", caption="Google Digital Talent Exploration")
    st.subheader("Skills")
    st.write("""
    - Programming Languages: Python (NumPy, Pandas), Golang
    - ML Frameworks & Tools: TensorFlow, PyTorch, Scikit-learn
    - Data Engineering & Databases: BigQuery, AlloyDB, MySQL
    - Cloud Platforms & MLOps: Vertex AI Pipelines, CI/CD for ML
    - Natural Language Processing: Word Embeddings, Semantic Analysis
    """)

st.markdown('<div class="main">', unsafe_allow_html=True)  # Start of the custom container
st.title("Education")
st.write("**National Changhua University of Education**")
st.write("Master of Science, Statistics and Information Science")
st.write("Sep 2019 - Jul 2021")
st.write("**Related Courses:** Artificial Intelligence, Machine Learning, Deep Learning, Data Science, Statistics")

st.title("Employment")
st.subheader("Machine Learning Engineer (May 2024 - Present)")
st.write("**TenMax Technology Co., Ltd.**")
st.write("""
- Designed and deployed predictive models to address complex business challenges using GCP tools such as Vertex AI and BigQuery ML.
- Optimized data pipelines and ETL workflows for scalability and efficiency, leveraging GCP services like Vertex AI Pipelines, AlloyDB, and BigQuery.
- Implemented ML-based recommendation and tagging systems on GCP.
""")

st.subheader("Data Analyst (Jul 2022 - May 2024)")
st.write("**Taiwan AI Labs**")
st.write("""
- Utilized Pandas, NumPy, and Scikit-Learn to process, analyze, and derive insights from large datasets.
- Created a comprehensive tool that encompasses clustering comment content based on semantic encoding and extracting entities from comments using ChatGPT.
""")

st.subheader("Data Analyst (Jul 2021 - May 2022)")
st.write("**Artificial Intelligence Applications Team, Xin Yin Information Ltd.**")
st.write("""
- Developed algorithms to analyze the platform, identify potential issues, propose marketing suggestions, and forecast future trends.
- Designed LSTM and ARIMA models that effectively predict platform trends.
""")

st.subheader("Research Assistant (Oct 2020 - Jun 2021)")
st.write("**National Changhua University of Education**")
st.write("""
- Predicting and Visualizing the Relationship between Small Genetic Variants and Disease Phenotype Expression.
- Employed the TensorFlow and PyTorch frameworks to develop Convolutional Neural Networks (CNN) with the aim of achieving predictive objectives.
""")
st.markdown('</div>', unsafe_allow_html=True)  # End of the custom container
