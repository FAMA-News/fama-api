from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import AnyUrl
from fama_models import Article
from fama_processing import ArticleParser
from typing import List

# Declare Router
router = APIRouter()

# Endpoint
@router.get("/url", response_model=Article)
async def article_by_url(article_url: AnyUrl):
    """
    Retrieve Article by URL
    """
    try:
        article = ArticleParser.parse(article_url)
        return article
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{article_id}", response_model=Article, include_in_schema=False)
async def article_by_id(article_id: str):
    """
    Retrieve Article by ID
    """
    return {}
