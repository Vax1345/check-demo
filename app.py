import streamlit as st
from PIL import Image

st.title("בדיקת צ׳קים דמו - תפעול עורפי אוטומטי")

st.write("העלה קובץ תמונה של צ׳ק (1.jpg, 2.jpg, 3.jpg, 4.jpg):")
uploaded_file = st.file_uploader("בחר קובץ", type=["jpg", "jpeg", "png"])

def analyze_check(filename):
    # מפה פשוטה לפי שם קובץ – בקלות אפשר לשפר אחר כך!
    results = {
        "1": {
            "דו\"ח": [
                "❌ חסר שם מוטב",
                "❌ עבר זמנו",
                "✅ סכום במילים תואם לסכום בספרות"
            ]
        },
        "2": {
            "דו\"ח": [
                "❌ בוצע תיקון בספרות ללא חתימה ליד התיקון",
                "❌ בוצע שינוי אסור בשדה המוטב",
                "❌ סכום במילים לא תואם לספרות (חסרה המילה 'אלף')",
                "❌ עבר זמנו",
                "✅ שם מוטב: קובי מנדלוביץ'"
            ]
        },
        "3": {
            "דו\"ח": [
                "✅ שם מוטב: ישראל ישראלסקי",
                "✅ סכום בספרות: 23,400",
                "❌ עבר זמנו"
            ]
        },
        "4": {
            "דו\"ח": [
                "❌ סכום במילים לא תואם לספרות ('הרבה מאוד כסף')",
                "❌ שם מוטב אינו קיים (מעמד הביניים)",
                "❌ עבר זמנו"
            ]
        }
    }
    base = filename.split(".")[0]
    return results.get(base, {"דו\"ח": ["⚠️ לא נמצא מידע לדוגמה עבור הצ׳ק הזה"]})

if uploaded_file is not None:
    st.image(uploaded_file, caption='התמונה שהעלית', use_column_width=True)
    st.markdown("---")
    st.header("📋 דו\"ח אוטומטי לצ׳ק:")

    analysis = analyze_check(uploaded_file.name)
    for row in analysis["דו\"ח"]:
        if "✅" in row:
            st.success(row)
        elif "❌" in row:
            st.error(row)
        else:
            st.info(row)

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#888;'>©️ תפעול עורפי 2025 — דמו בלבד. אין להשתמש כמערכת אמיתית.</div>",
    unsafe_allow_html=True
)