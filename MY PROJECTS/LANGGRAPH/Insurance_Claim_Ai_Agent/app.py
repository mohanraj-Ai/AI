import streamlit as st
from PIL import Image
import os
from graph.graph import app

st.set_page_config(
    page_title="Insurance Claim AI Agent",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Insurance Claim AI Agent")
st.write("Upload a damaged vehicle image and analyze the insurance claim.")

uploaded_file = st.file_uploader(
    "Upload Accident Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    os.makedirs("temp", exist_ok=True)

    image_path = os.path.join("temp", uploaded_file.name)

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Analyze Claim"):

        with st.spinner("Analyzing..."):

            state = {
                "image_path": image_path
            }

            result = app.invoke(state)

        st.success("Analysis Completed")

        # ------------------------
        # Vision Output
        # ------------------------
        st.header("🔍 Damaged Parts")

        vision = result["vision_output"]

        st.write("### Severity")
        st.write(vision["severity"])

        st.write("### Damage Summary")
        st.write(vision["damage_summary"])

        st.write("### Damaged Parts")

        for part in vision["damaged_parts"]:
            st.write("✅", part)

        # ------------------------
        # Cost Estimation
        # ------------------------
        st.header("💰 Repair Cost")

        cost = result["cost_estimation"]

        st.dataframe(cost["replaced_parts"])

        col1, col2, col3 = st.columns(3)

        col1.metric("Parts Cost", f"₹{cost['parts_cost']:,}")
        col2.metric("Labour Cost", f"₹{cost['labor_cost']:,}")
        col3.metric("Total Cost", f"₹{cost['total_cost']:,}")

        # ------------------------
        # Policy
        # ------------------------
        st.header("📄 Policy Analysis")

        st.write(result["policy_answer"])

        # ------------------------
        # Final Decision
        # ------------------------
        st.header("✅ Final Decision")

        decision = result["final_decision"]

        st.write("### Claim Status")
        st.success(decision["claim_status"])

        st.write("### Approved Amount")
        st.write(f"₹{decision['approved_amount']}")

        st.write("### Reason")
        st.write(decision["reason"])