# coin_tracker_assigment
"""Transfer detector.

Given a list of withdrawals and desposits, detect the likely transfers amongst them.

A few notes:
- The same withdrawal or deposit cannot be used for multiple different transfers. If there's a case where 
a given withdrawal or deposit can be matched with multiple possible transfers, use the first occurrence 
in the list.
- A transfer can only be made between different wallets.

For example, given:
[
	('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 5.3),  # 5.3 BTC was withdrawn out of 'wallet_id_1'
	('tx_id_2', 'wallet_id_1', '2020-01-03 12:05:25 UTC', 'out', 3.2),  # 3.2 BTC was withdrawn out of 'wallet_id_1'
	('tx_id_3', 'wallet_id_2', '2020-01-01 15:30:20 UTC', 'in', 5.3),   # 5.3 BTC was deposited into 'wallet_id_2'
	('tx_id_4', 'wallet_id_3', '2020-01-01 15:30:20 UTC', 'in', 5.3),   # 5.3 BTC was deposited into 'wallet_id_3'
]

Expected output:
[
	('tx_id_1', 'tx_id_3'),
]

Add a few tests to verify your implementation works on a variety of input
"""
