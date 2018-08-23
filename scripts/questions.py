import json
from anvil.module.api import APIARY


x = APIARY()
for _ in range(1000):
    log.info(x.post_question(question="Number {}: Bantai kya swaal hai".format(_), choices=["Zhakaas", "Lageli hai bhidu"]))
