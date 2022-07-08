import pandas as pd
import os
from collections import defaultdict

df = pd.read_csv("/Users/wwang33/Documents/vuepress/blog-base/scripts/leetcode calendar - google.csv")
print(df.head())

for i in df.index:
    tag_str = df.at[i, 'tag']
    tags = tag_str.split("[DELIM]")
    tags_name = ", ".join(tags)
    title = df.at[i, 'title'].split("[DELIM]")[0]
    file_name = f"{df.at[i, 'frequency']}.{df.at[i, 'number']} - {title} - {df.at[i, 'difficulty']}.md"

    f = open(f"/Users/wwang33/Documents/vuepress/blog-base/docs/06.Google/01.Incomplete/{file_name}", "w")
    f.write(f"tags: [{tags_name}]")
    f.close()

