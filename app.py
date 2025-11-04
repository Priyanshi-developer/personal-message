import streamlit as st

# ------------------ PAGE SETUP ------------------
st.set_page_config(page_title="Secret Message App", page_icon="💖", layout="centered")

# ------------------ PASSWORD PROTECTION ------------------
PASSWORD = "devil"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Password Protected App")
    password_input = st.text_input("Enter Password:", type="password")
    
    if st.button("Login"):
        if password_input == PASSWORD:
            st.session_state.authenticated = True
            st.success("Access Granted ✅")
            st.rerun()
        else:
            st.error("❌ Incorrect Password")

# ------------------ MAIN APP ------------------
else:
    st.title("💬 Click Message App")

    if "click_count" not in st.session_state:
        st.session_state.click_count = 0

    # One button only
    if st.button("Click Me ❤️"):
        st.session_state.click_count += 1
        if st.session_state.click_count > 3:
            st.session_state.click_count = 1  # Reset after 3 clicks

    # ---- Message Display ----
    if st.session_state.click_count == 1:
        st.markdown("""
            <div style='background-color:#87CEFA; padding:40px; border-radius:15px; text-align:center;'>
                <h2 style='color:white; font-size:2em;'>😔 Sorry</h2>
            </div>
        """, unsafe_allow_html=True)

    elif st.session_state.click_count == 2:
        st.markdown("""
            <div style='background-color:#32CD32; padding:40px; border-radius:15px; text-align:center;'>
                <h2 style='color:white; font-size:2em;'>😊 Thank You</h2>
            </div>
        """, unsafe_allow_html=True)

    elif st.session_state.click_count == 3:
        st.markdown("""
            <div style='background-color:pink; padding:40px; border-radius:15px; text-align:center;'>
                <h2 style='color:red; font-size:2em;'>❤️ I Love You ❤️</h2>
            </div>
        """, unsafe_allow_html=True)

