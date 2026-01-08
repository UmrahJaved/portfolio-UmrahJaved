import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Umrah Javed | Data Analyst",
    page_icon="portfolio/assets/pageicon.png",
    layout="wide"
)

# CSS
st.markdown("""
<style>
.stLinkButton > a {
    background-color: #eef3f9;   
    color: #334155;
    border-radius: 8px;
    padding: 0.4rem 0.4rem;
    font-weight: 600;
    text-align: center;
    transition: background-color 0.2s ease, transform 0.15s ease;
}


.stLinkButton > a:hover {
    transform: translateY(-2px);
}

.stDownloadButton > button {
    background-color: #eef3f9 ;
    color: #334155 ;
    border-radius: 10px;
    padding: 0.7rem 1rem;
    font-weight: bold;
    transition: background-color 0.2s ease, transform 0.15s ease;
}

.stDownloadButton > button:hover {
    transform: translateY(-2px);
}           

            
.card-img-wrapper {
    overflow: hidden;
    border-radius: 12px;
    margin-bottom: 1rem;
}
            
.card-img {
    width: 400;
    transition: transform 0.35s ease;
}
            
@media (hover: hover) {
    .card-img-wrapper:hover .card-img {
        transform: scale(1.08);
    }
}  
            
.header-grid {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap: 1.5rem;
    margin-bottom: 3rem;    
}
            
.header-card {
    background: #eef3f9;
    border-radius: 18px;
    padding: 1.5rem;
    box-shadow: 0 15px 35px rgba(0,0,0,0.25);
    min-height: 280px; 
}
            
.header-card h3, .header-card h2 {
    margin-bottom: 0.5rem;
    color: #334155;
}
            
.header-card p {
    margin: 0.25rem 0;
}

.profile-img {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 1rem;
}

.header-links a, .header-links button {
    width: 100%;
    margin-bottom: 0.6rem;
    color: #334155;
}

@media (max-width: 900px) {
    .header-grid {
        grid-template-columns: 1fr;
    }
}

.stApp {
    background-color: #ffffff;
}

.block-container {
    padding: 2.5rem 6vw;
}

h1, h2, h3 {
    font-family: 'Inter', sans-serif;
    
    color: #334155;
    
}

p, li {
    font-size: 16px;
    color: #334155;
    line-height: 1.6;
}

a {
    color: #FF4B4B;
    font-weight: 600;
    text-decoration: none;
}
            
a:hover {
    text-decoration: underline;
}

.hero {
    text-align: center;
    padding: 1.5rem 1rem;
}
            
.hero h1 {
    font-size: 3rem;
}
            
.hero p {
    font-size: 1.2rem;
}

.cta {
    display: inline-block;
    margin: 0.5rem;
    padding: 0.7rem 1.4rem;
    border-radius: 8px;
    background-color: #FF4B4B;
    color: white;
}

.card {
    background-color: #eef3f9;
    padding: 20px;
    border-radius: 16px;
    min-height: 520px;              
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    cursor: pointer;
    transition: transform 0.2s ease;
}
            
.card:hover {
    transform: translateY(-6px);
}

.card a {
    position: absolute;
    inset: 0;
    opacity: 0;
}

.card img {
    max-height: 180px;
    object-fit: contain;
}

.skill {
    display: inline-block;
    background: #eef3f9;
    padding: 0.4rem 0.8rem;
    border-radius: 999px;
    margin: 0.2rem;
    font-size: 14px;
}

@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.2rem;
    }
    .block-container {
        padding: 2rem 1rem;
    }
}
            
</style>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


left, center, right = st.columns([1, 2, 1], gap="large")

# Left: PROFILE SUMMARY
with left:
    st.markdown("""
    <div class="header-card">
        <img src="https://media.licdn.com/dms/image/v2/C4E03AQHLLLQEnRU2GQ/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1640031022423?e=1769040000&v=beta&t=YBsEJ5h5DlfPqXZr3YkBOsjON5UFl46BympWfXQZLGI "
             class="profile-img" />
        <h3>Umrah Javed</h3>
        <p><b>Data Analyst / AI Developer</b></p>
        <p>📍 Brussels, Belgium</p>
    </div>
    """, unsafe_allow_html=True)

# Center: ABOUT ME
with center:
    st.markdown("""
    <div class="header-card">
        <h2>About Me</h2>
        <p>
            Curious and driven <b>Data Analyst & AI Developer</b> with hands-on
            experience in Excel, SQL, Power BI, Python, Streamlit and AI/ML projects.
        </p>
        <p>
            I focus on transforming complex datasets into
            <b>clear insights and interactive dashboards</b>
            that support real business decisions.
        </p>
        <p>
            I am curious, enthusiastic.I love to read, travel and cook.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Right: LINKS
with right:
    with st.container():
        st.markdown(
            "<h3 style='color:#334155;'>Get to know me</h3>",
            unsafe_allow_html=True
        )
        st.link_button("📧 Contact", "mailto:umrahjaved.1@gmail.com")
        st.link_button("💻 GitHub", "https://github.com/UmrahJaved")
        st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/umrah-javed/")

        with open("portfolio/assets/Umrah_Javed_CV (1).docx", "rb") as file:
            st.download_button(
                "📄 Download CV",
                file,
                file_name="Umrah_Javed_CV.docx"
            )
 

# Skills
st.markdown(
            "<h3 style='color:#334155;'>🛠 Skills</h3>",
            unsafe_allow_html=True
        )


skills = [
    "Excel", "Postgres", "SQL", "Python", "Streamlit", "Power BI", "Tableau", "Pandas", "NumPy",
    "Plotly", "Flask", "Git", "Docker",
    "Machine Learning", "NLP", "Data Visualization",
    "Agile / Scrum", "Pytest", "Selenium"
]

st.markdown("".join([f"<span class='skill'>{s}</span>" for s in skills]),
            unsafe_allow_html=True)

# Projects
st.markdown(
            "<h3 style='color:#334155;'>🚀 Featured Projects</h3>",
            unsafe_allow_html=True
        )
col1, col2, col3 = st.columns(3, gap='medium', width = "stretch" )
# Project 1
with col1:
    st.markdown("""
    <div class="card">    
        <img src='https://private-user-images.githubusercontent.com/96992159/531627145-ab64fcd4-85ec-48b1-8705-7bee6bceff72.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc1MTU1MTIsIm5iZiI6MTc2NzUxNTIxMiwicGF0aCI6Ii85Njk5MjE1OS81MzE2MjcxNDUtYWI2NGZjZDQtODVlYy00OGIxLTg3MDUtN2JlZTZiY2VmZjcyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTA0VDA4MjY1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWJmMWM2YjQzMWQ2ZGM4OGY5N2Q2MTY3YjM1ZmEwNDEwNmRlOTM1YmY3NzJhYjhiMDFlZGNmMjQ3OTI4YmJkZTYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.6_fm-ANM_jxWbDfm00bHp4z0LJRWLY2aYBHMgB7bEQ8' heigth =800 >
        <h3 style='color:#334155'>☕ Coffee Shop Sales Dashboard</h3>
        <p>
            Interactive Excel dashboard analyzing sales trends,
            peak hours, revenue performance, and customer behavior.
        </p>
        <ul>
            <li>Built with Excel(Power Query, Measures)</li>
            <li>Interactive filters & KPIs</li>
            <li>Business-focused insights</li>
        </ul>
        <a href="https://github.com/UmrahJaved/Coffee-Shop-Sales-Dashboard" target="_blank">
            🔗 View on GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)

# Project 2
with col2:
    st.markdown("""
    <div class="card">
        <img src ='https://user-images.githubusercontent.com/98814867/159731156-2f00d42b-31fa-45c1-9b17-92d97cbff9a5.jpg' width=600 >
        <h3 style='color:#334155'>🍽 Restaurant Data Visualization</h3>
        <p>
            Collaborative data visualization project delivering insights
            for restaurant business strategy.
        </p>
        <ul>
            <li>Power BI dashboards</li>
            <li>Customer & sales trend analysis</li>
            <li>Data cleaning and storytelling</li>
        </ul>
        <a href="https://github.com/UmrahJaved/Data-visualization-of-restaurant-dataset" target="_blank">
            🔗 View on GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)

#Project 3
with col3:
    st.markdown("""
    <div class="card">
        <img src='https://user-images.githubusercontent.com/96992159/153191172-fc943e5f-ff48-446f-8a41-25cd799fe487.PNG' width=400>
        <h3 style='color:#334155'>📈 Challenge Data Analysis</h3>
        <p>
            Cleansed and analyzed a real-world dataset to extract key business
            insights and visualize trends with Python and data visualization libraries.
        </p>
        <ul>
            <li>Data cleaning & preprocessing</li>
            <li>Exploratory data analysis (EDA using Python)</li>
            <li>Visualization of key performance indicators</li>
        </ul>
        <a href="https://github.com/UmrahJaved/challenge-data-analysis-1" target="_blank">
            🔗 View on GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)

#Experience
st.markdown(
            "<h3 style='color:#334155;'>💼 Experience</h3>",
            unsafe_allow_html=True)


st.markdown("""
**Python Data Scientist & AI Developer**  
UNBLND – Ubigreat, Brussels  
*Sept 2022 – Dec 2022*

- Applied AI & NLP techniques to improve recommendation systems  
- Transitioned ML prototypes into production  
- Validated data pipelines and models  
""")

st.markdown("""
**AI Junior Developer Trainee**  
BeCode, Brussels  
*Jan 2022 – Aug 2022*

- Built end-to-end AI & data analytics solutions  
- Developed dashboards, prediction APIs & ML models  
- Collaborated in Agile teams with testing & QA focus  
""")

# Education
st.markdown(
            "<h3 style='color:#334155;'>🎓 Education</h3>",
            unsafe_allow_html=True)


st.markdown("""
- **AI & Data Science Bootcamp** — BeCode, Brussels  
- **Bachelor of Commerce** — Aligarh Muslim University, India  
""")


# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
<center>
<p>© 2026 Umrah Javed • Built with Streamlit</p>
</center>
""", unsafe_allow_html=True)
