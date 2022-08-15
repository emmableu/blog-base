import os, sys
import shutil

# Open a file
# path = '/Users/wwang33/Documents/vuepress/blog-base/docs/06.Google/03.Incomplete'
path = '/Users/wwang33/Documents/vuepress/Google - 03.Incomplete'
dirs = os.listdir( path )

# This would print all the files and directories
cnt = 0
for file in dirs:
    if file.endswith("md"):
        idx = file.split('.')
        newfile = f"{idx[0]}.{idx[0]} - {idx[1]}.{idx[2]}"
        os.rename(os.path.join(path,file), os.path.join(path, newfile))
        print(newfile)



# import pandas as pd
# import os
# from collections import defaultdict
#
# df = pd.read_csv("./leetcode calendar - google.csv")
# print(df.head())
#
# id_filename_map = {}
#
# for i in df.index:
#     tag_str = df.at[i, 'tag']
#     tags = tag_str.split("[DELIM]")
#     tags_name = ", ".join(tags)
#     title = df.at[i, 'title'].split("[DELIM]")[0].replace("?", "")
#     file_name = f"{'{:03}'.format(df.at[i, 'frequency'])}.{df.at[i, 'number']} - {title} - {df.at[i, 'difficulty']}.md"
#     id = df.at[i, 'number']
#     id_filename_map[id] = file_name
#
# print(id_filename_map)
#
#
#     # f = open(f"/Users/wwang33/Documents/vuepress/Google - 03.Incomplete/{file_name}", "w")
#     # f.write(f"tags: [{tags_name}]")
#     # f.close()
#
#
# import os, sys
# import shutil
#
# # Open a file
# path = '/Users/wwang33/Documents/vuepress/blog-base/docs/06.Google/02.Completed'
# dirs = os.listdir( path )
#
# # This would print all the files and directories
# cnt = 0
# for file in dirs:
#     print(file)
#     if file.endswith("md"):
#         ls_id = int(file.split(".")[1].split("-")[0].strip())
#         print(ls_id)
#         if ls_id in id_filename_map:
#             cnt += 1
#             print(ls_id)
#             print(id_filename_map[ls_id])
#             try:
#                 os.remove(f"/Users/wwang33/Documents/vuepress/Google - 03.Incomplete/{id_filename_map[ls_id]}")
#             except:
#                 continue
#             # break
#
# print(cnt)
#
#
#
