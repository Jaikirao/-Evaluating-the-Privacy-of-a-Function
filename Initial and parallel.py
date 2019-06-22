def sensitivity(query,n_enteries=1000):
  db, pdbs = create_db_and_parallel(n_enteries)
  full_db_result = query(db)
  max_distance = 0
  for pdb in pdbs:
    
    pdb_result = query(pdb)
    
    db_distance = torch.abs(pdb_result - full_db_result)
    
    if(db_distance > max_distance):
        max_distance = db_distance
  return max_distance

#now we make a another query fuction
def query(db):
    return db.float().mean()
sensitivity(query)

db, pdbs = create_db_and_parallel(20)
db
pdbs

