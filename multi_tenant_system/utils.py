from __future__ import unicode_literals, absolute_import

import arrow
from arrow import Arrow

# TIMESTAMPS
def get_current_utc() -> Arrow:
    return arrow.now('UTC')


def get_current_utc_timestamp() -> int:
    return get_current_utc().timestamp