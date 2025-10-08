from typing import List, Optional
from models.campaign_model import Campaign


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
        platform="TIKTOK",
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
        platform="GOOGLE",
        buy_type="CPC",
        objective="Search Traffic",
        placement="Google Search Results",
        cpu="PHP 5.50 (CPC)",
        est_kpi="20,000 clicks",
        cost="PHP 4,000",
        campaign_name="Find Your Brew",
        start="2025-12-05",
        end="2025-12-15"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="PINTEREST",
        buy_type="CPM",
        objective="Traffic",
        placement="Promoted Pins",
        cpu="PHP 10.00 (CPM)",
        est_kpi="50,000 impressions",
        cost="PHP 5,000",
        campaign_name="Pin Your Favorite Brew",
        start="2025-12-10",
        end="2025-12-18"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="LINKEDIN",
        buy_type="CPC",
        objective="Lead Generation",
        placement="LinkedIn Feed",
        cpu="PHP 15.00 (CPC)",
        est_kpi="1,000 leads",
        cost="PHP 15,000",
        campaign_name="Brewtopia Business Brew",
        start="2025-12-15",
        end="2025-12-25"
    ),
    Campaign(
        client="Brewtopia Coffee House",
        platform="TWITTER",
        buy_type="CPM",
        objective="Brand Awareness",
        placement="Twitter Feed",
        cpu="PHP 12.00 (CPM)",
        est_kpi="100,000 impressions",
        cost="PHP 12,000",
        campaign_name="Brewtopia Twitter Blitz",
        start="2025-12-01",
        end="2025-12-10"
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
