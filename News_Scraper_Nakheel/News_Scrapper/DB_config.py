# -*- coding: utf-8 -*-
BOT_NAME = 'News_Scrapper'
SPIDER_MODULES = ['News_Scrapper.spiders']
NEWSPIDER_MODULE = 'News_Scrapper.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'News_Scrapper.pipeline.MongoDBPipeline': 100
}
DOWNLOAD_DELAY = 2
MONGODB_HOST = 'ac-fziuve1-shard-00-01.rpnhqpi.mongodb.net'
MONGODB_PORT = 27017
MONGODB_USER = 'raed98'
MONGODB_PASS = 'morErWCVfjE90uxz'
MONGODB_DB = 'News_Scrapper'
MONGODB_COLLECTION = 'News'
# -*- coding: utf-8 -*-
BOT_NAME = 'News_Scrapper'
SPIDER_MODULES = ['News_Scrapper.spiders']
NEWSPIDER_MODULE = 'News_Scrapper.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'News_Scrapper.pipeline.MongoDBPipeline': 100
}
DOWNLOAD_DELAY = 2
MONGODB_HOST = 'ac-fziuve1-shard-00-01.rpnhqpi.mongodb.net'
MONGODB_PORT = 27017
MONGODB_USER = 'raed98'
MONGODB_PASS = 'morErWCVfjE90uxz'
MONGODB_DB = 'News_Scrapper'
MONGODB_COLLECTION = 'News'
