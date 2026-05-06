import streamlit as st
import pandas as pd
from src.agents import run_system
from src.rag import load_knowledge, build_index, retrieve

st.title("🚦 AI Smart Traffic Control System")

query = st.text_input("Ask Traffic Insight")

if st.button("Analyze Traffic"):
    
    df, prediction, signal, state = run_system()
    
    st.subheader("📊 Traffic Data")
    st.dataframe(df)
    
    st.subheader("📈 Prediction")
    st.write(f"Next Traffic Volume: {prediction:.2f}")
    
    st.subheader("🚦 Signal Optimization")
    st.write(signal)
    
    st.line_chart(df.set_index("time")["vehicles"])
    
    # RAG
    docs = load_knowledge()
    index = build_index(docs)
    
    if query:
        insights = retrieve(query, docs, index)
        
        st.subheader("🔎 Insights")
        for i in insights:
            st.write(i)