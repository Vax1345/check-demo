import streamlit as st
from PIL import Image
import datetime

# --- לוגו עליון ודגלון ---
st.markdown("""
    <div style='display: flex; align-items: center;'>
        <img src='https://i.imgur.com/V5yEq5G.png' width='45'/>
        <div style='margin-right: 12px;'>
            <span style='font-size:2.3em;font-weight:700'>התפעול העורפי מציג:</span><br/>
            <span style='font-size:1.3em;'>בדיקת צ׳קים אוטומטית</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("העלה תמונה של צ׳ק (עדיף תמונה ברורה, ישרה וללא השתקפויות).")
uploaded_file = st.file_uploader("בחר קובץ תמונה", type=["jpg", "jpeg", "png"])

def analyze_check(image):
    # הדגמת פלט — אפשר להחליף ל־OCR אמיתי בקלות
    return {
        "מוטב": "קובי מנדלוביץ'",
        "סכום בספרות": "240,300",
        "סכום במילים": "מאתיים ארבעים אלף ושלוש מאות",
        "תאריך": "10.8.25",
        "יש תיקון בשדה סכום": True,
        "חתימה ליד התיקון": False,
        "תיקון בשדה מוטב": True,
        "חתימה ליד תיקון המוטב": False,
        "חסרה חתימת מושך": True,
        "למוטב בלבד": False,
        "קרוס": False,
        "אי התאמה סכום": True,
    }

if uploaded_file is not None:
    st.image(uploaded_file, caption='התמונה שהעלית', use_column_width=True)
    st.markdown("---")
    st.header("📋 דו\"ח אוטומטי:")

    # *** כאן תכניס קריאה ל־OCR אמיתי אם תרצה בעתיד ***
    analysis = analyze_check(uploaded_file)

    # מציג שגיאות
    errors = []
    if analysis["יש תיקון בשדה סכום"] and not analysis["חתימה ליד התיקון"]:
        errors.append("❌ בוצע תיקון בסכום ללא חתימה ליד התיקון")
    if analysis["תיקון בשדה מוטב"]:
        errors.append("❌ בוצע תיקון בשדה המוטב (לא חוקי)")
    if not analysis["למוטב בלבד"]:
        errors.append("❌ חסר 'למוטב בלבד' בצ׳ק")
    if not analysis["קרוס"]:
        errors.append("❌ חסר קרוס (שני פסים)")
    if analysis["אי התאמה סכום"]:
        errors.append("❌ סכום במילים לא תואם לסכום בספרות")
    if analysis["חסרה חתימת מושך"]:
        errors.append("❌ חסרה חתימת מושך")
    # תוכל להוסיף כאן עוד שגיאות מהחוקים שלך

    if not errors:
        st.success("הצ׳ק תקין ✅")
    else:
        for err in errors:
            st.error(err)

    # פירוט הערכים שחולצו
    with st.expander("פרטי הצ׳ק שחולצו:"):
        for k, v in analysis.items():
            st.write(f"**{k}**: {v}")

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#888;'>©️ תפעול עורפי 2025 — הדגמה בלבד. אין להשתמש כמערכת אמיתית.<br>פותח ע\"י GPT4o, צחי והחברים.</div>",
    unsafe_allow_html=True
)
