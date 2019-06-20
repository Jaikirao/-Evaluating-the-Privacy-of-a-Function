import torch
# the number of entries in our database
num_entries = 5000
db = torch.rand(num_entries) > 0.5
db
