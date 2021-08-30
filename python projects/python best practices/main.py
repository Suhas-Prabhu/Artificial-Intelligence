from tqdm import tqdm
import os

# use tqdm to check the progress of loop
for i in tqdm(range(10),desc="Looping through the loop"):
    pass

# In a scenario where the user can pass an undisclosed or uncertain number of parameters, use “args” and “kwargs”. You should remember the following purpose of both the keywords.
# Args is used to specify an unknown number of positional arguments

# Kwargs is used to specify an unknown number of keyword arguments

# args
def count_files_in_dir(project_root_dir, *fpaths: str):
      for path in fpaths:
            rel_path = os.path.join(project_root_dir, path)
            print(path, ":", len(os.listdir(rel_path)))
count_files_in_dir("Artificial-Intelligence", "Computer Vision projects","Sentiment Analysis")

# kwargs
def print_results(**results):
      for key, val in results.items():
          print(key,"asdfaf",val)
print_results(clf = "SVM", score = 98.2, time_taken = 1.28, split_size = 0.8, tuning = False)