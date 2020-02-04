import datetime
import os

from peewee import (BooleanField, CharField, DateField, DateTimeField,
                    ForeignKeyField, IntegerField, Model, SqliteDatabase,
                    TextField)
from playhouse.sqlite_ext import JSONField

from config import settings


def table_list():
    return [Round, RoundImport, InvestmentImport, Investor, InvestorImport]


class DbSingleton:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DbSingleton.__instance == None:
            DbSingleton()
        return DbSingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DbSingleton.__instance != None:
            raise Exception(
                "This class is a singleton! Use DbSingleton.get_instance()")
        else:
            self.init_db()
            DbSingleton.__instance = self

    def prep_test(self):
        self.drop_tables()
        self.create_tables()

    def create_tables(self):
        if self.tables_created:
            return

        self.database.create_tables(
            table_list()
        )
        self.tables_created = True

    def init_db(self):
        self.tables_created = False
        self.database = SqliteDatabase(settings.database)

    def drop_tables(self):
        if settings.stage == 'test':
            self.database.drop_tables(table_list())
            self.tables_created = False
        else:
            raise Exception('You cant drop a db except for in test')


class BaseModel(Model):
    class Meta:
        database = DbSingleton.get_instance().database


class InvestmentImport(BaseModel):
    uuid = CharField(null=False, primary_key=True)
    name = CharField(null=False)
    type = CharField(null=False)
    permalink = CharField(null=False)
    cb_url = CharField(null=False)
    rank = CharField(null=True)
    created_at = DateField(null=False)
    updated_at = DateField(null=False)
    funding_round_uuid = CharField(null=False, index=True)
    funding_round_name = CharField(null=False)
    investor_uuid = CharField(null=False)
    investor_name = CharField(null=False)
    investor_type = CharField(null=False)
    is_lead_investor = BooleanField(null=False)

    class Meta:
        table_name = 'investment_imports'


class Round(BaseModel):
    Name = CharField(max_length=255, null=True)
    Company__c = CharField(max_length=255, null=True)
    Amount__c = IntegerField(null=True)
    Crunchbase_Id__c = CharField(max_length=40, null=True, index=True)
    Funding_Date__c = DateField(null=True)
    Lead_Investor__c = CharField(max_length=100, null=True)
    Series__c = CharField(max_length=20, null=True)
    Type__c = CharField(max_length=50, null=True)

    class Meta:
        table_name = 'rounds'


class Investor(BaseModel):
    Name = CharField(null=True)
    Crunchbase_Id__c = CharField(null=True, index=True)
    Round__c = CharField(null=True)
    Investor__c = CharField(null=True)
    Funding_Date__c = DateField(null=True)
    round_id = IntegerField(null=True)

    class Meta:
        table_name = 'investors'


class RoundImport(BaseModel):
    uuid = CharField(max_length=42, null=True, unique=True, primary_key=True)
    name = CharField(null=True)
    type = CharField(null=True)
    permalink = CharField(null=True)
    cb_url = CharField(null=True)
    rank = CharField(null=True)
    created_at = DateField(null=True)
    updated_at = DateField(null=True)
    country_code = CharField(null=True)
    state_code = CharField(null=True)
    region = CharField(null=True)
    city = CharField(null=True)
    investment_type = CharField(null=True)
    announced_on = DateField(null=True)
    raised_amount_usd = IntegerField(null=True)
    raised_amount = IntegerField(null=True)
    raised_amount_currency_code = CharField(null=True)
    post_money_valuation_usd = IntegerField(null=True)
    post_money_valuation = IntegerField(null=True)
    post_money_valuation_currency_code = CharField(null=True)
    investor_count = IntegerField(null=True)
    org_uuid = CharField(null=True)
    org_name = CharField(null=True)
    lead_investor_uuids = CharField(max_length=10000, null=True)
    checked = BooleanField(null=True, default=False)

    class Meta:
        table_name = 'round_imports'


class InvestorImport(BaseModel):
    uuid = CharField(max_length=42, null=True, unique=True, primary_key=True)
    name = CharField(null=True)
    type = CharField(null=True)
    permalink = CharField(null=True)
    cb_url = CharField(null=True)
    rank = IntegerField(null=True)
    created_at = CharField(null=True)
    updated_at = CharField(null=True)
    roles = CharField(null=True)
    domain = CharField(null=True)
    country_code = CharField(null=True)
    state_code = CharField(null=True)
    region = CharField(null=True)
    city = CharField(null=True)
    investor_types = CharField(null=True)
    investment_count = IntegerField(null=True)
    total_funding_usd = IntegerField(null=True)
    total_funding = IntegerField(null=True)
    total_funding_currency_code = CharField(null=True)
    founded_on = DateField(null=True)
    closed_on = DateField(null=True)
    facebook_url = CharField(null=True)
    linkedin_url = CharField(null=True)
    twitter_url = CharField(null=True)
    logo_url = CharField(null=True)

    class Meta:
        table_name = 'investor_imports'
