 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/app.py b/app.py
new file mode 100644
index 0000000000000000000000000000000000000000..38df3a1970a0e9c9d7540dc62f2c8afe470f7caa
--- /dev/null
+++ b/app.py
@@ -0,0 +1,30 @@
+import streamlit as st
+
+st.set_page_config(page_title="Questionnaire", page_icon="📝")
+
+st.title("Quick Questionnaire")
+st.write("Please answer all five questions and submit to see a summary of your responses.")
+
+with st.form("questionnaire_form"):
+    name = st.text_input("1. What is your name?")
+    role = st.selectbox("2. What best describes your role?", ["Student", "Professional", "Manager", "Other"])
+    experience = st.slider("3. How many years of experience do you have?", 0, 30, 5)
+    favorite_tool = st.text_input("4. What is your favorite productivity tool?")
+    newsletter = st.radio("5. Would you like to receive our newsletter?", ["Yes", "No"], horizontal=True)
+
+    submitted = st.form_submit_button("Submit")
+
+if submitted:
+    st.subheader("Summary")
+    st.write("Here are your responses:")
+    st.markdown(
+        "\n".join(
+            [
+                f"- **Name:** {name or 'Not provided'}",
+                f"- **Role:** {role}",
+                f"- **Experience:** {experience} years",
+                f"- **Favorite tool:** {favorite_tool or 'Not provided'}",
+                f"- **Newsletter:** {newsletter}",
+            ]
+        )
+    )
 
EOF
)