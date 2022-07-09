import pandas as pd
import os
from collections import defaultdict

df = pd.read_csv("./leetcode calendar - google.csv")
print(df.head())

id_filename_map = {}

for i in df.index:
    tag_str = df.at[i, 'tag']
    tags = tag_str.split("[DELIM]")
    tags_name = ", ".join(tags)
    title = df.at[i, 'title'].split("[DELIM]")[0].replace("?", "")
    file_name = f"{'{:03}'.format(df.at[i, 'frequency'])}.{df.at[i, 'number']} - {title} - {df.at[i, 'difficulty']}.md"
    id = df.at[i, 'number']
    id_filename_map[id] = file_name 
    
# print(id_filename_map)

    # f = open(f"/Users/wwang33/Documents/vuepress/Google - 03.Incomplete/{file_name}", "w")
    # f.write(f"tags: [{tags_name}]")
    # f.close()


import os, sys

# Open a file
path = '/Users/wwang33/Documents/vuepress/blog-base/docs/02.LS/02.LS - completed'
dirs = os.listdir( path )

# This would print all the files and directories
cnt = 0
for file in dirs:
   if file.endswith("md"):
        ls_id = file.split(".")[1].split("-")[0].strip()
        if id in id_filename_map:
            cnt += 1
            print(ls_id)
            os.rename(f"{path}/{file}", f"/Users/wwang33/Documents/vuepress/Google - 03.Incomplete/{id_filename_map[id]}")

print(cnt)



