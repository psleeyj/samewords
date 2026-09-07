SCENARIOS = {
    "You're really early": {
        "sentence": "Wow, you're really early.",
        "context_a": "Alex arrived twenty minutes before everyone else.",
        "context_b": "Alex arrived forty minutes late after everyone had been waiting.",
        "labels": ["sincere praise", "sarcasm", "uncertain"],
    },
    "I'm fine": {
        "sentence": "I'm fine.",
        "context_a": "Jordan just received good news and is smiling while talking with a friend.",
        "context_b": "Jordan just had an argument, has become unusually quiet, and avoids eye contact.",
        "labels": ["genuinely okay", "upset but hiding it", "uncertain"],
    },
    "That's interesting": {
        "sentence": "That's interesting.",
        "context_a": "A student enthusiastically explains a new idea and the listener asks follow-up questions.",
        "context_b": "A student gives an awkward presentation and the listener quickly changes the subject.",
        "labels": ["genuine interest", "polite disapproval", "uncertain"],
    },
    "It's getting late": {
        "sentence": "It's getting pretty late.",
        "context_a": "Two friends are studying and one notices they both have an early class tomorrow.",
        "context_b": "A host says this to a guest who has stayed long after everyone else has left.",
        "labels": ["literal observation", "indirect request to leave", "uncertain"],
    },
    "Great job": {
        "sentence": "Great job.",
        "context_a": "A teammate successfully finishes a difficult task and the group celebrates.",
        "context_b": "A teammate accidentally deletes the shared file right before the deadline.",
        "labels": ["sincere praise", "sarcasm", "uncertain"],
    },
}
