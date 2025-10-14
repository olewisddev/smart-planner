from typing import List, Optional
from models.campaign_model import Campaign

from collections import defaultdict
import re
from statistics import mean, median


fake_campaigns_db = [
    Campaign(
        client="Brewtopia Coffee House",
        platform="FACEBOOK",
        buy_type="Auction",
        objective="Brand Awareness",
        placement="Feed",
        cpu="PHP 18.00 (CPR)",
        est_kpi="500,000 reaches",
        cost="PHP 9,000",
        campaign_name="Sips of Serenity",
        start="2025-11-01",
        end="2025-11-15"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="INSTAGRAM",
        buy_type="Auction",
        objective="Engagement",
        placement="Stories",
        cpu="PHP 22.00 (CPC)",
        est_kpi="3,000 interactions",
        cost="PHP 6,600",
        campaign_name="Brew Your Moment",
        start="2025-11-03",
        end="2025-11-12"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="YOUTUBE",
        buy_type="CPV",
        objective="Video Views",
        placement="Pre-Roll Ads",
        cpu="PHP 5.50 (CPV)",
        est_kpi="200,000 video views",
        cost="PHP 5,500",
        campaign_name="Roast & Revel",
        start="2025-11-10",
        end="2025-11-20"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="TIKTOK",  # TIKTOK added back
        buy_type="Auction",
        objective="Video Views",
        placement="For You Page",
        cpu="PHP 7.00 (CPV)",
        est_kpi="250,000 video views",
        cost="PHP 7,000",
        campaign_name="Sip & TikTok",
        start="2025-12-01",
        end="2025-12-07"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="FACEBOOK",
        buy_type="Auction",
        objective="Video Views",
        placement="Feed",
        cpu="PHP 6.00 (CPC)",
        est_kpi="150,000 video views",
        cost="PHP 9,000",
        campaign_name="Brewtopia Video Magic",
        start="2025-11-12",
        end="2025-11-22"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="INSTAGRAM",
        buy_type="CPM",
        objective="Brand Awareness",
        placement="Feed",
        cpu="PHP 10.00 (CPM)",
        est_kpi="400,000 impressions",
        cost="PHP 8,000",
        campaign_name="Brewtopia Insta Buzz",
        start="2025-12-01",
        end="2025-12-10"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="YOUTUBE",
        buy_type="CPV",
        objective="Video Views",
        placement="In-Stream Ads",
        cpu="PHP 7.00 (CPV)",
        est_kpi="250,000 video views",
        cost="PHP 8,000",
        campaign_name="Brewtopia YouTube Fever",
        start="2025-12-05",
        end="2025-12-15"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="TIKTOK",  # Another TIKTOK campaign
        buy_type="Auction",
        objective="Brand Awareness",
        placement="For You Page",
        cpu="PHP 8.00 (CPM)",
        est_kpi="300,000 impressions",
        cost="PHP 10,000",
        campaign_name="Tiktok Brew Buzz",
        start="2025-12-01",
        end="2025-12-07"
    ),
]


def get_campaigns_for_client(platform: Optional[str] = None, objective: Optional[str] = None, 
                              buy_type: Optional[str] = None) -> List[Campaign]:
    """
    Fetches the campaigns for the predefined client, filtered by platform, objective, or buy type.
    """
    return [
        campaign for campaign in fake_campaigns_db
        if (platform is None or campaign.platform.lower() == platform.lower()) and
           (objective is None or campaign.objective.lower() == objective.lower()) and
           (buy_type is None or campaign.buy_type.lower() == buy_type.lower())
    ]


def add_campaigns(campaign_list: list[Campaign]):
    """
    Append list of new campaigns to datastore.
    """
    fake_campaigns_db.extend(campaign_list)


def extract_cpu_value(cpu_str: str) -> float:
    match = re.search(r"PHP (\d+(\.\d+)?)", cpu_str)
    return float(match.group(1)) if match else 0.0
    

def get_cpu_metrics():
    """Get mean and median of each CPU type for all campaigns."""
    campaigns = get_campaigns_for_client()
    metrics_groups = defaultdict(list)
    
    for campaign in campaigns:
        cpu_value = float(campaign.cpu.split()[1].replace(",", ""))
        cpu_type = campaign.cpu.split()[-1].replace("(", "").replace(")", "").lower()

        metrics_groups[cpu_type].append(cpu_value)

    overall_metrics = {
        metric: {
            "mean": mean(values),
            "median": median(values)
        }
        for metric, values in metrics_groups.items() if values
    }
    
    return overall_metrics


