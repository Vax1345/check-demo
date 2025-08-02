import streamlit as st
import pandas as pd

# --- לוגו + סלוגן עם מיתוג כתום-שחור ---
st.markdown("""
<div style='text-align:center;'>
    <img src="https://raw.githubusercontent.com/Vax1345/check-demo/main/AISelect_20250802_213329_Chrome.jpg" width='100'/><br><br>
    <span style="display: inline-block; padding: 12px 24px; background: #f7941d; color: white; font-weight: bold; font-size: 1.6em; border-radius: 25px;">
        לא מוותרים על בן אדם בבנק


 style='font-size:1.1em;color:#ccc;'>התפעול העורפי מציג — ניתוח אוטומטי</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 📲 העלה תמונה של צ'ק לבדיקה:")

uploaded_file = st.file_uploader("בחר קובץ", type=["jpg", "jpeg", "png"])

# --- פונקציית ניתוח צ'ק ---
def analyze_check(filename):
    fname = filename.lower()
    results = {
        "check1.jpg": {
            "שדות": [
                ("שם מוטב", False,  "❌ חסר שם מוטב",),
                ( "סכום בספרות: "23,000", True), 
                ("סכום במילים", True "עשרים ושלוש אלף ש״ח",),
                ("עבר זמנו", False 12 09.2011),
                ("חתימת מושך", True),
                ("קרוס",True),
            ],
            "שגיאות": [,
                "❌חסר שם מוטב",
                 
                "❌ עבר זמנו של הצ׳ק"
            ]

        },
        "check2.jpg": {
            "שדות": [
                ("שם מוטב", True),
                ("סכום בספרות", True),
                ("סכום במילים", False),
                ("עבר זמנו", True),
                ("חתימה ליד תיקון", False),
                ("בוצע תיקון בשם המוטב (אסור)", True),
                ("קרוס", True),
            ],
            "שגיאות": [
                "אי התאמה בין מילים לספרות",
                "חסרה חתימה ליד התיקון בספרות",
                "בוצע תיקון בשם המוטב",
                "בוצע שינוי אסור בצ׳ק"
            ]
        },
        "check3.jpg": {
            "שדות": [
                ("שם מוטב", True),
                ("סכום בספרות", True),
                ("סכום במילים", True),
                ("עבר זמנו", True),
                ("חתימת מושך", True),
                ("קרוס", True),
            ],
            "שגיאות": []
        },
        "check4.jpg": {
            "שדות": [
                ("שם מוטב", False),
                ("סכום בספרות", True),
                ("סכום במילים", False),
                ("עבר זמנו", True),
                ("חתימת מושך", False),
                ("קרוס", False),
            ],
            "שגיאות": []
        }
    }
    return results.get(fname, None)

# --- עיצוב צבעוני לטבלה ---
def highlight_status(val):
    if "תקין" in val:
        return 'background-color: #d4edda; color: black; text-align: right; font-size: 16px;'  # ירוק בהיר
    else:
        return 'background-color: #f8d7da; color: black; text-align: right; font-size: 16px;'  # ורוד בהיר

# --- הצגת תוצאות ---
if uploaded_file:
    st.image(uploaded_file, caption="📸 הצ'ק שהועלה", use_column_width=True)
    st.markdown("---")

    check_result = analyze_check(uploaded_file.name)

    if check_result:
        st.subheader("📋 תוצאות הבדיקה")

        df = pd.DataFrame(check_result["שדות"], columns=["שדה", "תקין"])
        df["סטטוס"] = df["תקין"].apply(lambda x: "✅ תקין" if x else "❌ שגוי")
        df = df[["סטטוס", "שדה"]]  # סדר עמודות
        styled_df = df.style.applymap(highlight_status, subset=["סטטוס"]).hide(axis='index')

        st.markdown("#### 📑 בדיקת שדות:")
        st.dataframe(styled_df)

        if check_result["שגיאות"]:
            st.markdown("#### ⚠️ שגיאות בצ'ק:")
            for error in check_result["שגיאות"]:
                st.error(f"❗ {error}")
       
    else:
        st.warning("⛔ שם הקובץ לא מזוהה. ודא שהקובץ הוא check1.jpg / check2.jpg וכו', באותיות קטנות בלבד.")