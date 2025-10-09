from fastapi import APIRouter, HTTPException
from typing import Optional
from models.campaign_model import Campaign
import services.campaign_service as campaign_service


campaign_router = APIRouter()

@campaign_router.get("/api/clients/{client_id}/campaigns")
def get_campaigns(client_id: int, buy_type: Optional[str] = None, 
                  platform: Optional[str] = None, objective: Optional[str] = None) -> dict:
    """
    Get campaigns for the predefined client, filtered by platform, objective, or buy type.
    """
    
    # Add client filtering here.    
    
    campaigns = campaign_service.get_campaigns_for_client(platform=platform, objective=objective, buy_type=buy_type)
    
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
    
    
@campaign_router.get("/api/clients/{client_id}/campaigns/costs")
def get_campaigns(client_id: int) -> dict:
    """
    Get campaign costs
    """
    
    # Add client filtering here.    
    
    campaigns = campaign_service.get_campaigns_for_client()
    
    if not campaigns:
        raise HTTPException(status_code=404, detail="No campaigns found matching the criteria")
    
    return {
        "client": "Brewtopia Coffee House", 
        "campaigns": [
            {
                "campaign-name": campaign.campaign_name,
                "cost-value": int(campaign.cost.removeprefix("PHP ").replace(",", ""))
            }
            for campaign in campaigns
        ]
    }
    
    
@campaign_router.get("/api/clients/{client_id}/campaigns/stats/cpu-per-platform")
def get_cpu_stats():
    stats = campaign_service.get_cpu_stats_by_platform()
    return stats
