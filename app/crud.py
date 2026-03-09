from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
import secrets

async def create_api_key(db: AsyncSession, name: str = None) -> models.APIKey:
    key = secrets.token_urlsafe(32)
    db_key = models.APIKey(key=key, name=name)
    db.add(db_key)
    await db.commit()
    await db.refresh(db_key)
    return db_key

async def get_api_key(db: AsyncSession, key: str) -> models.APIKey | None:
    result = await db.execute(select(models.APIKey).where(models.APIKey.key == key))
    return result.scalar_one_or_none()

async def create_subscription(db: AsyncSession, sub: schemas.SubscriptionCreate, api_key_id: int) -> models.Subscription:
    db_sub = models.Subscription(**sub.dict(), api_key_id=api_key_id)
    db.add(db_sub)
    await db.commit()
    await db.refresh(db_sub)
    return db_sub

async def get_active_subscriptions(db: AsyncSession) -> list[models.Subscription]:
    result = await db.execute(
        select(models.Subscription).where(models.Subscription.is_active == True)
    )
    return result.scalars().all()