"""
LESSON 1 - The Python you actually need
=======================================

YOU type the answers. Then run the file. It checks your work and tells
you what's wrong. Get all 6 green and you're done.

    python3 ~/journey_to_ML/lessons/02_python_you_need.py

Nothing to install. No API key. Real HYDTP data.
"""

import json
import os

# Use the full local HYDTP dataset if it's on this machine; otherwise fall back
# to the 200-post public sample that ships with this repo, so the lesson runs
# for anyone who clones it.
HERE = os.path.dirname(os.path.abspath(__file__))
FULL = "/home/yuvaraj-ambati/HCP/hcp/data/posts/all_posts.json"
DATA = FULL if os.path.exists(FULL) else os.path.join(HERE, "data", "hydtp_sample.json")

# json.load() reads a file of text and turns it into Python dicts and lists.
# This one line is how almost all data gets into a Python program.
everything = json.load(open(DATA, encoding="utf-8"))

# `everything` is a dict. A dict maps a KEY to a VALUE, like a phone book.
# Its keys are: "last_updated", "taxonomy", "posts"
# You get a value out with square brackets:
posts = everything["posts"]

# `posts` is a LIST - an ordered pile of things. Each thing is one tweet,
# and each tweet is itself a dict. Here is the first one:
first = posts[0]          # [0] means "the first item". Counting starts at 0.


# ─────────────────────────────────────────────────────────────────
# EXERCISE 1 - how many tweets are there?
# len() gives the length of a list.
# Replace None with the right expression.
# ─────────────────────────────────────────────────────────────────
total_tweets = None


# ─────────────────────────────────────────────────────────────────
# EXERCISE 2 - get the TEXT of the first tweet.
# `first` is a dict. One of its keys is "text".
# ─────────────────────────────────────────────────────────────────
first_text = None


# ─────────────────────────────────────────────────────────────────
# EXERCISE 3 - count the English tweets.
# Every post has a "language" key. Loop over posts, add 1 each time
# the language is "english".
#
#   count = 0
#   for post in posts:
#       if post["language"] == "english":
#           count = count + 1
#
# Write that loop yourself, then set english_count = count
# ─────────────────────────────────────────────────────────────────
english_count = None


# ─────────────────────────────────────────────────────────────────
# EXERCISE 4 - count tweets per time slot.
# Every post has "time_slot": morning / afternoon / evening / night.
# Build a dict like {"morning": 412, "afternoon": 508, ...}
#
# Starting point:
#   slots = {}
#   for post in posts:
#       slot = post["time_slot"]
#       if slot not in slots:
#           slots[slot] = 0
#       slots[slot] = slots[slot] + 1
#
# Then set slot_counts = slots
# ─────────────────────────────────────────────────────────────────
slot_counts = None


# ─────────────────────────────────────────────────────────────────
# EXERCISE 5 - find every tweet mentioning Panjagutta.
# `"abc" in some_text` is True if abc appears anywhere in it.
# Careful: tweets write it different ways, so lowercase the text first
# with post["text"].lower() and search for "panjagutta".
# Build a LIST of the matching posts.
#
#   found = []
#   for post in posts:
#       if "panjagutta" in post["text"].lower():
#           found.append(post)
# ─────────────────────────────────────────────────────────────────
panjagutta_posts = None


# ─────────────────────────────────────────────────────────────────
# EXERCISE 6 - write a FUNCTION.
# A function is a named piece of code you can reuse.
# This one takes one post and returns its list of topics.
# The topics live at post["tags"]["topics"] - a dict inside a dict.
# Some posts have no tags, so return an empty list [] if anything is missing.
#
#   def get_topics(post):
#       tags = post.get("tags")       # .get() returns None instead of crashing
#       if not tags:
#           return []
#       return tags.get("topics", [])
# ─────────────────────────────────────────────────────────────────
def get_topics(post):
    return None          # <- replace this whole line with the real body


# ═════════════════════════════════════════════════════════════════
#  Don't edit below here. This checks your answers.
# ═════════════════════════════════════════════════════════════════

def check(n, what, got, ok, hint):
    if got is None:
        print(f"  [ ] {n}. {what:<34} not attempted yet")
    elif ok:
        print(f"  [x] {n}. {what:<34} correct  ->  {str(got)[:44]}")
    else:
        print(f"  [!] {n}. {what:<34} not right yet")
        print(f"         you have: {str(got)[:60]}")
        print(f"         hint:     {hint}")

print("\n" + "=" * 66)
print("  LESSON 1 - The Python you actually need")
print("=" * 66 + "\n")

check(1, "total_tweets", total_tweets,
      total_tweets == len(posts), "len(posts)")

check(2, "first_text", first_text,
      isinstance(first_text, str) and "HYDTP" in first_text,
      'first["text"]')

check(3, "english_count", english_count,
      english_count == sum(1 for p in posts if p.get("language") == "english"),
      "loop over posts, count language == 'english'")

check(4, "slot_counts", slot_counts,
      isinstance(slot_counts, dict) and sum(slot_counts.values()) == len(posts),
      "every post lands in exactly one slot, so the totals must add to len(posts)")

check(5, "panjagutta_posts", panjagutta_posts,
      isinstance(panjagutta_posts, list)
      and len(panjagutta_posts) == sum(1 for p in posts
                                       if "panjagutta" in p.get("text", "").lower()),
      "lowercase the text before searching")

try:
    r6 = get_topics(first)
    ok6 = isinstance(r6, list) and r6 == first.get("tags", {}).get("topics", [])
except Exception as e:
    r6, ok6 = f"crashed: {e}", False
check(6, "get_topics(first)", r6, ok6, 'post["tags"]["topics"], safely')

done = sum([
    total_tweets == len(posts),
    isinstance(first_text, str) and "HYDTP" in first_text,
    english_count == sum(1 for p in posts if p.get("language") == "english"),
    isinstance(slot_counts, dict) and sum(slot_counts.values()) == len(posts) if slot_counts else False,
    isinstance(panjagutta_posts, list) and len(panjagutta_posts) > 0,
    ok6,
])
print(f"\n  {done} of 6 done.\n")
