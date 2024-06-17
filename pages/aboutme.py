import streamlit as st

st.title("ABOUT MYSELF")

st.markdown("---")
image_paths = ["pict/self.png"]

cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)

st.header("👧🌹 INFANTE, MIKEE BIANAN")
st.markdown("---")


st.markdown("""
##### ♡∞  FAMILY MEMBERS ♡∞ 

* 👩‍👦 Mother's Name: Mila Elcy B. Infante
* 👨‍👧‍👧 Father's Name: Paquito D. Infante
* 👭🏻 Brother's Name: Montrel B. Infante
* 👭🏻 Sister's Name: Myrell B. Infante
* 👭🏻 Sister's Name: Michelle B. Infante
* 👭🏻 Sister's Name: Mellissa B. Infante
* 👭🏻 Brother's Name: Melvin B. Infante
* 👭🏻 Sister's Name: Meagan B. Infante
                

### 🔎 OVERVIEW
""", unsafe_allow_html=True)

# Personal Information
st.header("🧚PERSONAL INFORMATION 🧚")
st.write("**Name:** Mikee B. Infante 😊")
st.write("**Age:** 21 years old 🎂")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY 🎓")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student 💻📚")

with st.expander("GET TO KNOW ME MORE:⬇️"):
    st.markdown("""   
    #
Ten years from now, I envision myself as a thriving entrepreneur. 
Although I won't be directly applying my Information Systems degree, 
I will leverage my skills in data analysis, software development, and problem-solving to forge a new path. 
I see myself leading a successful venture that harmoniously blends my passion for technology with my creative inclinations,
potentially in digital art or interactive storytelling. This business will not only ensure my financial stability but also 
utilize technology to positively impact people's lives.
    """, unsafe_allow_html=True)


# Favorites
st.header("Favorite Quotes")
st.write("1. \"Discover who you truly are and embody that person. Your soul was placed on this earth to fulfill that purpose. Uncover your truth, live authentically, and everything will naturally align.\"")
st.write("2. \"The greatest triumph in life does not come from never falling, but from persevering and rising stronger each time we encounter setbacks.\"")
st.write("3. \"You will undoubtedly face numerous setbacks in life, but never allow yourself to be defeated by them.\"")

st.header("Favorite Song")
st.write("1. *\"Enchanted\"*")
st.write("2. *\"Lover\"*")
st.write("3. *\"Love Story\"*")

st.header("Favorite Food")
st.write("1. *\"Avocado Smoothie\"*")
st.write("2. *\"Vanilla Ice Cream\"*")
st.write("3. *\"Chicken Adobo\"*")



import streamlit as st


images = [
    {"path": "./pict/fam.jpg", "caption": "The thing that matters most in the end is not the number of breaths we take, but the moments that take our breath away. And it's those moments, I believe, that we share with our family. -Leo Buscaglia "},
    {"path": "./pict/love.jpg", "caption": "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage. - Lao Tzu"},
    {"path": "./pict/friend3.jpg", "caption": "Friendship is a precious gift that life gives us, to lighten our burdens and double our joys. - Epicurus"}
]


st.title("🖼️ FAVORITE PHOTOS 🖼️")


for image in images:
    st.image(image["path"], caption=image["caption"])



st.markdown(
    """
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
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### * * * Thank you for visiting my profile! * * * ")
