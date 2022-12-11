import time

import requests
from typing import Dict, Optional, Tuple

from constants import MAX_PAGES, WB_URL
from loggers import logger
from osm_utils import get_wb_dest


def parse_query(
    id: int,
    query_string: str,
    coords: Optional[Tuple[float, float]] = None
) -> Tuple[int, int, Optional[Dict]]:
    if coords:
        dest_str = ','.join(map(str, get_wb_dest(coords[0], coords[1])))
        logger.info(dest_str)
        url = WB_URL + '&dest=' + dest_str
    else:
        url = WB_URL + '&dest=-1075831,-77677,-398551,12358499'
    for i in range(MAX_PAGES):
        page_num, query = i + 1, query_string.lower()
        url += f'&page={page_num}&&query={query}'
        page = requests.get(url).json()
        if 'data' in page:
            products = page['data']['products']
            lp = len(products)
            for j in range(lp):
                if products[j]['id'] == id:
                    return i, j, products[j]
            time.sleep(2)
    return -1, -1, None


if __name__ == '__main__':
    id = 37260674
    query = 'Omega 3'
    print(*parse_query(id, query))
