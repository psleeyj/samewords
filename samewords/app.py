import streamlit as st
import pandas as pd
from analysis import analyze_scenario, context_sensitivity_score
from data.scenarios import SCENARIOS

st.set_page_config(page_title="SameWords", page_icon="🧠", layout="wide")
st.title("SameWords")
st.caption("Measuring how conversational context changes AI interpretations of ambiguous language.")

with st.sidebar:
    st.header("Experiment")
    selected = st.selectbox("Choose a scenario", list(SCENARIOS.keys()))
    model_name = st.selectbox("Model", ["facebook/bart-large-mnli"])
    run = st.button("Run analysis", type="primary", use_container_width=True)

scenario = SCENARIOS[selected]
st.subheader("Target sentence")
st.info(f'“{scenario["sentence"]}”')

c1, c2 = st.columns(2)
with c1:
    st.markdown("### Context A")
    st.write(scenario["context_a"])
with c2:
    st.markdown("### Context B")
    st.write(scenario["context_b"])

st.markdown("### What SameWords tests")
st.write(
    "The same words can communicate different meanings depending on context. "
    "SameWords compares a model's interpretation with no context, Context A, and Context B."
)

if run:
    labels = scenario["labels"]
    with st.spinner("Running the language model..."):
        no_context = analyze_scenario(scenario["sentence"], "", labels, model_name)
        a_result = analyze_scenario(scenario["sentence"], scenario["context_a"], labels, model_name)
        b_result = analyze_scenario(scenario["sentence"], scenario["context_b"], labels, model_name)

    rows = []
    for label in labels:
        rows.append({
            "Interpretation": label,
            "No context": no_context.get(label, 0.0),
            "Context A": a_result.get(label, 0.0),
            "Context B": b_result.get(label, 0.0),
        })
    df = pd.DataFrame(rows).set_index("Interpretation")

    st.markdown("## Results")
    st.dataframe(df.style.format("{:.1%}"), use_container_width=True)

    chart_df = df.reset_index().melt(
        id_vars="Interpretation", var_name="Condition", value_name="Probability"
    )
    st.bar_chart(chart_df, x="Condition", y="Probability", color="Interpretation", use_container_width=True)

    sensitivity = context_sensitivity_score(a_result, b_result, labels)
    dominant_a = max(a_result, key=a_result.get)
    dominant_b = max(b_result, key=b_result.get)

    m1, m2 = st.columns(2)
    m1.metric("Context sensitivity", f"{sensitivity:.2f}")
    m2.metric("Top interpretation changed?", "Yes" if dominant_a != dominant_b else "No")

    st.caption(
        "SameWords measures model behavior, not whether AI experiences emotions or understands language like humans."
    )
else:
    st.markdown("## Example research questions")
    st.write(
        "- Does added context change a model's interpretation?\n"
        "- Which types of ambiguous language are most context-sensitive?\n"
        "- Does confidence improve when useful context is added?\n"
        "- Are sarcasm, emotion, and indirect requests equally difficult?"
    )
