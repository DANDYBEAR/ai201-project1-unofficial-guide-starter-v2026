# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
The questions that are written need to be answered from the best document it can match. It needs to find evidence that is actually useful, the 4 of 5 target allows for some margin of error. 


---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
The system runs by giving an answer with evidence from a corpus, making the documents the sources of truth. If there is no named document we cannot verify the answer given.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
This gate ensures that questions that are clearly not in the corpuses are rejected, while also giving some room for error.

---

## 4. Something about your chunks

All 5 test questions should be a chunk, 100 character minimum with a complete thought that does not cut off mid sentence.


**Why this target:**
When chunks are too small they are not big enough provide context or are sometimes not even full thoughts. This would make my answer a lot weaker and the search harder. The 100 charcater minimum ensures that each chunk is enough to support an answer and not big enough that would require a large dataset.

---

## 5. Your choice

For at least 4 of the 5 test questions, the answer directly addresses the question and does not provide unsupported details or made up information.

**Why this target:**
The system is mean to be infromative/ helpful while also being certain. The main issue is not an incorrect corpus, but an answer sounds correct even when sureness is low. The 4 of 5 keeps the standard high to eliminate bad answers while allowing room for extremes.

---

