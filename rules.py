SYNONYMS = {
    "维生素B2": "核黄素",
    "婴幼儿": "婴儿",
    "拉肚子": "腹泻"
}


def clean_output(data, schema):
    entities = data.get("entities", [])
    relations = data.get("relations", [])
    tokens = data.get("tokens", [])

    # 文本归一
    for ent in entities:
        ent["type"] = normalize_text(ent["type"])

    # 过滤非法关系
    valid_relations = []
    for rel in relations:
        head_idx, tail_idx, rel_type = rel.get("head"), rel.get("tail"), rel.get("type")

        # 索引越界检查（直接跳过非法关系）
        if (
            head_idx is None or tail_idx is None
            or head_idx < 0 or head_idx >= len(entities)
            or tail_idx < 0 or tail_idx >= len(entities)
        ):
            continue

        head = entities[head_idx]
        tail = entities[tail_idx]

        # 获取约束
        constraint = schema.get(rel_type, None)
        if constraint is None:
            continue

        # 多个可选约束
        if isinstance(constraint, list):
            valid = any(head["type"] == c[0] and tail["type"] == c[1] for c in constraint)
        else:
            valid = (head["type"] == constraint[0] or constraint[0] == "*") \
                 and (tail["type"] == constraint[1] or constraint[1] == "*")

        if not valid:
            continue

        # 对称关系去重
        if rel_type == "alias_of":
            if {"head": tail_idx, "tail": head_idx, "type": rel_type} in valid_relations:
                continue

        # 冲突关系处理
        if rel_type == "not_suitable_for":
            valid_relations = [
                r for r in valid_relations if not (
                    r["type"] == "suitable_for" and r["head"] == head_idx and r["tail"] == tail_idx
                )
            ]

        valid_relations.append(rel)

    return {"tokens": tokens,"entities": entities, "relations": valid_relations}


def normalize_text(text):
    return SYNONYMS.get(text, text)