
-- 1. Overall marketing performance
SELECT
    COUNT(*) AS total_ads,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    ROUND(SUM(spent), 2) AS total_spend,
    SUM(total_conversion) AS total_leads,
    SUM(approved_conversion) AS total_approved_conversions,
    ROUND(
        100.0 * SUM(clicks) /
        NULLIF(SUM(impressions), 0), 2
    ) AS ctr_pct,
    ROUND(
        SUM(spent) /
        NULLIF(SUM(approved_conversion), 0), 2
    ) AS cost_per_approved_conversion
FROM marketing_campaigns;


-- 2. Campaign performance
SELECT
    xyz_campaign_id AS campaign_id,
    COUNT(*) AS total_ads,
    SUM(impressions) AS impressions,
    SUM(clicks) AS clicks,
    ROUND(SUM(spent), 2) AS spend,
    SUM(total_conversion) AS leads,
    SUM(approved_conversion) AS approved_conversions,
    ROUND(
        100.0 * SUM(clicks) /
        NULLIF(SUM(impressions), 0), 2
    ) AS ctr_pct,
    ROUND(
        SUM(spent) /
        NULLIF(SUM(approved_conversion), 0), 2
    ) AS cost_per_approved_conversion
FROM marketing_campaigns
GROUP BY xyz_campaign_id
ORDER BY approved_conversions DESC;


-- 3. Age group performance
SELECT
    age,
    SUM(impressions) AS impressions,
    SUM(clicks) AS clicks,
    ROUND(SUM(spent), 2) AS spend,
    SUM(approved_conversion) AS conversions,
    ROUND(
        SUM(spent) /
        NULLIF(SUM(approved_conversion), 0), 2
    ) AS cost_per_conversion
FROM marketing_campaigns
GROUP BY age
ORDER BY conversions DESC;


-- 4. Gender performance
SELECT
    gender,
    SUM(impressions) AS impressions,
    SUM(clicks) AS clicks,
    ROUND(SUM(spent), 2) AS spend,
    SUM(approved_conversion) AS conversions,
    ROUND(
        SUM(spent) /
        NULLIF(SUM(approved_conversion), 0), 2
    ) AS cost_per_conversion
FROM marketing_campaigns
GROUP BY gender
ORDER BY conversions DESC;


-- 5. Top interest segments
SELECT
    interest,
    SUM(impressions) AS impressions,
    ROUND(SUM(spent), 2) AS spend,
    SUM(approved_conversion) AS conversions,
    ROUND(
        SUM(spent) /
        NULLIF(SUM(approved_conversion), 0), 2
    ) AS cost_per_conversion
FROM marketing_campaigns
GROUP BY interest
HAVING SUM(approved_conversion) >= 5
ORDER BY cost_per_conversion ASC
LIMIT 10;
