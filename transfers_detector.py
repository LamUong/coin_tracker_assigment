'''
To run this you just need a standard python interpreter.
'''
from collections import OrderedDict

def detect_transfers(transactions):
  transfer_map = {}
  for trans in transactions:
    tx_id, wallet_id, date, transfer_type, amount = trans
    key = (date, transfer_type, amount)
    if key not in transfer_map:
      transfer_map[key] = OrderedDict()
    transfer_map[key][tx_id] = wallet_id

  transactions_output = []
  
  for trans in transactions:
    tx_id, wallet_id, date, transfer_type, amount = trans
    this_tx_key = (date, transfer_type, amount)
    
    if this_tx_key in transfer_map and tx_id in transfer_map[this_tx_key] :
      other_tx_type = 'in' if transfer_type == 'out' else 'out'
      other_tx_key = (date, other_tx_type, amount)
      
      if other_tx_key in transfer_map and len(transfer_map[other_tx_key]) > 0:
        other_tx_id,  other_wallet_id = transfer_map[other_tx_key].popitem(last=False)
        
        # We do not want a transfer from a Wallet Id to itself. 
        if wallet_id == other_wallet_id and len(transfer_map[other_tx_key]) > 0:
          other_tx_id_2,  other_wallet_id_2 = transfer_map[other_tx_key].popitem(last=False)
          transactions_output.append((tx_id,  other_tx_id_2))
          transfer_map[other_tx_key][other_tx_id] = other_wallet_id
          transfer_map[other_tx_key].move_to_end(other_tx_id, last=False)
        elif wallet_id != other_wallet_id:
          transactions_output.append((tx_id,  other_tx_id))
        
        del transfer_map[this_tx_key][tx_id]
  return transactions_output

test_1 = [
	('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 5.3), 
	('tx_id_2', 'wallet_id_1', '2020-01-03 12:05:25 UTC', 'out', 3.2), 
	('tx_id_3', 'wallet_id_2', '2020-01-01 15:30:20 UTC', 'in', 5.3),
	('tx_id_4', 'wallet_id_3', '2020-01-01 15:30:20 UTC', 'in', 5.3),   
]
'''
original example, 	('tx_id_1', 'tx_id_3')
'''
test_2 = [
	('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 5.3), 
	('tx_id_2', 'wallet_id_1', '2020-01-03 12:05:25 UTC', 'out', 3.2), 
	('tx_id_3', 'wallet_id_2', '2020-01-01 15:30:20 UTC', 'in', 5.3),
	('tx_id_4', 'wallet_id_2', '2020-01-03 12:05:25 UTC', 'in', 3.2),   
]
'''
	('tx_id_1', 'tx_id_3'), ('tx_id_2, 'tx_id_4') 
'''
test_3 = [
	('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 3.2),  
	('tx_id_2', 'wallet_id_2', '2020-01-01 15:30:20 UTC', 'in', 3.2),  
	('tx_id_3', 'wallet_id_3', '2020-01-01 15:30:20 UTC', 'in', 3.2),  
]
'''
	('tx_id_1', 'tx_id_2') Selects tx_id_2 because it is first in the list, eventhough tx_id_1, tx_id_3 is possible
'''
test_4 = [
	('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 3.2),  
	('tx_id_2', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'in', 3.2),  
	('tx_id_3', 'wallet_id_3', '2020-01-01 15:30:20 UTC', 'out', 3.2),  
  ('tx_id_4', 'wallet_id_3', '2020-01-01 15:30:20 UTC', 'in', 3.2),  
]
'''
CANNOT be [('tx_id_1', 'tx_id_2'), ('tx_id_3', 'tx_id_4')] since sending from a wallet to itself is silly.
Better be [('tx_id_1', 'tx_id_4'), ('tx_id_2', 'tx_id_3')]

'''
print(detect_transfers(test_4))


