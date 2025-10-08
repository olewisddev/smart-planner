from pydantic import BaseModel
from datetime import date


class Campaign(BaseModel):
    client: str
    platform: str
    buy_type: str
    objective: str
    placement: str
    cpu: str
    est_kpi: str
    cost: str
    campaign_name: str
    start: date
    end: date
