import streamlit as st
from PIL import Image

# --- לוגו וסלוגן ---
st.markdown("""
<div style='text-align:center;'> <img src="https://raw.githubusercontent.com/Vax1345/check-demo/main/AISelect_20250802_213329_Chrome.jpg" width="110"/><br>
  <span style="font-size:1.3em; font-weight:800; color:{color}">{icons[ok]} לא מוותרים על בן אדם בבנק
</span>div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- העלאת תמונה ---
st.markdown("### 📲 העלה תמונה של צ'ק לבדיקה:")

uploaded_file = st.file_uploader("בחר קובץ (JPG, PNG)", type=["jpg", "jpeg", "png"])

def analyze_check(filename):
    fname = filename.lower()
    results = {
        "check1.jpg": {
            "שדות": [
                ("שם מוטב", False),
                ("סכום בספרות", True),
                ("סכום במילים", True),
                ("עבר זמנו", True),
                ("חתימת מושך", False),
                ("קרוס", False),
            ]
        },
       EXAMPLES=
    "Check1.jpg": {
        "שם מוטב": "לא קיים",
        "סכום בספרות": "23,000",
        "סכום במילים": "עשרים ושלש אלף ש\"ח",
        "תאריך": "30.09.2018 - עבר זמנו",
        "חתימת מושך": "קיימת",
        "למוטב בלבד": "תקין (אם גרוס)",
        "שגיאות": [
            "חסר שם מוטב",
            "עבר זמנו"
        ]
    },
    "Check2.jpg": {
        "שם מוטב": "קובי מנדלוביץ'",
        "סכום בספרות": "240,300",
        "סכום במילים": "מאתיים ארבעים של מאות",
        "תאריך": "10.06.25 - תקין",
        "חתימת מושך": "תקין",
        "למוטב בלבד": "תקין",
        "שגיאות": [
            "אי התאמה בין מילים לספרות",
            "חסרה חתימה ליד התיקון בספרות",
            "בוצע תיקון בשם המוטב",
            "בוצע שינוי אסור בצ׳ק"
        ]
    },
    # כאן תוכל להמשיך להוסיף עוד צ׳קים
} "check3.jpg": {
            "שדות": [
                ("שם מוטב", True),
                ("סכום בספרות", True),
                ("סכום במילים", True),
                ("עבר זמנו", True),
                ("חתימת מושך", True),
                ("קרוס", True),
            ]
        },
        "check4.jpg": {
            "שדות": [
                ("שם מוטב", False),
                ("סכום בספרות", True),
                ("סכום במילים", False),
                ("עבר זמנו", True),
                ("חתימת מושך", False),
                ("קרוס", False),
            ]
        }
    }
    return results.get(fname, None)
# --- תצוגה "אפליקציה" של בדיקת שדות ---
def render_fields(fields):
    icons = {True: "✅", False: "❌"}
    for name, ok in fields:
        color = "#27ae60" if ok else "#e74c3c"
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: space-between; background: #262d36; border-radius: 12px; padding: 10px 16px; margin: 5px 0;">
                <span style="color: #fff; font-size: 1.15em;">{name}</span>
                <span style="font-size :1.3em; font-weight: 800; color:{color}'>{icons[ok]}</span>
            </div>
            """, unsafe_allow_html=True
        )

if uploaded_file:
    st.image(uploaded_file, caption='התמונה שהעלית', use_container_width=True)
    st.markdown("### תוצאות הבדיקה:")

    result = analyze_check(uploaded_file.name)
    if result:
        render_fields(result["שדות"])
    else:
        st.warning("לא נמצאה דוגמת בדיקה עבור הצ'ק הזה.")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- קרדיט תחתון ---
st.markdown("""
<div style='text-align:center;font-size:0.97em;color:#777;padding:12px;'>
    <img src='https://i.imgur.com/tT1QpLS.png' width='48' style='vertical-align:middle; margin-bottom:3px;'/>
    <br>©️ תפעול עורפי — 2025 | דמו בלבד | אין להסתמך על הבדיקה<br>
    Powered by GPT-4o, צחי, והחברים
</div>
""", unsafe_allow_html=True)