def calculate_cpu_stats(campaigns: list[Campaign] = None) -> dict[str, float]:
    if campaigns is None:
        campaigns = fake_campaigns_db
    
    cpu_values = [extract_cpu_value(campaign.cpu) for campaign in campaigns]
    return {
        "mean_cpu": mean(cpu_values),
        "median_cpu": median(cpu_values)
    }


def get_cpu_metrics_by_platform():
    """For each platform, get mean and median of each CPU type."""
    campaigns = get_campaigns_for_client()
    platforms = defaultdict(list)
    
    # Group campaigns by platform
    for campaign in campaigns:
        platforms[campaign.platform.lower()].append(campaign)
    
    platform_groups = {}
    for platform, campaigns in platforms.items():
        metrics_groups = defaultdict(list)
        
        for campaign in campaigns:
            cpu_value = float(campaign.cpu.split()[1].replace(",", ""))
            cpu_type = campaign.cpu.split()[-1].replace("(", "").replace(")", "").lower()

            metrics_groups[cpu_type].append(cpu_value)

        platform_groups[platform] = {
            metric: {
                "mean": mean(values),
                "median": median(values)
            }
            for metric, values in metrics_groups.items() if values
        }
            
    return platform_groups


def get_cpu_metrics_by_objective():
    """For each objective, get mean and median of each CPU type."""
    campaigns = get_campaigns_for_client()
    objectives = defaultdict(list)
    
    # Group campaigns by objective
    for campaign in campaigns:
        objectives[campaign.objective.lower()].append(campaign)
        
    objective_groups = {}
    for objective, campaigns in objectives.items():
        metrics_groups = defaultdict(list)
        
        for campaign in campaigns:
            cpu_value = float(campaign.cpu.split()[1].replace(",", ""))
            cpu_type = campaign.cpu.split()[-1].replace("(", "").replace(")", "").lower()

            metrics_groups[cpu_type].append(cpu_value)

        objective_groups[objective] = {
            metric: {
                "mean": mean(values),
                "median": median(values)
            }
            for metric, values in metrics_groups.items() if values
        }
            
    return objective_groups
  
    
def get_campaign_cost_insights() -> dict:
    campaigns_costs = {campaign.campaign_name: float(re.sub(r'[^\d.]', '', campaign.cost)) for campaign in fake_campaigns_db}
        
    return {
        "total_cost": f"{sum(campaigns_costs.values()):,.2f}",
        "max_cost_percentage": f"{((max(campaigns_costs.values()) / sum(campaigns_costs.values())) * 100):.2f}%",
        "max_cost_campaign": max(campaigns_costs, key=campaigns_costs.get),
        "mean_cost": f"{mean(campaigns_costs.values()):,.2f}"
    }
    
    
def get_platform_cpu_insights(platform: str) -> dict:
    platform_campaigns = get_campaigns_for_client(platform)
    
    platform_max_cpu = max(platform_campaigns, key=lambda m: extract_cpu_value(m.cpu))
    mean_cpu_all = calculate_cpu_stats().get("mean_cpu")
    max_cpu_percent_diff = (extract_cpu_value(platform_max_cpu.cpu) - mean_cpu_all) / mean_cpu_all
    
    return {
        "total_cost": f"{sum([float(re.sub(r'[^\d.]', '', campaign.cost)) for campaign in platform_campaigns]):,.2f}",
        "max_cpu_campaign": platform_max_cpu.campaign_name,
        "max_cpu_percent_diff": f"{max_cpu_percent_diff:,.2f}"
    }
        
    
def get_objective_cpu_insights(objective: str) -> dict:
    objective_campaigns = get_campaigns_for_client(None, objective)
    
    objective_max_cpu = max(objective_campaigns, key=lambda m: extract_cpu_value(m.cpu))
    mean_cpu_all = calculate_cpu_stats().get("mean_cpu")
    max_cpu_percent_diff = (extract_cpu_value(objective_max_cpu.cpu) - mean_cpu_all) / mean_cpu_all

    return {
        "total_cost": f"{sum([float(re.sub(r'[^\d.]', '', campaign.cost)) for campaign in objective_campaigns]):,.2f}",
        "max_cpu_campaign": objective_max_cpu.campaign_name,
        "max_cpu_percent_diff": f"{max_cpu_percent_diff:,.2f}"
    }
      