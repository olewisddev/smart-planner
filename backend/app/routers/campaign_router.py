from fastapi import APIRouter, HTTPException
from typing import Optional
from models.campaign_model import Campaign
from services.campaign_service import get_campaigns_for_client


campaign_router = APIRouter()

@campaign_router.get("/api/clients/{client_id}/campaigns")
def get_campaigns(client_id: int, buy_type: Optional[str] = None, 
                  platform: Optional[str] = None, objective: Optional[str] = None) -> dict:
    """
    Get campaigns for the predefined client, filtered by platform, objective, or buy type.
    """
    
    # Add client filtering here.    
    
    campaigns = get_campaigns_for_client(platform=platform, objective=objective, buy_type=buy_type)
    
    if not campaigns:
        raise HTTPException(status_code=404, detail="No campaigns found matching the criteria")
    
    return {
        "client": "Brewtopia Coffee House", 
        "campaigns": [
            {
                "campaign-name": campaign.campaign_name,
                "platform": campaign.platform,
                "buy-type": campaign.buy_type,
                "objective": campaign.objective,
                "placement": campaign.placement,
                "cpu": campaign.cpu,
                "est-kpi": campaign.est_kpi,
                "cost": campaign.cost,
                "start": campaign.start,
                "end": campaign.end
            }
            for campaign in campaigns
        ]
    }
