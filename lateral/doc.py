class LateralDoc():
    def __init__(self, data):
        for k, v in data.items():
            setattr(self, k, v)

    def __repr__(self):
        return '[{0}] {1}...'.format(self.document_id, self.text[:50])
