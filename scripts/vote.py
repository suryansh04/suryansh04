"""Count one vote from an issue titled 'vote: <topic>'.

Reads ISSUE_TITLE and VOTER from the environment (never interpolated into shell),
accepts only topics already in votes.json, allows one vote per GitHub account,
and writes the reply for the issue comment to reply.txt."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "..", "votes.json")

title = os.environ.get("ISSUE_TITLE", "")
voter = os.environ.get("VOTER", "").lower()
topic = title.split(":", 1)[1].strip().lower() if ":" in title else ""

data = json.load(open(PATH))
topics = data["topics"]
voters = data.setdefault("voters", [])

if topic not in topics:
    options = ", ".join(sorted(topics))
    reply = f"I couldn't find **{(topic[:40] or 'that topic')}** on the list. Open options: {options}. Use the links on my profile to vote."
    changed = False
elif voter in voters:
    reply = f"Thanks @{voter}! You've already voted, so this one isn't counted. One vote per account keeps it fair."
    changed = False
else:
    topics[topic] += 1
    voters.append(voter)
    json.dump(data, open(PATH, "w"), indent=2, sort_keys=True)
    open(PATH, "a").write("\n")
    leader = max(topics.items(), key=lambda kv: kv[1])
    reply = (f"Vote counted for **{topic}**. Thanks @{voter}! "
             f"It's now at {topics[topic]}. Current leader: **{leader[0]}** ({leader[1]}). "
             "The chart on my profile updates in a minute.")
    changed = True

open(os.path.join(HERE, "..", "reply.txt"), "w").write(reply)
print("changed" if changed else "unchanged")
sys.exit(0)
