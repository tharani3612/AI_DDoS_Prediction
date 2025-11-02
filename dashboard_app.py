import streamlit as st
from real_time_detection import detect_ddos

st.title("AI-Based DDoS Attack Prediction System")

st.write("Enter the following features (comma-separated):")
st.write("packets_per_second, bytes_per_second, avg_packet_size, flow_duration, unique_src_ips, unique_dst_ports")

input_data = st.text_input("Example: 1500,1200000,450,2.5,120,5")

if st.button("Predict"):
    try:
        data = [float(x.strip()) for x in input_data.split(",")]
        result = detect_ddos(data)
        st.success(result)
    except:
        st.error("Invalid input format. Please enter 6 numeric values separated by commas.")
