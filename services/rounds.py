from services.crunchbase.rounds import CrunchbaseRounds
from services.db.database import Round


class Rounds():
    def create_new_rounds(self):
        batch = self.__round_import_batch()
        while len(batch) > 0:
            for round_import in batch:
                self.__process_round_import(round_import)
            batch = self.__round_import_batch()

    def __round_import_batch(self):
        return CrunchbaseRounds().unchecked_round_imports()

    def __process_round_import(self, round_import):
        # TODO: your job :)
        Round.create(
            # TODO: create properties of the rounds
        )
        round_import.checked = True
        round_import.save()
