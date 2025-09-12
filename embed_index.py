# embed_index.py
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

MODEL_NAME = "all-MiniLM-L6-v2"

def build_index(item_bank_path="data/item_bank.json", index_out="faiss.index", map_out="item_map.json"):
    model = SentenceTransformer(MODEL_NAME)
    with open(item_bank_path, "r") as f:
        items = json.load(f)
    texts = [it["prompt_text"] + " " + it["solution_text"] for it in items]
    embs = model.encode(texts, show_progress_bar=True)
    embs = np.array(embs).astype("float32")
    d = embs.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(embs)
    faiss.write_index(index, index_out)
    # mapping
    item_map = [{"id": it["id"], "topic_tag": it["topic_tag"], "difficulty": it["difficulty"]} for it in items]
    with open(map_out, "w") as f:
        json.dump(item_map, f)
    print("Index built:", index_out)

if __name__ == "__main__":
    build_index()
