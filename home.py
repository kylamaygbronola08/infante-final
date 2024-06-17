import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
 [
    Page("home.py", "APPLICATION OF MACHINE LEARNING", "👩‍💻"),
    Section("THE APPLICATION OF LEARNINGS"),
    Page("pages/aboutme.py", "ABOUT MYSELF", "📝", in_section=True),
    Page("pages/description.py", "DESCRIPTION OF APPLICATIONS", "📋", in_section=True),
    Page("pages/itqmtlearnings.py", "LEARNINGS", "📘", in_section=True),

    Section("PROJECTS", "💾"),
    Page("pages/prediction.py", "MILK QUALITY PREDICTION", "🥛", in_section=True),
    Page("pages/sentimentemotion.py", "EMOTION ANALYZER", "🧠", in_section=True),
    Page("pages/imageclassifier.py", "IMAGE CLASSIFICATION", "🖼️", in_section=True),

    Section("SOURCE CODE", "📄"),
    Page("pages/prediction_src.py", "PREDICTION SOURCE CODE", "🔍", in_section=True),
    Page("pages/sentimentemotionanalyzer_src.py", "EMOTION ANALYZER SOURCE CODE", "🔎", in_section=True),
    Page("pages/imageclassifier_src.py", "IMAGE CLASSIFICATION SOURCE CODE", "🔍", in_section=True),
]
)

hide_pages(["Thank you"])

st.header("👧INFANTE, MIKEE BIANAN")
st.subheader("Final Requirements in ITEQMT")

st.markdown("---")

st.image("pict/self.png")

# Display info box
st.info("⚙️This application illustrates various machine learning methods applied in quality management, enhancing our effectiveness and productivity as students.🤖")

# Display divider
st.markdown("---")


st.image("pict/ML2.jpg")

# Display more markdown content
st.write("""
#
Machine learning is a powerful technology that teaches computers to learn and make decisions based on data patterns, rather than relying on explicit programming instructions.
In image classification, machine learning algorithms can be trained to automatically recognize and categorize objects within images, such as identifying whether a photo contains a dog or a cat. 
Emotion analysis involves using machine learning to interpret emotions from text or speech, enabling applications to understand and respond to human sentiments expressed in online reviews or conversations. 
Additionally, machine learning excels in prediction tasks by analyzing historical data to forecast future outcomes, such as predicting customer preferences or medical diagnoses.
These applications are crucial because they automate complex processes, enhance decision-making accuracy, and drive innovation across industries like healthcare, finance, and entertainment. 
By continuously learning from data, machine learning improves efficiency, reduces human error, and opens new possibilities for technological advancement and understanding

### 🌟🌟 Star the project on Github 🌟🌟 
<iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Additional custom styles
custom_styles = """
<style>
.stApp {
    background-color: #EAD8C0;
    padding: 2em;
}
 h1, h2 {
        color: #6F4E37;
    }
    .stText {
        font-size: 1.5em;
        color: #322C2B;
}
</style>
"""
st.markdown(custom_styles, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)