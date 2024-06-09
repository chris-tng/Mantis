import json
from pathlib import Path
from tqdm import tqdm
# file_list = ["data_insf.json", "data_lab.json", "data_real.json", "data_static.json", "data_worsen_gen.json"]
file_list = list([str(x) for x in Path("./").glob("data*.json")])
print(file_list)
all_data = []
for file_name in file_list:
    with open(file_name, "r") as f:
        data = json.load(f)
        for item in tqdm(data, desc=file_name):
            item['images'] = ["images/" + "/" + image for i, image in enumerate(item['images'])]
            assert all([Path(image).exists() for image in item['images']]), item['images']
            all_data.append({
                "id": item['id'],
                "images": item['images'],
                "conversations": item['conversations'],
            })
with open("train.json", "w") as f:
    json.dump(all_data, f, indent=4)