import os

ENV = os.environ.get('ENV') or 'test'


class Config:
    pass


class TestingConfig(Config):
    mongo_uri = 'mongodb://localhost:27017/',
    database = 'lab_server_test'


class ProductionConfig(Config):
    mongo_uri = 'mongodb://localhost:27017/',
    database = 'lab_server_production'


class TestingTable(Config):
    person = 'person_test'  # 人员资料
    report = 'report_test'  # 组会汇报
    paper = 'paper_test'    # 论文资源


class ProductionTable(Config):
    person = 'person'
    report = 'report'
    paper = 'paper'


config = TestingConfig()
table = TestingTable()

if ENV == 'production':
    config = ProductionConfig()
    table = ProductionTable()
