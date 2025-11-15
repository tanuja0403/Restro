import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'
RESERVATIONS_FILE = DATA_DIR / 'reservations.json'


class ReservationAgent:
    def __init__(self):
        # very small simple reservation store
        if not RESERVATIONS_FILE.exists():
            RESERVATIONS_FILE.write_text('[]')

    def list_reservations(self):
        return json.loads(RESERVATIONS_FILE.read_text())

    def create_reservation(self, name, time, party_size=2):
        reservations = self.list_reservations()
        new = {'name': name, 'time': time, 'party_size': party_size}
        reservations.append(new)
        RESERVATIONS_FILE.write_text(json.dumps(reservations, indent=2))
        return new
