import streamlit as st

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
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>Resume</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 45px;'>Shih-Ying Chen</h1>", unsafe_allow_html=True)
    st.subheader("Machine Learning Engineer, Data Scientist")
    st.image("static/profile.jpg")

    st.markdown(
        """
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="flex: 0.5;">
                <img src="https://i.imgur.com/YwLlSqD.png" alt="LinkedIn" style="width: 40px;">
            </div>
            <div style="flex: 5; margin-left: 10px;">
                <a href="https://www.linkedin.com/in/shihying-chen/" target="_blank" style="text-decoration: none; color: inherit;">
                    https://www.linkedin.com/in/shihying-chen/
                </a>
            </div>
        </div>
        
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="flex: 0.5;">
                <img src="https://i.imgur.com/jl9glQL.png" alt="Mail" style="width: 40px;">
            </div>
            <div style="flex: 5; margin-left: 10px;">
                <a href="mailto:shihying0516@gmail.com" style="text-decoration: none; color: inherit;">
                    shihying0516@gmail.com
                </a>
            </div>
        </div>
        
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="flex: 0.5;">
                <img src="https://i.imgur.com/v2SeKrc.png" alt="Telephone" style="width: 40px;">
            </div>
            <div style="flex: 5; margin-left: 10px;">
                +886 938599730
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Certification</h1>", unsafe_allow_html=True)
    st.image("static/Certification.png", caption="Google Digital Talent Exploration")
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Skills</h1>", unsafe_allow_html=True)

    st.write("""
    - Programming Languages: Python (NumPy, Pandas), Golang
    - ML Frameworks & Tools: TensorFlow, PyTorch, Scikit-learn
    - Data Engineering & Databases: BigQuery, AlloyDB, MySQL
    - Cloud Platforms & MLOps: Vertex AI Pipelines, CI/CD for ML
    - Natural Language Processing: Word Embeddings, Semantic Analysis
    """)

st.markdown('<div class="main">', unsafe_allow_html=True)  # Start of the custom container
st.title("Education")
st.subheader("National Changhua University of Education")
st.write("**Master of Science, Statistics and Information Science**")
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
