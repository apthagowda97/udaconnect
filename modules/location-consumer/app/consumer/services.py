import logging
from datetime import datetime, timedelta
from typing import Dict, List

from db_conf import Base,Session
from consumer.models import Location
from consumer.schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("location-consumer")

db = Session()

class LocationService:

    def create(location: Dict):

        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        db.add(new_location)
        db.commit()

        return new_location