from fastapi import APIRouter, Depends, HTTPException, status
from fama_models import RSSFeed, RSSFeedItem, Article
from fama_processing import FeedParser
from typing import List

# Declare Router
router = APIRouter()


# Query
@router.post("/", response_model=Article)
async def query(): #query: Query
    """
    Query Articles
    """
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Query not yet Implemented")


# Query Feeds
@router.get("/feeds", response_model=RSSFeed)
async def query_feeds():
    """
    Query Feeds
    """
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Query not yet Implemented")


# Query Articles
@router.get("/articles", response_model=Article)
async def query_articles():
    """
    Query Articles
    """
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Query not yet Implemented")
