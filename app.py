import streamlit as st
from PIL import Image

st.set_page_config(page_title="בדיקת צ׳קים דמו", page_icon=":money_with_wings:", layout="centered")

st.markdown("""
    <div style='display: flex; align-items: center; justify-content: center; gap: 18px; margin-bottom: 0.6em;'>
        <img src='https://cdn-icons-png.flaticon.com/512/3514/3514347.png' width='50'/>
        <div>
            <span style='font-size:2.2em;font-weight:800;color:#fff;'>בדיקת צ׳קים דמו</span><br/>
            <span style='font-size:1.1em;color:#ccc;'>התפעול העורפי מציג — ניתוח אוטומטי</span>
        </div>
    </div>
""", unsafe_allow_html=True)

with st.expander("🛈 איך זה עובד?", expanded=False):
    st.write("""
    העלה תמונה של צ׳ק (jpg / png), והמערכת תנתח אוטומטית ותציג לך שגיאות ומידע רלוונטי.
    זו הדגמה בלבד (המידע מזוהה לפי שם הקובץ — הכל לשואו).
    """)
    st.write("🟢 תומך בצ׳קים לדוגמה, אפשר להעלות כמה שבא לך.")

uploaded_file = st.file_uploader("העלה צ׳ק לבדיקה אוטומטית:", type=["jpg", "jpeg", "png"])

def analyze_check_demo(filename):
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
        with st.expander("📑 פרטי הצ׳ק שחולצו:"):
            for k, v in result.items():
                if k != "שגיאות":
                    st.write(f"**{k}**: {v}")
    else:
        st.warning("⚠️ אין מידע לדוגמה עבור הצ׳ק הזה.\nנסה להעלות אחד מהצ׳קים לדוגמה.")

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#aaa; font-size:0.95em;'>©️ תפעול עורפי 2025 — דמו בלבד. אין להשתמש כמערכת אמיתית.<br>פותח ע\"י GPT4o, צחי והחברים.</div>",
    unsafe_allow_html=True
)
