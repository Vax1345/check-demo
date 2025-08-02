import streamlit as st
from PIL import Image

st.markdown("""
    <div style='display: flex; align-items: center;'>
        <img src='https://i.imgur.com/V5yEq5G.png' width='45'/>
        <div style='margin-right: 12px;'>
            <span style='font-size:2.3em;font-weight:700'>בדיקת צ׳קים דמו - תפעול עורפי אוטומטי</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("העלה קובץ תמונה של צ׳ק (1.jpg, 2.jpg, 3.jpg, 4.jpg) להדגמה:")

uploaded_file = st.file_uploader("בחר קובץ", type=["jpg", "jpeg", "png"])

# ----- פונקציית הדגמה: מחזירה תוצאה לפי שם הקובץ בלבד -----
def analyze_check_demo(filename):
    # השמות שמגיעים מ־st.file_uploader
    demo_checks = {
        "1.jpg": {
            "סכום בספרות": "23,000",
            "סכום במילים": "עשרים ושלוש אלף ש״ח",
            "שגיאות": [
                "❌ חסר שם מוטב",
                "❌ עבר זמנו של הצ׳ק"
            ]
        },
        "2.jpg": {
            "סכום בספרות": "240,300",
            "סכום במילים": "מאתיים ארבעים ושלוש מאות",
            "שם מוטב": "קובי מנדלוביץ'",
            "שגיאות": [
                "❌ בוצע תיקון בספרות ללא חתימה ליד התיקון",
                "❌ בוצע תיקון בשדה המוטב (אסור)",
                "❌ עבר זמנו של הצ׳ק",
                "❌ סכום במילים לא תואם לסכום הספרות (חסרה המילה 'אלף')"
            ]
        },
        "3.jpg": {
            "סכום בספרות": "23,400",
            "סכום במילים": "עשרים ושלושה אלף ש״ח",
            "שם מוטב": "ישראל ישראלסקי",
            "שגיאות": [
                "❌ עבר זמנו של הצ׳ק"
            ]
        },
        "4.jpg": {
            "סכום בספרות": "1,000,000",
            "סכום במילים": "הרבה מאוד כסף",
            "שם מוטב": "מעמד הביניים",
            "שגיאות": [
                "❌ סכום במילים לא תואם לסכום בספרות",
                "❌ שם המוטב אינו על שם הנחזה",
                "❌ עבר זמנו של הצ׳ק"
            ]
        },
    }
    # תומך גם ב-Check1.jpg, Check2.jpg וכו'
    if filename.lower().startswith("check"):
        key = filename.lower().replace("check", "").replace(".jpg", "") + ".jpg"
        return demo_checks.get(key)
    return demo_checks.get(filename)

if uploaded_file is not None:
    st.image(uploaded_file, caption='התמונה שהעלית', use_container_width=True)
    st.markdown("---")
    st.header("📋 דו\"ח אוטומטי לצ׳ק:")

    result = analyze_check_demo(uploaded_file.name)
    if result:
        for err in result.get("שגיאות", []):
            st.error(err)
        with st.expander("פרטי הצ׳ק שחולצו:"):
            for k, v in result.items():
                if k != "שגיאות":
                    st.write(f"**{k}**: {v}")
    else:
        st.warning("⚠️ לא נמצא מידע לדוגמה עבור הצ׳ק הזה.")

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#888;'>©️ תפעול עורפי 2025 — דמו בלבד. אין להשתמש כמערכת אמיתית.<br>פותח ע\"י GPT4o, צחי והחברים.</div>",
    unsafe_allow_html=True
)
