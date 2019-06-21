import torch
# the number of entries in our database
num_entries = 5000
db = torch.rand(num_entries) > 0.5
db
db, pdbs = create_db_and_parallels(5000)
def query(db):
    return db.sum()
full_db_result = query(db)
sensitivity = 0
for pdb in pdbs:
    pdb_result = query(pdb)
    
    db_distance = torch.abs(pdb_result - full_db_result)
    
    if(db_distance > sensitivity):
        sensitivity = db_distance
sensitivity

