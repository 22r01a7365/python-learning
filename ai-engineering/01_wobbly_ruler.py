"""
LESSON 1 DEMO - "at high temperature, your eval set stops working"

Setup:
  You have 100 real HYDTP tweets. A human wrote down the correct tag
  for each one. That is your EVAL SET.

  You have two prompts:
      PROMPT A - the one running today
      PROMPT B - a new one you wrote, GENUINELY better (87% vs 85%)

  You want your eval set to tell you "yes, B is better, ship it."

  Question: does it?
"""

import json
import os

# Use the full local HYDTP dataset if it's on this machine; otherwise fall back
# to the 200-post public sample that ships with this repo, so the lesson runs
# for anyone who clones it.
HERE = os.path.dirname(os.path.abspath(__file__))
FULL = "/home/yuvaraj-ambati/HCP/hcp/data/posts/all_posts.json"
DATA = FULL if os.path.exists(FULL) else os.path.join(HERE, "data", "hydtp_sample.json")
import random

posts = json.load(open(DATA, encoding="utf-8"))["posts"]
eval_set = posts[:100]

# Every tweet has a fixed "difficulty" from 0.00 to 1.00.
# Easy tweets (low number) get tagged right by any prompt.
# This never changes - it's a property of the tweet, not the model.
difficulty = {}
rng = random.Random(42)
for post in eval_set:
    difficulty[post["id"]] = rng.random()

PROMPTS = {
    "PROMPT A (current)": 0.85,   # handles tweets up to difficulty 0.85
    "PROMPT B (new)":     0.87,   # handles tweets up to difficulty 0.87  <- better
}


def tag_one(post, prompt_quality, temperature):
    """Tag ONE tweet. Returns True if the tag is correct."""
    settled_answer = difficulty[post["id"]] < prompt_quality

    # temperature = the chance the model ignores its best answer
    # and picks something else instead
    if random.random() < temperature:
        return random.random() < 0.5      # coin toss instead
    return settled_answer                 # its actual best answer


def score(prompt_quality, temperature):
    """Run the whole 100-tweet eval set once. Returns accuracy out of 100."""
    return sum(tag_one(p, prompt_quality, temperature) for p in eval_set)


def experiment(temperature, label):
    print("\n" + "=" * 64)
    print(f"  TEMPERATURE {temperature}  -  {label}")
    print("=" * 64)

    for name, quality in PROMPTS.items():
        runs = [score(quality, temperature) for _ in range(5)]
        spread = max(runs) - min(runs)
        print(f"\n  {name}")
        print(f"    same eval set, run 5 times : {runs}")
        print(f"    spread                     : {spread} points")

    print(f"\n  Now the decision you actually have to make.")
    print(f"  You run each prompt once and compare. 10 times over:\n")
    wrong = 0
    for i in range(10):
        a, b = score(0.85, temperature), score(0.87, temperature)
        ok = b > a
        if not ok:
            wrong += 1
        print(f"    try {i+1:>2}:  A={a:>3}   B={b:>3}   your eval says "
              f"{'B is better  ok' if ok else 'A is better  WRONG'}")
    print(f"\n  B is truly better. Your eval got it wrong {wrong} times out of 10.")


experiment(0.0, "model is consistent")
experiment(0.6, "model is moody")
print()
