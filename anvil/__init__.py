import builtins
print(2)
from anvil.module.logger import Logger

log = Logger().log_to_file(__file__)
setattr(builtins, "log", log)
