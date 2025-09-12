# adaptive_engine.py
import random

# item_bank list loader
import json
with open("data/item_bank.json","r") as f:
    ITEM_BANK = json.load(f)

def topic_mastery(mastery_map, topic):
    d = mastery_map.get(topic, {"correct":0,"total":0})
    if d["total"] == 0:
        return 0.5
    return d["correct"]/d["total"]

def select_next_questions(mastery_map, num=5):
    # sort topics by mastery ascending (weaker first)
    topics = sorted(list({it["topic_tag"] for it in ITEM_BANK}), key=lambda t: topic_mastery(mastery_map,t))
    chosen = []
    for t in topics[:3]:
        pool = [it for it in ITEM_BANK if it["topic_tag"]==t]
        chosen.append(random.choice(pool))
    while len(chosen) < num:
        chosen.append(random.choice(ITEM_BANK))
    return chosen
