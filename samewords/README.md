# SameWords

**SameWords** is an interactive NLP experiment that measures how conversational context changes an AI model's interpretation of ambiguous language.

> How much can the meaning of the same words change when the surrounding context changes?

SameWords compares model interpretations across controlled contextual conditions rather than treating sarcasm, emotion, or indirect language as simple yes/no classification problems.

## What it does

For each scenario, the app evaluates the same sentence under:
1. no context
2. Context A
3. Context B

A pretrained zero-shot language model assigns probabilities to possible interpretations. The app then calculates a **context sensitivity score** using total variation distance.

## Example

**Sentence:** `Wow, you're really early.`

- Context A: Alex arrived 20 minutes early.
- Context B: Alex arrived 40 minutes late.

Possible interpretations:
- sincere praise
- sarcasm
- uncertain

## Tech stack

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Pandas
- Zero-shot natural language inference

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The first run downloads the pretrained Hugging Face model.

## Research directions

Possible extensions:
- compare multiple language models
- test sarcasm, emotion, irony, and indirect requests separately
- measure confidence calibration
- progressively add or remove context
- analyze which contextual cues most strongly change predictions

## Resume description

**SameWords | Python, NLP, Streamlit**

- Developed an experimental NLP application to quantify how conversational context changes model interpretations of ambiguous and nonliteral language.
- Evaluated model behavior across controlled context conditions and implemented a context-sensitivity metric to compare interpretation distributions.

## Responsible use

SameWords studies model behavior. It does not claim that AI experiences emotion or understands language in the same way humans do, and it should not be used to diagnose real people.
