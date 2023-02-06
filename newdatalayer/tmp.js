
const flowers = [
    {"strain":"Peanut Butter Pie","type":"Indica","farm":"Noble","weight_in_grams":1.09,"thc_percent":27.3,"cbd_percent":0.09,"harvest":"10/22/19","description":"Indoor/outdoor terpenes","price":12.0,"count":10,"product":"flower"},
    {"strain":"Sunset Sherbert","type":"Hybrid","farm":"HighWinds","weight_in_grams":1.01,"thc_percent":28.4,"cbd_percent":0.1,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":11.0,"count":10,"product":"flower"},
    {"strain":"Headdog","type":"Hybrid","farm":"Heros of the Farm","weight_in_grams":1.04,"thc_percent":26.64,"cbd_percent":0.07,"harvest":"11/14/19","description":"Indoor/outdoor terpenes","price":8.0,"count":10,"product":"flower"},
    {"strain":"OG KB","type":"Indica","farm":"Makru Farms","weight_in_grams":1.04,"thc_percent":25.03,"cbd_percent":0.09,"harvest":"10/21/19","description":"Indoor/outdoor terpenes","price":10.0,"count":10,"product":"flower"},
    {"strain":"Lost Cause","type":"Sativa","farm":"Trichome","weight_in_grams":1.08,"thc_percent":22.06,"cbd_percent":0.0,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":9.0,"count":10,"product":"flower"},
    {"strain":"Peanut Butter Pie","type":"Indica","farm":"Noble","weight_in_grams":1.09,"thc_percent":27.3,"cbd_percent":0.09,"harvest":"10/22/19","description":"Indoor/outdoor terpenes","price":12.0,"count":10,"product":"flower"},
    {"strain":"Sunset Sherbert","type":"Hybrid","farm":"HighWinds","weight_in_grams":1.01,"thc_percent":28.4,"cbd_percent":0.1,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":11.0,"count":10,"product":"flower"},
    {"strain":"Headdog","type":"Hybrid","farm":"Heros of the Farm","weight_in_grams":1.04,"thc_percent":26.64,"cbd_percent":0.07,"harvest":"11/14/19","description":"Indoor/outdoor terpenes","price":8.0,"count":10,"product":"flower"},
    {"strain":"OG KB","type":"Indica","farm":"Makru Farms","weight_in_grams":1.04,"thc_percent":25.03,"cbd_percent":0.09,"harvest":"10/21/19","description":"Indoor/outdoor terpenes","price":10.0,"count":10,"product":"flower"},
    {"strain":"Lost Cause","type":"Sativa","farm":"Trichome","weight_in_grams":1.08,"thc_percent":22.06,"cbd_percent":0.0,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":9.0,"count":10,"product":"flower"},
    {"strain":"Peanut Butter Pie","type":"Indica","farm":"Noble","weight_in_grams":1.09,"thc_percent":27.3,"cbd_percent":0.09,"harvest":"10/22/19","description":"Indoor/outdoor terpenes","price":12.0,"count":10,"product":"flower"},
    {"strain":"Sunset Sherbert","type":"Hybrid","farm":"HighWinds","weight_in_grams":1.01,"thc_percent":28.4,"cbd_percent":0.1,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":11.0,"count":10,"product":"flower"},
    {"strain":"Headdog","type":"Hybrid","farm":"Heros of the Farm","weight_in_grams":1.04,"thc_percent":26.64,"cbd_percent":0.07,"harvest":"11/14/19","description":"Indoor/outdoor terpenes","price":8.0,"count":10,"product":"flower"},
    {"strain":"OG KB","type":"Indica","farm":"Makru Farms","weight_in_grams":1.04,"thc_percent":25.03,"cbd_percent":0.09,"harvest":"10/21/19","description":"Indoor/outdoor terpenes","price":10.0,"count":10,"product":"flower"},
    {"strain":"Lost Cause","type":"Sativa","farm":"Trichome","weight_in_grams":1.08,"thc_percent":22.06,"cbd_percent":0.0,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":9.0,"count":10,"product":"flower"},
    {"strain":"Peanut Butter Pie","type":"Indica","farm":"Noble","weight_in_grams":1.09,"thc_percent":27.3,"cbd_percent":0.09,"harvest":"10/22/19","description":"Indoor/outdoor terpenes","price":12.0,"count":10,"product":"flower"},
    {"strain":"Sunset Sherbert","type":"Hybrid","farm":"HighWinds","weight_in_grams":1.01,"thc_percent":28.4,"cbd_percent":0.1,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":11.0,"count":10,"product":"flower"},
    {"strain":"Headdog","type":"Hybrid","farm":"Heros of the Farm","weight_in_grams":1.04,"thc_percent":26.64,"cbd_percent":0.07,"harvest":"11/14/19","description":"Indoor/outdoor terpenes","price":8.0,"count":10,"product":"flower"},
    {"strain":"OG KB","type":"Indica","farm":"Makru Farms","weight_in_grams":1.04,"thc_percent":25.03,"cbd_percent":0.09,"harvest":"10/21/19","description":"Indoor/outdoor terpenes","price":10.0,"count":10,"product":"flower"},
    {"strain":"Lost Cause","type":"Sativa","farm":"Trichome","weight_in_grams":1.08,"thc_percent":22.06,"cbd_percent":0.0,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":9.0,"count":10,"product":"flower"},
    {"strain":"Peanut Butter Pie","type":"Indica","farm":"Noble","weight_in_grams":1.09,"thc_percent":27.3,"cbd_percent":0.09,"harvest":"10/22/19","description":"Indoor/outdoor terpenes","price":12.0,"count":10,"product":"flower"},
    {"strain":"Sunset Sherbert","type":"Hybrid","farm":"HighWinds","weight_in_grams":1.01,"thc_percent":28.4,"cbd_percent":0.1,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":11.0,"count":10,"product":"flower"},
    {"strain":"Headdog","type":"Hybrid","farm":"Heros of the Farm","weight_in_grams":1.04,"thc_percent":26.64,"cbd_percent":0.07,"harvest":"11/14/19","description":"Indoor/outdoor terpenes","price":8.0,"count":10,"product":"flower"},
    {"strain":"OG KB","type":"Indica","farm":"Makru Farms","weight_in_grams":1.04,"thc_percent":25.03,"cbd_percent":0.09,"harvest":"10/21/19","description":"Indoor/outdoor terpenes","price":10.0,"count":11,"product":"flower"},
    {"strain":"Lost Cause","type":"Sativa","farm":"Trichome","weight_in_grams":1.08,"thc_percent":22.06,"cbd_percent":0.0,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":9.0,"count":9,"product":"flower"},
    ]

let seen = {} 

for ( i in flowers ) { 
    const v = flowers[i] 
    const s = JSON.stringify(v)
    if ( seen.hasOwnProperty(s)) {
        seen[s]++
    } else {
        seen[s] = 1
    }
}
console.log( seen )