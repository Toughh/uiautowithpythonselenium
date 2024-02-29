class ProofOfIdentity:

    def __init__(self, pick_a_country: str, identity_type: str):
        self._pick_a_country = pick_a_country
        self._identity_type = identity_type

    def get_pick_a_country(self) -> str:
        return self._pick_a_country

    def set_pick_a_country(self, val: str):
        self._pick_a_country = val

    def get_identity_type(self) -> str:
        return self._identity_type

    def set_identity_type(self, val: str):
        self._identity_type = val
