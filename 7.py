keys = ["name", "description", "title", "keywords","content","charset"]
values = ["document","The best document","My document","doc, word,excel","None"]

result_dict = {keys[i]: values[i] for i in range(min(len(keys), len(values)))}

print(result_dict)
