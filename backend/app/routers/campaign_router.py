from fastapi import APIRouter, HTTPException, UploadFile, Query
from typing import Optional
from models.campaign_model import Campaign
import services.campaign_service as campaign_service
from io import StringIO
import csv


campaign_router = APIRouter()

@campaign_router.get("/api/clients/{client_id}/campaigns")
def get_campaigns(client_id: int, buy_type: Optional[str] = None, 
                  platform: Optional[str] = None, objective: Optional[str] = None) -> dict:
    """
    Get campaigns for the predefined client, filtered by platform, objective, or buy type.
    """
    
    # Add client filtering here.    
    
    campaigns = campaign_service.get_campaigns_for_client(platform=platform, objective=objective, buy_type=buy_type)
    
    
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
    
    
@campaign_router.post("/api/clients/{client_id}/campaigns")
async def create_upload_file(file: UploadFile):
    contents = await file.read()

    string_io = StringIO(contents.decode("utf-8"))
    csv_reader = csv.DictReader(string_io)
    
    campaigns = []
    for row in csv_reader:
        campaign = Campaign(
            client=row["client"],
            platform=row["platform"],
            buy_type=row["buy-type"],
            objective=row["objective"],
            placement=row["placement"],
            cpu=row["cpu"],
            est_kpi=row["est-kpi"],
            cost=row["cost"],
            campaign_name=row["campaign-name"],
            start=row["start"],
            end=row["end"]
        )
        campaigns.append(campaign)

    campaign_service.add_campaigns(campaigns)
    return {"message": f"Successfully uploaded {len(campaigns)} campaigns."}
        
    
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
    

@campaign_router.get("/api/clients/{client_id}/metrics/cpu")
async def get_cpu_metrics(client_id: str, group_by: str | None = Query(None, alias="group-by")):
    """Get mean and median values of each CPU type for all, each platform, or each objective."""  
    if group_by and group_by.strip().lower() == "platform":
        return campaign_service.get_cpu_metrics_by_platform()
        
    if group_by and group_by.strip().lower() == "objective":
        return campaign_service.get_cpu_metrics_by_objective()
        
    return campaign_service.get_cpu_metrics()
    
    
@campaign_router.get("/api/clients/{client_id}/campaigns/insights")
def get_client_campaign_insights():
    insight_values = campaign_service.get_campaign_cost_insights()
    
    return {
        "client":  "Brewtopia Coffee House",
        "insights": [
            f"Total running cost of campaigns is {insight_values["total_cost"]}.",
            f"Campaign with highest cost is {insight_values["max_cost_campaign"]}, {insight_values["max_cost_percentage"]} of total.",
            f"Average cost of each campaign at {insight_values["mean_cost"]}."
        ]
    }

@campaign_router.get("/api/clients/{client_id}/campaigns/insights/platforms/{platform}")
def get_platform_cpu_insights(platform: str):
    insight_values = campaign_service.get_platform_cpu_insights(platform)
    
    if insight_values["max_cpu_percent_diff"][0] == "-":
        relative_diff = f"{insight_values["max_cpu_percent_diff"][1:]}% lower"
    else:
        relative_diff = f"{insight_values["max_cpu_percent_diff"]}% higher"
        
    
    return {
        "client": "Brewtopia Coffee House",
        "insights": [
            f"Total running cost of {platform.capitalize()} campaigns at {insight_values["total_cost"]}.",
            f"{platform.capitalize()} campaign with highest CPU is {insight_values["max_cpu_campaign"]}, {relative_diff} compared to average CPU of all campaigns.",
        ]
    }
    
    
@campaign_router.get("/api/clients/{client_id}/campaigns/insights/objectives/{objective}")
def get_objective_cpu_insights(objective: str):
    insight_values = campaign_service.get_objective_cpu_insights(objective)
    
    if insight_values["max_cpu_percent_diff"][0] == "-":
        relative_diff = f"{insight_values["max_cpu_percent_diff"][1:]}% lower"
    else:
        relative_diff = f"{insight_values["max_cpu_percent_diff"]}% higher"
        
    return {
        "client": "Brewtopia Coffee House",
        "insights": [
            f"Total running cost of campaigns for {objective.lower()} at {insight_values["total_cost"]}.",
            f"Campaign for {objective.lower()} with highest CPU is {insight_values["max_cpu_campaign"]}, {relative_diff} compared to average CPU of all campaigns.",
        ]
    }
    