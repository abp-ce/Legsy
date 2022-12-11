from dataclasses import dataclass
from typing import List, Tuple

import requests

from constants import OSM_URL


@dataclass
class OsmItem:
    place_id: int
    parent_place_id: int
    osm_id: int


def make_osm_relations_list(place_id: int) -> List[OsmItem]:
    osm_list = []
    while place_id != 0:
        url = OSM_URL + f'details?format=json&place_id={place_id}'
        result = requests.get(url).json()
        item = OsmItem(
            place_id=result['place_id'],
            parent_place_id=result['parent_place_id'],
            osm_id=result['osm_id']
        )
        osm_list.append(item)
        place_id = item.parent_place_id

    return osm_list


def get_wb_dest(lat: float, lon: float) -> Tuple[int]:
    url = OSM_URL + f'reverse?format=json&lat={lat}&lon={lon}'
    result = requests.get(url).json()
    osm_list = make_osm_relations_list(result["place_id"])
    return (-osm_list.pop().osm_id, -osm_list.pop().osm_id,
            -osm_list.pop().osm_id, 12358499)


if __name__ == '__main__':
    lat, lon = 54.487966, 53.476754
    dest_str = ','.join(map(str, get_wb_dest(lat, lon)))
    print(dest_str)
