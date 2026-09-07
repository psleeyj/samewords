from functools import lru_cache

@lru_cache(maxsize=4)
def _get_pipeline(model_name):
    from transformers import pipeline
    return pipeline("zero-shot-classification", model=model_name)

def analyze_scenario(sentence, context, labels, model_name="facebook/bart-large-mnli"):
    classifier = _get_pipeline(model_name)
    text = f"Context: {context}\nStatement: {sentence}" if context.strip() else f"Statement: {sentence}"
    result = classifier(text, candidate_labels=labels, multi_label=False)
    return {label: float(score) for label, score in zip(result["labels"], result["scores"])}

def context_sensitivity_score(a, b, labels):
    # Total variation distance: 0 = identical, 1 = maximally different
    return 0.5 * sum(abs(a.get(label, 0.0) - b.get(label, 0.0)) for label in labels)
