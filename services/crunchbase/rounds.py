from services.db.database import RoundImport


class CrunchbaseRounds():
    def unchecked_round_imports(self, limit=40):
        return (
            RoundImport
            .select()
            .where(RoundImport.checked == False)
        )
