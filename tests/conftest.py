
import os

import brownie

if not brownie.network.is_connected():
    network_id = os.environ.get('BROWNIE_NETWORK_ID') or os.environ['BROWNIE_NETWORK']
    brownie.network.connect(network_id)
brownie._config.CONFIG.settings['autofetch_sources'] = True
