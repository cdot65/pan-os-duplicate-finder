# pan_os_duplicate_finder/utilities/analysis.py

from typing import Dict, List, Tuple
from collections import defaultdict
from panos.objects import AddressObject


def find_duplicate_objects(
    address_objects: List[Tuple[str, AddressObject]]
) -> Dict[str, List[Tuple[str, AddressObject]]]:
    """
    Find duplicate address objects based on their values.

    Args:
        address_objects: List of tuples containing (device_group_name, address_object)

    Returns:
        Dictionary mapping value keys to lists of matching address objects
    """
    value_map = defaultdict(list)

    for dg_name, obj in address_objects:
        if hasattr(obj, "value") and obj.value:
            key = f"{obj.type}:{obj.value}"
            value_map[key].append((dg_name, obj))

    return {k: v for k, v in value_map.items() if len(v) > 1}
