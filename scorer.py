import re


def judge(question, expects, answer, results) -> bool:
    """Return whether the answer contains every expected fact."""
    del question, results  # Required by run_eval.py; not needed for this rule.

    if not isinstance(expects, str) or not expects.strip():
        return False
    if not isinstance(answer, str) or not answer.strip():
        return False

    answer_words = set(re.findall(r"[a-z0-9]+", answer.casefold()))
    connector_words = {"a", "an", "and", "at", "by", "from", "in", "of", "the", "to"}

    for expected_fact in expects.split(","):
        expected_words = {
            word
            for word in re.findall(r"[a-z0-9]+", expected_fact.casefold())
            if word not in connector_words
        }
        if not expected_words or not expected_words.issubset(answer_words):
            return False

    return True
