from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import AnyUrl
from fama_models import RSSFeed, RSSFeedItem
from fama_processing import FeedParser
from typing import List

# Declare Router
router = APIRouter()


# Endpoint
@router.get("/url", response_model=RSSFeed)
async def feed_by_url(feed_url: AnyUrl):
    """
    Retrieve Feed by URL
    """
    try:
        feed = FeedParser.parse_feed(feed_url)
        return feed
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{feed_id}", response_model=RSSFeed, include_in_schema=False)
async def feed_by_id(feed_id: str):
    """
    Retrieve Feed by ID
    """
    return {}


# Endpoint
@router.get("/url/entries", response_model=List[RSSFeedItem])
async def feed_entries_by_url(feed_url: AnyUrl):
    """
    Retrieve Feed Entries by URL
    """
    try:
        items = FeedParser.parse_items(feed_url)
        return items
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{feed_id}/entries", response_model=List[RSSFeedItem], include_in_schema=False)
async def feed_entries_by_id(feed_id: str):
    """
    Retrieve Feed Entries by ID
    """
    return {}
