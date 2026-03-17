from collections import deque

# 1. Initialize
application_inbox = deque()   # queue
processed_history = []        # stack

# 2. Ingest Data
raw_data = ["  techcorp ", "bio-gen ", " AI Labs", "fintech  ", "  health-plus"]

for item in raw_data:
    clean_item = item.lower().strip()
    application_inbox.append(clean_item)

# 3. Process (FIFO)
while application_inbox:
    name = application_inbox.popleft()
    print(f"Approving: {name}")
    processed_history.append(name)

# 4. Undo (LIFO)
if processed_history:
    last_processed = processed_history.pop()
    print(f"Reverting approval for: {last_processed}")