import datetime

from services.db.database import DbSingleton, Round, RoundImport
from services.rounds import Rounds


def test_round_import_with_lead_investor():
    db = DbSingleton.get_instance()
    db.prep_test()

    # create mock objects
    RoundImport.create(
        uuid='asdf',
        name='Test Name',
        type='person',
        permalink='test-name',
        cb_url='https://hi.com',
        rank=100,
        created_at=datetime.date.today(),
        updated_at=datetime.date.today(),
        country_code='US',
        # TODO: other properties
    )

    # TODO: create other mock objects

    # call the service you'll write
    Rounds().create_new_rounds()

    # NOTE: the complier bitches unless you add database=None to Peewee queries. :facepalm:
    cb_round = Round.select().first(database=None)
    assert cb_round.Lead_Investor__c == 'Nick Weber'

    assert cb_round.Amount__c > 500000


def test_round_import_with_unqualified_rounds():
    # TODO: write a test to show that given two RoundImports, one with a qualifying `Amount___c` and another without
    # that the application properly skips the unqualified round import.
    pass
