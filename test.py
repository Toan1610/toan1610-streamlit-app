import streamlit as st

st.title("🚀 Startup Idea Generator")

form = st.form(key="user_settings")
with form:
    # User input - Industry name
    industry_input = st.text_input("Industry", key="industry_input")

    # Create a two-column view
    col1, col2 = st.columns(2)

    with col1:
        # User input - The number of ideas to generate
        num_input = st.slider("Number of ideas", value=3, key="num_input", min_value=1, max_value=10)

    with col2:
        # User input - The 'temperature' value representing the level of creativity
        creativity_input = st.slider("Creativity", value=0.5, key="creativity_input", min_value=0.1, max_value=0.9)

    # Submit button to start generating ideas
    generate_button = form.form_submit_button("Generate Idea")

if generate_button:
    if industry_input == "":
        st.error("Industry field cannot be blank")
    else:
        my_bar = st.progress(0.05)
        st.subheader("Startup Ideas")
        for i in range(num_input):
            st.markdown("""---""")
            startup_idea = generate_idea(industry_input, creativity_input)
            startup_name = generate_name(startup_idea, creativity_input)
            st.markdown("##### " + startup_name)
            st.write(startup_idea)
            my_bar.progress((i + 1) / num_input)
