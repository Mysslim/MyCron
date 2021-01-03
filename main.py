from croniter import croniter
from datetime import datetime
base = datetime(2010, 1, 25, 4, 46)
iter = croniter('*/5 * * * *', base)  # every 5 minutes
print(iter.get_next(datetime))   # 2010-01-25 04:50:00
print(iter.get_next(datetime))   # 2010-01-25 04:55:00
print(iter.get_next(datetime))   # 2010-01-25 05:00:00